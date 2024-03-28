from django.conf import settings
import pymongo

class RepositorioSalas:

    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def getConnection(self):
        client = pymongo.MongoClient(
            getattr(settings, "CONNECTION_STRING"))
        connection = client[
            getattr(settings, "DATABASE_NAME")]
        return connection
    
    def getColletion(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    def getAll(self):
        document = self.getColletion().find({})
        return document
    
    def insert(self, document):
        self.getColletion().insert_one(document)

    def deleteAll(self):
        self.getColletion().delete_many({})