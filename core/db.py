from pymongo import MongoClient

client_url = ""
client = MongoClient(client_url)
bot_db = client["discord-bot"]
