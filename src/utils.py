import os
import shutil

from PyQt5.QtWidgets import QFileDialog


def select_directory(title="Выберите директорию"):
    """
    Открывает диалоговое окно для выбора директории.
    :param title: Заголовок окна выбора директории.
    :return: Путь к выбранной директории или None, если выбор отменен.
    """
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.Directory)
    file_dialog.setOption(QFileDialog.ShowDirsOnly, True)
    file_dialog.setWindowTitle(title)
    if file_dialog.exec_():
        return file_dialog.selectedFiles()[0]
    return None


def create_directory(path):
    """
    Создает директорию, если она не существует.
    :param path: Путь к создаваемой директории.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def copy_files(source, destination):
    """
    Копирует файлы из одной директории в другую.
    :param source: Исходная директория.
    :param destination: Директория назначения.
    """
    if os.path.exists(source):
        for item in os.listdir(source):
            src_path = os.path.join(source, item)
            dest_path = os.path.join(destination, item)
            if os.path.isdir(src_path):
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                copy_files(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)


def get_user_home_directory():
    """
    Возвращает путь к домашней директории пользователя.
    :return: Путь к домашней директории.
    """
    return os.path.expanduser("~")


def get_desktop_path():
    """
    Возвращает путь к рабочему столу пользователя.
    :return: Путь к рабочему столу.
    """
    return os.path.join(get_user_home_directory(), "Desktop")


def create_shortcut_linux(exec_path, icon_path, desktop_entry_path):
    """
    Создает .desktop файл для ярлыка на Linux.
    :param exec_path: Путь к исполняемому файлу.
    :param icon_path: Путь к иконке.
    :param desktop_entry_path: Путь к .desktop файлу.
    """
    desktop_entry = f"""
    [Desktop Entry]
    Name=MyApp
    Exec={exec_path}
    Icon={icon_path}
    Type=Application
    Terminal=false
    """
    with open(desktop_entry_path, "w") as f:
        f.write(desktop_entry)


def create_shortcut_windows(exec_path, icon_path, shortcut_path):
    """
    Создает ярлык на рабочем столе Windows.
    :param exec_path: Путь к исполняемому файлу.
    :param icon_path: Путь к иконке.
    :param shortcut_path: Путь к ярлыку.
    """
    import winshell
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = exec_path
        shortcut.description = "MyApp"
        shortcut.icon_location = (icon_path, 0)


def create_uninstall_script(install_dir, platform='linux'):
    """
    Создает скрипт деинсталляции для программы.
    :param install_dir: Директория установки программы.
    :param platform: Платформа (linux или windows).
    """
    if platform == 'linux':
        script_path = os.path.join(install_dir, 'uninstall.sh')
        script_content = f"""#!/bin/bash
rm -rf "{install_dir}"
echo "Программа удалена."
"""
    elif platform == 'windows':
        script_path = os.path.join(install_dir, 'uninstall.bat')
        script_content = f"""@echo off
rmdir /S /Q "{install_dir}"
echo Программа удалена.
"""
    else:
        raise ValueError("Unsupported platform")

    with open(script_path, "w") as script_file:
        script_file.write(script_content)

    if platform == 'linux':
        os.chmod(script_path, 0o755)
