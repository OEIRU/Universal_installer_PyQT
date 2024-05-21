import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QLineEdit, QHBoxLayout, QProgressBar
from PyQt5.QtCore import Qt
import os
import shutil

from src.utils import create_shortcut_windows


class ChooseInstallTypeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Выберите тип установки')
        self.setGeometry(100, 100, 400, 150)

        self.label = QLabel('Выберите тип установки:', self)
        self.button_install_folder = QPushButton('Папка для установки', self)
        self.button_install_zip = QPushButton('ZIP-файл для установки', self)

        self.button_install_folder.clicked.connect(self.open_choose_install_folder_window)
        self.button_install_zip.clicked.connect(self.open_choose_install_zip_window)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_install_folder)
        layout.addWidget(self.button_install_zip)
        self.setLayout(layout)

    def open_choose_install_folder_window(self):
        self.install_folder_window = ChooseInstallFolderWindow()
        self.install_folder_window.show()
        self.hide()  # Скрываем текущее окно после открытия окна выбора папки

    def open_choose_install_zip_window(self):
        self.install_zip_window = ChooseInstallZipWindow()
        self.install_zip_window.show()
        self.hide()  # Скрываем текущее окно после открытия окна выбора ZIP-файла
class ChooseInstallFolderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Выберите папку для установки')
        self.setGeometry(100, 100, 500, 200)
        self.show()  # Покажем окно выбора папки для установки

        self.label_install_folder = QLabel('Выберите папку для установки программы:', self)
        self.line_edit_install_folder = QLineEdit()
        self.line_edit_install_folder.setReadOnly(True)
        self.button_choose_install_folder = QPushButton('Выбрать папку', self)

        self.label_additional_info = QLabel('Выберите папку для ярлыка и дополнительной информации:', self)
        self.line_edit_additional_info = QLineEdit()
        self.line_edit_additional_info.setReadOnly(True)
        self.button_choose_additional_info = QPushButton('Выбрать папку', self)

        self.button_next = QPushButton('Далее', self)
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(0)
        self.progress_bar.setVisible(False)

        self.button_choose_install_folder.clicked.connect(self.choose_install_folder)
        self.button_choose_additional_info.clicked.connect(self.choose_additional_info)
        self.button_next.clicked.connect(self.next_action)

        layout = QVBoxLayout()
        layout.addWidget(self.label_install_folder)
        layout.addWidget(self.line_edit_install_folder)
        layout.addWidget(self.button_choose_install_folder)

        layout.addWidget(self.label_additional_info)
        layout.addWidget(self.line_edit_additional_info)
        layout.addWidget(self.button_choose_additional_info)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button_next)
        h_layout.addWidget(self.progress_bar)

        layout.addLayout(h_layout)
        self.setLayout(layout)

        self.install_folder = None
        self.additional_info_folder = None

    def choose_install_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Выберите папку для установки программы')
        if folder:
            self.line_edit_install_folder.setText(folder)
            self.install_folder = folder

    def choose_additional_info(self):
        folder = QFileDialog.getExistingDirectory(self, 'Выберите папку для ярлыка и дополнительной информации')
        if folder:
            self.line_edit_additional_info.setText(folder)
            self.additional_info_folder = folder

    def next_action(self):
        if self.install_folder and self.additional_info_folder:
            print(f"Выбранная папка для установки программы: {self.install_folder}")
            print(f"Выбранная папка для ярлыка и дополнительной информации: {self.additional_info_folder}")
            self.start_loading()  # Начать индикацию загрузки
            # Добавьте здесь вашу логику, которая должна выполняться после выбора директорий
            self.create_shortcut()
        else:
            print("Не все директории выбраны")

    def start_loading(self):
        self.button_next.setEnabled(False)
        self.progress_bar.setVisible(True)

    def create_shortcut(self):
        # Создание ярлыка и дополнительной информации в дополнительной директории
        if self.install_folder and self.additional_info_folder:
            # Создание ярлыка
            shortcut_path = os.path.join(self.additional_info_folder, "MyApp.lnk")
            target_path = os.path.join(self.install_folder, "myapp.exe")  # Здесь нужно указать реальное имя исполняемого файла
            create_shortcut_windows(target_path, shortcut_path)

            # Создание дополнительной информации (например, текстового файла с описанием программы)
            info_file_path = os.path.join(self.additional_info_folder, "README.txt")
            with open(info_file_path, "w") as f:
                f.write("Дополнительная информация о программе MyApp")

            print("Ярлык и дополнительная информация успешно созданы")

class ChooseInstallZipWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Выберите ZIP-файл для установки')
        self.setGeometry(100, 100, 500, 150)
        self.show()  # Покажем окно выбора ZIP-файла для установки

        self.label_install_zip = QLabel('Выберите ZIP-файл для установки программы:', self)
        self.line_edit_install_zip = QLineEdit()
        self.line_edit_install_zip.setReadOnly(True)
        self.button_choose_additional_info = QPushButton('Выбрать папку', self)

        self.button_next = QPushButton('Далее', self)
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(0)
        self.progress_bar.setVisible(False)

        self.button_choose_install_zip.clicked.connect(self.choose_install_zip)
        self.button_choose_additional_info.clicked.connect(self.choose_additional_info)
        self.button_next.clicked.connect(self.next_action)

        layout = QVBoxLayout()
        layout.addWidget(self.label_install_zip)
        layout.addWidget(self.line_edit_install_zip)
        layout.addWidget(self.button_choose_install_zip)

        layout.addWidget(self.label_additional_info)
        layout.addWidget(self.line_edit_additional_info)
        layout.addWidget(self.button_choose_additional_info)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button_next)
        h_layout.addWidget(self.progress_bar)

        layout.addLayout(h_layout)
        self.setLayout(layout)

        self.install_zip = None
        self.additional_info_folder = None

    def choose_install_zip(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите ZIP-файл для установки программы',
                                                   filter='ZIP files (*.zip)')
        print(file_path)  # Добавим эту строку для отладки
        if file_path:
            self.line_edit_install_zip.setText(file_path)
            self.install_zip = file_path
    def choose_additional_info(self):
        folder = QFileDialog.getExistingDirectory(self, 'Выберите папку для ярлыка и дополнительной информации')
        if folder:
            self.line_edit_additional_info.setText(folder)
            self.additional_info_folder = folder

    def next_action(self):
        if self.install_zip and self.additional_info_folder:
            print(f"Выбранный ZIP-файл для установки программы: {self.install_zip}")
            print(f"Выбранная папка для ярлыка и дополнительной информации: {self.additional_info_folder}")
            self.start_loading()  # Начать индикацию загрузки
            # Добавьте здесь вашу логику, которая должна выполняться после выбора директорий
            self.create_shortcut()
        else:
            print("Не все директории выбраны")

    def start_loading(self):
        self.button_next.setEnabled(False)
        self.progress_bar.setVisible(True)

    def create_shortcut(self):
        # Создание ярлыка и дополнительной информации в дополнительной директории
        if self.install_zip and self.additional_info_folder:
            # Распаковка ZIP-файла
            target_path = os.path.join(self.additional_info_folder, "extracted_files")
            os.makedirs(target_path, exist_ok=True)
            shutil.unpack_archive(self.install_zip, target_path)

            # Создание ярлыка
            shortcut_path = os.path.join(self.additional_info_folder, "MyApp.lnk")
            exec_path = os.path.join(target_path, "myapp.exe")  # Здесь нужно указать реальное имя исполняемого файла
            create_shortcut_windows(exec_path, shortcut_path)

            # Создание дополнительной информации (например, текстового файла с описанием программы)
            info_file_path = os.path.join(self.additional_info_folder, "README.txt")
            with open(info_file_path, "w") as f:
                f.write("Дополнительная информация о программе MyApp")

            print("Ярлык и дополнительная информация успешно созданы")

    def create_shortcut_windows(exec_path, shortcut_path):
        """
        Создает ярлык на рабочем столе Windows.
        :param exec_path: Путь к исполняемому файлу.
        :param shortcut_path: Путь к ярлыку.
        """
        import winshell
        with winshell.shortcut(shortcut_path) as shortcut:
            shortcut.path = exec_path
            shortcut.description = "MyApp"
            # shortcut.icon_location = (icon_path, 0)  # Можно добавить путь к иконке

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = ChooseInstallTypeWindow()
        window.show()
        sys.exit(app.exec_())