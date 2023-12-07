CREATE DATABASE IF NOT EXISTS span;
USE span;

DROP TABLE IF EXISTS `departments`;
CREATE TABLE IF NOT EXISTS `departments` (
    `department_id` INT(11) NOT NULL AUTO_INCREMENT,
    `department_name` VARCHAR(250) NOT NULL DEFAULT '',
    PRIMARY KEY (`department_id`)
    ) ENGINE=MYISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
    `employee_id` INT(11) NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(100) NOT NULL DEFAULT '',
    `middle_name` VARCHAR(100) NOT NULL DEFAULT '',
    `last_name` VARCHAR(100) NOT NULL DEFAULT '',
    `department_id` INT(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (`employee_id`)
    ) ENGINE=MYISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO departments (department_name)
VALUES ('Бухгалтерия'),
        ('Отдел программирования'),
        ('Служба поддержки клиентов');

INSERT INTO employees (first_name, middle_name, last_name, department_id)
VALUES ('Вера', 'Ивановна', 'Степанова', 1),
        ('Анна', 'Петровна', 'Николаева', 1),
        ('Жанна', 'Сергеевна', 'Новикова', 1),
        ('Петр', 'Николаевич', 'Иванов', 2),
        ('Семен', 'Семенович', 'Сидоров', 2),
        ('Василий', 'Иванович', 'Петров', 3);

DROP TABLE IF EXISTS `goods`;
CREATE TABLE IF NOT EXISTS `goods` (
  `goods_id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Код товара',
  `goods_category_id` INT(11) NOT NULL DEFAULT 0 COMMENT 'Код категории товара',
  `goods_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'Название товара',
  `price` DECIMAL(10,2) DEFAULT 0.00 COMMENT 'Цена товара',
  PRIMARY KEY (`goods_id`)
) ENGINE=MYISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Код заказа',
  `order_number` VARCHAR(100) NOT NULL DEFAULT '' COMMENT 'Номер заказа',
  `goods_id` INT(11) NOT NULL DEFAULT 0 COMMENT 'Код товара',
  `quantity` INT(11) DEFAULT 1 COMMENT 'Количество товара',
  `date_of_order` DATETIME DEFAULT '0000-00-00 00:00:00' COMMENT 'Дата заказа',
  PRIMARY KEY (`order_id`)
  ) ENGINE=MYISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `goods_categories`;
CREATE TABLE IF NOT EXISTS `goods_categories` (
    `goods_category_id` INT(11) NOT NULL AUTO_INCREMENT,
    `goods_category_name` VARCHAR(250) NOT NULL DEFAULT '',
    PRIMARY KEY (`goods_category_id`)
    ) ENGINE=MYISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO goods (goods_category_id, goods_name, price)
VALUES (1, 'Электронная книга', 1000),
        (2, 'Программа "Калькулятор"', 2000),
        (3, 'Обновление программы', 500);

INSERT INTO orders (order_number, goods_id, quantity, date_of_order)
VALUES ('№01-2023', 1, 2, NOW()),
        ("№02-2023", 2, 1, NOW()),
        ("№03-2023", 3, 5, NOW());

INSERT INTO goods_categories (goods_category_name)
VALUES ('Гаджеты'),
        ('Программное обеспечение'),
        ('Услуги');
