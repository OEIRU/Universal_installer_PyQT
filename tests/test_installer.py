import unittest
import os
import shutil
from src.installer import extract_archive, install_program, create_linux_shortcut, create_windows_shortcut, \
    create_uninstall_script


class TestInstaller(unittest.TestCase):

    def setUp(self):
        # Создание временной директории для тестов
        self.test_dir = 'test_install_dir'
        self.archive_path = 'resources/myapp.zip'
        self.extract_to = 'test_extracted'
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.extract_to, exist_ok=True)

    def tearDown(self):
        # Очистка после тестов
        shutil.rmtree(self.test_dir, ignore_errors=True)
        shutil.rmtree(self.extract_to, ignore_errors=True)
        if os.path.exists(f"{os.path.expanduser('~')}/.local/share/applications/myapp.desktop"):
            os.remove(f"{os.path.expanduser('~')}/.local/share/applications/myapp.desktop")
        if os.path.exists(os.path.join(os.path.expanduser('~'), 'Desktop', 'MyApp.lnk')):
            os.remove(os.path.join(os.path.expanduser('~'), 'Desktop', 'MyApp.lnk'))

    def test_extract_archive(self):
        # Проверка разархивирования
        extract_archive(self.archive_path, self.extract_to)
        self.assertTrue(os.path.exists(os.path.join(self.extract_to, 'myapp')))

    def test_install_program(self):
        # Проверка установки программы
        extract_archive(self.archive_path, self.extract_to)
        install_program(self.extract_to, self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'myapp')))

    def test_create_linux_shortcut(self):
        # Проверка создания ярлыка в Linux
        if os.name == 'posix':
            create_linux_shortcut(self.test_dir)
            self.assertTrue(os.path.exists(f"{os.path.expanduser('~')}/.local/share/applications/myapp.desktop"))

    def test_create_windows_shortcut(self):
        # Проверка создания ярлыка в Windows
        if os.name == 'nt':
            create_windows_shortcut(self.test_dir)
            self.assertTrue(os.path.exists(os.path.join(os.path.expanduser('~'), 'Desktop', 'MyApp.lnk')))

    def test_create_uninstall_script_linux(self):
        # Проверка создания скрипта деинсталляции для Linux
        if os.name == 'posix':
            create_uninstall_script(self.test_dir)
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'uninstall.sh')))

    def test_create_uninstall_script_windows(self):
        # Проверка создания скрипта деинсталляции для Windows
        if os.name == 'nt':
            create_uninstall_script(self.test_dir)
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'uninstall.bat')))


if __name__ == '__main__':
    unittest.main()
