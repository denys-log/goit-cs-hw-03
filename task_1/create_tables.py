import logging
import psycopg2

# Конфігурація підключення до бази даних
db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1234",
    "host": "localhost"
}

# SQL-запити для створення таблиць
create_tables_commands = [
    """
    create table if not exists users (
        id SERIAL primary key,
        fullname VARCHAR(100) not NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    )
    """,
    """
    create table if not exists status (
        id SERIAL primary key,
        name VARCHAR(50) NOT NULL UNIQUE
    )
    """,
    """
    create table if not exists tasks (
        id SERIAL primary key,
        title VARCHAR(100) not null,
        description TEXT,
        status_id INTEGER not null,
        user_id INTEGER not null,
        FOREIGN KEY (status_id) REFERENCES status(id),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,
]


def create_tables():
    conn = None
    try:
        # Підключення до бази даних
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Створення таблиць
        for command in create_tables_commands:
            cur.execute(command)

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
    create_tables()
