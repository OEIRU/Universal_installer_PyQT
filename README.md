# MyAppInstaller

Универсальный установщик программ для Linux и Windows.  

## Установка зависимостей

```bash
pip install -r requirements.txt
```
## Тестирование и сборка

Для тестирования используйте `tests/` директорию. Создавайте тесты для проверки правильности работы установщика. Можете использовать `unittest` или `pytest`.

Для сборки проекта используйте `setup.py`, если планируете распространять ваш установщик как пакет Python.

Эта структура проекта обеспечивает логичную организацию, облегчающую разработку и поддержку кроссплатформенного установщика.

Для запуска тестов выполните команду:
```bash
python -m unittest discover tests
```

## Запуск 

```bash 
python ./src/main.py
```

# MyAppInstaller

Универсальный установщик программ для Linux и Windows.  

## Установка зависимостей

```bash
pip install -r requirements.txt
```
## Тестирование и сборка

Для тестирования используйте `tests/` директорию. Создавайте тесты для проверки правильности работы установщика. Можете использовать `unittest` или `pytest`.

Для сборки проекта используйте `setup.py`, если планируете распространять ваш установщик как пакет Python.

Эта структура проекта обеспечивает логичную организацию, облегчающую разработку и поддержку кроссплатформенного установщика.

Для запуска тестов выполните команду:
```bash
python -m unittest discover tests
```

## Запуск 

```bash 
python ./src/main.py
```

## TODO:  
- [ ] Графический выбор папки  
- [ ] В зависимости от системы прописать дефолтные папки  
- [ ] Прописать применение иконки в зависимости от системы 
- [ ] Добавить панель со справкой о программе  
- [ ] Оптимизировать requirements  
- [ ] Собрать пакеты  
- [ ] Задача 3 Проверить работоспособность на GUI Linux  
