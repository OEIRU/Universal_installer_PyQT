from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
from installer import extract_archive, install_program, create_uninstall_script


def select_directory():
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.Directory)
    if file_dialog.exec_():
        return file_dialog.selectedFiles()[0]


def run_installer():
    app = QApplication([])

    archive_path = QFileDialog.getOpenFileName()[0]
    if not archive_path:
        print("Файл архива не выбран.")
        return

    extract_to = select_directory()
    if not extract_to:
        print("Директория не выбрана.")
        return

    extract_archive(archive_path, extract_to)
    install_path = select_directory()
    if not install_path:
        print("Директория установки не выбрана.")
        return

    install_program(extract_to, install_path)
    create_uninstall_script(install_path)

    app.exec_()
