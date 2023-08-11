-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
    student_id SERIAL,
    first_name VARCHAR,
    last_name VARCHAR,
    birthday DATE,
    phone VARCHAR
);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE students
ADD COLUMN  middle_name VARCHAR(20);

-- 3. Удалить колонку middle_name
ALTER TABLE students
DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE students
RENAME birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE students
ALTER COLUMN phone SET DATA TYPE VARCHAR(32);


-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name)
VALUES ('Andrew'),('Alex'),('Jack');


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
ALTER TABLE students
TRUNCATE TABLE student RESTART IDENTITY;