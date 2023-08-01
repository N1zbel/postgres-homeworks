"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

PASS = os.getenv('pgadmin')

customers_data = "north_data/customers_data.csv"
employees_data = "north_data/employees_data.csv"
orders_data = "north_data/orders_data.csv"

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password=PASS
)
with conn.cursor() as cur:
    with open(employees_data, encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)
        cur.execute('SELECT * FROM employees')
        cur.executemany(
            "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
            reader
        )
        conn.commit()

    with open(customers_data, encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)

        cur.execute('SELECT * FROM customers')
        cur.executemany("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)", reader)
        conn.commit()

    with open(orders_data, encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)
        cur.execute('SELECT * FROM orders')
        cur.executemany(
            "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
            reader
        )
        conn.commit()

conn.close()
