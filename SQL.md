SQL - запросы:
1. Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 


SELECT c.login, COUNT(o.inDelivery)AS Количество
FROM 'Couriers' AS c
LEFT JOIN 'Orders' AS o
ON o.courierId = c.id
WHERE o.inDelivery = 'true'
GROUP BY c.login;

2. Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.
Технические примечания:
Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.

SELECT track,
CASE
WHEN finished = 'true' THEN 2
WHEN canсelled = 'true' THEN -1
WHEN inDelivery = 'true' THEN 1
ELSE 0
END
FROM 'Orders';