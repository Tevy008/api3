# Обрезка ссылок с помощью Битли
Проект создан для сокращения или подсчета кликов по ссылке. Для получения сокращенной ссылки необходимо передать программе ссылку для сокращения. В ином случае, если вы хотите узнать сколько раз переходили по вашей сслыку, необходимо передать сокращенную ссылку.

### Установка
Скачайте необходимые файлы, Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости
так-же можно установить командой предоставленной ниже.
```
pip install -r requirements.txt
```
### Как запустить скрипт
Для запуска скрипта у вас уже должен быть установлен python3.

Для получения необходимой сокращенной ссылки необходимо написать команду такого типа:
```
python main.py --url https://dvmn.org/modules/web-api/lesson/migration-from-website/#8
```

Для получения количества кликов по ссылке необходимо написать команду такого типа:
```
python main.py --url bit.ly/3RdEnxl
```
" bit.ly/3RdEnxl " Это сокращенная ссылка которую вы сократили ранее.

### Переменные окружения
Переменные окружения - Переменные окружения — это глобальные значения, которые хранят различные данные на вашем компьютере. Они доступны для всех программ и могут быть использованы для передачи информации между программами или для контроля поведения программ.

Пример: файл .env
```
BITLY_KEY=40446a048508d97e2476eacdf6284c872516f296
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).