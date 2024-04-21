import argparse
import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://test:1234@cluster0.x0vh5fg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1'),
    tlsCAFile=certifi.where()
)

db = client.book


parser = argparse.ArgumentParser(description="Add a new cat")
parser.add_argument(
    "--action", help="[read, readOne, updateAge, updateFeatures, deleteByName, deleteAll]")
parser.add_argument("--name", help="Name of the cat")
parser.add_argument("--age", help="Age of the cat")
parser.add_argument("--features", help="Features of the cat")

args = vars(parser.parse_args())
action = args['action']
name = args['name']
age = args['age']
features = args['features']


def read():
    cats = db.cats.find()
    return cats


def readOne(name):
    cats = db.cats.find_one({"name": name})
    return cats


def updateAge(name, age):
    return db.cats.update_one(
        {"name": name}, {"$set": {"age": age}})


def updateFeatures(name, features):
    return db.cats.update_one(
        {"name": name}, {"$push": {"features": features}})


def deleteByName(name):
    return db.cats.delete_one({"name": name})


def deleteAll():
    return db.cats.delete_many({})


if __name__ == "__main__":
    match action:
        case "read":
            [print(cat) for cat in read()]
        case "readOne":
            print(readOne(name))
        case "updateAge":
            result = updateAge(name, age)
            print(result.modified_count)
        case "updateFeatures":
            result = updateFeatures(name, features)
            print(result.modified_count)
        case "deleteByName":
            result = deleteByName(name)
            print(result.deleted_count)
        case "deleteAll":
            result = deleteAll()
            print(result.deleted_count)
        case _:
            print("Wrong action")
