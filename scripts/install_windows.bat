@echo off

:: Путь к архиву и директория установки
set ARCHIVE_PATH=myapp.zip
set INSTALL_DIR=%USERPROFILE%\MyApp
set DESKTOP_SHORTCUT=%USERPROFILE%\Desktop\MyApp.lnk
set UNINSTALL_SCRIPT=%INSTALL_DIR%\uninstall.bat

:: Создание директории установки
mkdir "%INSTALL_DIR%"

:: Распаковка архива
powershell -Command "Expand-Archive -Force -Path '%ARCHIVE_PATH%' -DestinationPath '%INSTALL_DIR%'"

:: Создание ярлыка на рабочем столе
powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('%DESKTOP_SHORTCUT%'); $s.TargetPath='%INSTALL_DIR%\\myapp.exe'; $s.IconLocation='%INSTALL_DIR%\\icon.ico'; $s.Save()"

:: Создание скрипта деинсталляции
echo @echo off > "%UNINSTALL_SCRIPT%"
echo rmdir /S /Q "%INSTALL_DIR%" >> "%UNINSTALL_SCRIPT%"
echo del "%DESKTOP_SHORTCUT%" >> "%UNINSTALL_SCRIPT%"
echo echo Программа удалена. >> "%UNINSTALL_SCRIPT%"

echo Программа установлена успешно.
