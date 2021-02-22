# Выпускная работа по автоматизации тестирования
[![Build Status](https://travis-ci.org/Miami-stack/graduation_work_automation.svg?branch=main)](https://travis-ci.org/Miami-stack/graduation_work_automation)

# Тестируемый ресурс:
* URL https://www.saucedemo.com/

В рамках этого проекта автоматизированы основные позитивные и негативные сценарии

# Стэк технологий:
* Selenium WebDriver, Python, Pytest, Allure

# Запуск тестов

1. Клонирование репозитория https://github.com/Miami-stack/graduation_work_automation.git
2. (Этот шаг опциональный) Создать виртуальное окружение
   * Если не установлен `virtualenv` , то выполнить `pip install virtualenv`
   * Создать и активировать виртульное окружение
       ```
       virtualenv <env_name>
       <env_name>\Scripts\activate
       ```
3. Запуск тестов
   * Запуск в режиме headless ( Без GUI )
        ```
        pytest --headless true
        ```
   * Запуск с GUI
       ```
       pytest
       ```
   * Запуск конкретного теста
       ```
       pytest <path_to_filename>
       ```
       * примеч. Данные команды нужно вводить в терминале




# Контроль качества кода

Реализован с помощью pre-commit hook, который проверяет и форматирует код перед коммитом.

## Установка

    pip install pre-commit
    pre-commit install

## Использование

Хук запускается автоматически перед коммитом. Принудительный запуск:

    pre-commit run --all-files

## Запуск конкретной проверки

  `pre-commit run <hook_id> <options>`

`hook-id`  - идентификатор хука;
`-a, --all-files`   - запуск всех все файлов в репозитории;
`--files [FILES[FILES...]]`   - запуск для конкретных файлов.


# Отчёты

Для удобного анализа результатов тестирования, добавлен функционал построения очётов

## Отчёты в Allure

### Установка
**Установка на Linux**

  * Необходимо проверить, установлена ли Java. Для этого ввести echo $JAVA_HOME. Если не отобразился путь Java, то необходимо установить и добавить в переменные окружения.
    * Установка Java
      ```
      sudo apt update
      sudo apt install default-jre -y
      sudo apt install default-jdk -y
      javac -version
      ```
    * Добавить в переменную окружения JAVA_HOME
        ```
        export JAVA_HOME=$(readlink -f /usr/bin/javac | sed "s:/bin/javac::")
        ```

* Команды для установки Allure:
    ```
    1. curl -o allure-2.7.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz
    2. sudo tar -zxvf allure-2.7.0.tgz -C /opt/
    3. sudo ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure
    4. allure --version
    ```
    * Если после выполнения последней команды отобразилась версия allure, значит все установилось.


**Установка на Windows**

В powershell выполнить две команды для установки scoop:

    Set-ExecutionPolicy RemoteSigned -scope CurrentUser

    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('[https://get.scoop.sh]')

**Allure**

C помощью scoop установить Allure:

       scoop install allure

>Необходимо проверить, установлена ли Java. Для этого ввести allure и нажать enter. Если не установлена, то необходимо установить и добавить в переменные окружения. Что бы добавить в переменные окружения , в powershell выполнить команду $env:JAVA_HOME="PATH_TO_JAVA"

### Запуск

    pytest --alluredir <dir_name>

### Просмотр отчёта

> Запустить команду в терминале в той папке, где лежит <dir_name>

    allure serve <dir_name>
