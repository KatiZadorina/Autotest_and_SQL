Автоматизация теста к API
Автоматизирован сценарий, который подготовили коллеги-тестировщики:
1. Клиент создает заказ.
2. Проверяется, что по треку заказа можно получить данные о заказе.

Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.

Для запуска тестов должны быть установлены пакеты pytest и requests
Запуск всех тестов выполянется командой pytest

Документация API доступна после запуска стенда (сервера) по адресу`https://{id}.serverhub.praktikum-services.ru/docs/`

URL, который нужно использовать в запросах к API: `https://{id}.serverhub.praktikum-services.ru`