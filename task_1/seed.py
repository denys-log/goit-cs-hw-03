import logging
from faker import Faker
import psycopg2
from psycopg2 import DatabaseError
import random

# Налаштування Faker
fake = Faker()

# Конфігурація підключення до бази даних
db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1234",
    "host": "localhost"
}


def generate_users(n=10):
    """Генерує випадкові дані для таблиці користувачів"""
    return [(fake.name(), fake.unique.email()) for _ in range(n)]


def generate_statuses():
    """Генерує фіксовані статуси для таблиці статусів"""
    return [('new',), ('in progress',), ('completed',)]


def generate_tasks(n=30):
    """Генерує випадкові дані для таблиці завдань"""
    tasks = []
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.randint(1, 3)
        user_id = random.randint(1, 10)
        tasks.append((title, description, status_id, user_id))
    return tasks


def populate_database():
    conn = None
    try:
        # Підключення до бази даних
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Вставка користувачів
        users = generate_users()
        cur.executemany(
            "INSERT INTO users (fullname, email) VALUES (%s, %s)", users)

        # Вставка статусів
        statuses = generate_statuses()
        cur.executemany(
            "INSERT INTO status (name) VALUES (%s)", statuses)

        # Вставка завдань
        tasks = generate_tasks()
        cur.executemany(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        # Заверщення транзакції
        conn.commit()

        # Закриття курсора і підключення
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    populate_database()
