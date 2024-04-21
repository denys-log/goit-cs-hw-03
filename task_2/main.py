import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError, ConnectionFailure

try:
    client = MongoClient(
        "mongodb+srv://test:1234@cluster0.x0vh5fg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi('1'),
        tlsCAFile=certifi.where()
    )
    db = client["mydatabase"]
    collection = db["cats"]
    # Перевірка з'єднання
    client.admin.command("ismaster")
    print("MongoDB підключена успішно.")
except ConnectionFailure:
    print("Не вдалося підключитися до MongoDB, перевірте з'єднання.")


def create_document():
    try:
        name = input("Введіть ім'я тварини: ")
        age = int(input("Введіть вік тварини: "))
        features_input = input(
            "Введіть особливості тварини, розділенні комою: ")
        features = features_input.split(", ")
        document = {"name": name, "age": age, "features": features}
        collection.insert_one(document)
        print("Документ створено.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


def read_all_documents():
    documents = list(collection.find({}))
    for doc in documents:
        print(doc)


def read_document_by_name():
    name = input("Введіть ім'я тварини для пошуку: ")
    document = collection.find_one({"name": name})
    if document is not None:
        print(document)
    else:
        print("Тварини з таким ім'я немає.")


def update_document_age():
    try:
        name = input("Введіть ім'я тварини для оновлення віку: ")
        age = int(input("Введіть новий вік тварини: "))
        result = collection.update_one(
            {"name": name}, {"$set": {"age": age}})
        if result.modified_count > 0:
            print("Вік тварини оновлено.")
        else:
            print("Тварина не знайдена.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")


def add_feature_to_document():
    try:
        name = input("Введіть ім'я тварини для додавання особливості: ")
        feature = input("Введіть особливість, яку хочете додати: ")
        result = collection.update_one(
            {"name": name}, {"$addToSet": {"features": feature}})
        if result.modified_count > 0:
            print("Особливість додано до тварини.")
        else:
            print("Тварина не знайдена або особливість вже присутня.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")


def delete_document():
    try:
        name = input("Введіть ім'я тварини для видалення: ")
        result = collection.delete_one({"name": name})
        print("Документ видалено.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


def delete_all_documents():
    try:
        collection.delete_many({})
        print("Усі документи видалено.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


def main():
    while True:
        print("\nДоступні дії:")
        print("1 - Створити запис про тварину")
        print("2 - Показати всі записи")
        print("3 - Пошук запису за ім'ям тварини")
        print("4 - Оновити вік тварини")
        print("5 - Додати особливість до тварини")
        print("6 - Видалити запис про тварину")
        print("7 - Видалити всі записи")
        print("8 - Вийти")
        choice = input("Введіть дію: ")

        match choice:
            case "1":
                create_document()
            case "2":
                read_all_documents()
            case "3":
                read_document_by_name()
            case "4":
                update_document_age()
            case "5":
                add_feature_to_document()
            case "6":
                delete_document()
            case "7":
                delete_all_documents()
            case "8":
                break
            case _:
                print("Невірна дія")


if __name__ == "__main__":
    main()
