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
    `department_id` int(11) NOT NULL DEFAULT 0,
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
