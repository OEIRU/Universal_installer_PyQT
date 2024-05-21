#!/bin/bash

# Путь к архиву и директория установки
ARCHIVE_PATH="myapp.zip"
INSTALL_DIR="$HOME/MyApp"
DESKTOP_ENTRY="$HOME/.local/share/applications/myapp.desktop"
UNINSTALL_SCRIPT="$INSTALL_DIR/uninstall.sh"

# Создание директории установки
mkdir -p "$INSTALL_DIR"

# Распаковка архива
unzip -o "$ARCHIVE_PATH" -d "$INSTALL_DIR"

# Создание .desktop файла
cat <<EOL > "$DESKTOP_ENTRY"
[Desktop Entry]
Name=MyApp
Exec=$INSTALL_DIR/myapp
Icon=$INSTALL_DIR/icon.png
Type=Application
Terminal=false
EOL

# Создание скрипта деинсталляции
cat <<EOL > "$UNINSTALL_SCRIPT"
#!/bin/bash
rm -rf "$INSTALL_DIR"
rm "$DESKTOP_ENTRY"
echo "Программа удалена."
EOL

# Установка прав на выполнение для скрипта деинсталляции
chmod +x "$UNINSTALL_SCRIPT"

echo "Программа установлена успешно."
