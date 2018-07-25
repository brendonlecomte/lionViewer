from pymongo import MongoClient

client = MongoClient()
db = client['test-database']  # get db from the client. Can use db.val if valid naming
collection = db.test_collection #collection is like a table, class/item/etc
