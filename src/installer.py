import os
import shutil
import zipfile
import logging
from directory_chooser import MainWindow
from src.utils import (
    select_directory, create_directory, copy_files, get_desktop_path,
    create_shortcut_linux, create_shortcut_windows, create_uninstall_script
)

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def extract_archive(archive_path, extract_to):
    """
    Разархивирует указанный архив в указанную директорию.
    :param archive_path: Путь к архиву.
    :param extract_to: Директория для разархивирования.
    """
    logger.debug(f"Начинаем разархивирование {archive_path} в {extract_to}")
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logger.info(f"Разархивирование {archive_path} успешно завершено.")
    except zipfile.BadZipFile:
        logger.error(f"Файл {archive_path} поврежден или не является архивом.")
        raise


def install_program(source, destination):
    """
    Копирует файлы программы из исходной директории в директорию назначения.
    :param source: Исходная директория.
    :param destination: Директория назначения.
    """
    logger.debug(f"Начинаем установку программы из {source} в {destination}")
    try:
        create_directory(destination)
        copy_files(source, destination)
        logger.info(f"Программа успешно установлена в {destination}.")
    except Exception as e:
        logger.error(f"Ошибка при установке программы: {e}")
        raise


def create_linux_shortcut(install_dir):
    """
    Создает ярлык для программы на рабочем столе в Linux.
    :param install_dir: Директория установки программы.
    """
    exec_path = os.path.join(install_dir, 'myapp')
    icon_path = os.path.join(install_dir, 'resources/icon.png')
    desktop_entry_path = os.path.join(os.path.expanduser("~"), ".local/share/applications/myapp.desktop")
    logger.debug(f"Создаем ярлык для Linux: {desktop_entry_path}")
    try:
        create_shortcut_linux(exec_path, icon_path, desktop_entry_path)
        logger.info(f"Ярлык для Linux успешно создан: {desktop_entry_path}")
    except Exception as e:
        logger.error(f"Ошибка при создании ярлыка для Linux: {e}")
        raise


def create_windows_shortcut(install_dir):
    """
    Создает ярлык для программы на рабочем столе в Windows.
    :param install_dir: Директория установки программы.
    """
    exec_path = os.path.join(install_dir, 'myapp.exe')
    icon_path = os.path.join(install_dir, 'resources/icon.ico')
    shortcut_path = os.path.join(get_desktop_path(), 'MyApp.lnk')
    logger.debug(f"Создаем ярлык для Windows: {shortcut_path}")
    try:
        create_shortcut_windows(exec_path, icon_path, shortcut_path)
        logger.info(f"Ярлык для Windows успешно создан: {shortcut_path}")
    except Exception as e:
        logger.error(f"Ошибка при создании ярлыка для Windows: {e}")
        raise



def main():
    """
    Основная функция для запуска процесса установки.
    """
    try:
        logger.debug("Запуск процесса установки.")

        # Шаг 1: Выбор директории установки
        install_dir = select_directory("Выберите директорию для установки MyApp")
        if not install_dir:
            logger.warning("Установка отменена пользователем.")
            return
        logger.info(f"Директория установки выбрана: {install_dir}")

        # Шаг 2: Разархивирование файлов
        archive_path = 'resources/myapp.zip'
        extract_to = os.path.join(install_dir, 'temp')
        extract_archive(archive_path, extract_to)

        # Шаг 3: Установка программы
        install_program(extract_to, install_dir)

        # Шаг 4: Создание ярлыка и скрипта деинсталляции
        if os.name == 'posix':
            create_linux_shortcut(install_dir)
            create_uninstall_script(install_dir, platform='linux')
        elif os.name == 'nt':
            create_windows_shortcut(install_dir)
            create_uninstall_script(install_dir, platform='windows')

        logger.info("Установка завершена успешно.")
    except Exception as e:
        logger.critical(f"Критическая ошибка при установке: {e}")


if __name__ == "__main__":
    try:
        main_window = MainWindow()
        main_window.show()
    except Exception as e:
        print("Произошла ошибка:", e)