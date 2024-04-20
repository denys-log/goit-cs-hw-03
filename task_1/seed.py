import logging
from faker import Faker
import psycopg2
from psycopg2 import DatabaseError

fake = Faker()

conn = psycopg2.connect(host="localhost", database="postgres",
                        user="postgres", password="1234")
cur = conn.cursor()

for _ in range(3):
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)",
                (fake.name(), fake.email()))

status_names = ['new', 'in progress', 'completed']
for idx in range(3):
    cur.execute("INSERT INTO status (name) VALUES (%s)",
                (status_names[idx],))


for entity_id in range(1, 4):
    for _ in range(2):
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                    (fake.word(), fake.word(), entity_id, entity_id))


try:
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    cur.close()
    conn.close()
