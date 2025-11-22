import pymongo
import tornado.ioloop
import tornado.web
import json
from bson import ObjectId

# Connessione sincrona a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["publisher_db"]
publishers_collection = db["publishers"]
books_collection = db["books"]


# Handler principale
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Benvenuto nella API Publisher-Books, da qui puoi avviare la tua ricerca che sia tramite le case editrici o tramite i libri!")
