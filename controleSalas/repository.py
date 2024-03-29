from django.conf import settings
import pymongo

class RepositorioSalas:

    class SalaNaoEncontradaException(Exception):
        pass

    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def getConnection(self):
        client = pymongo.MongoClient(
            getattr(settings, "CONNECTION_STRING"))
        connection = client[
            getattr(settings, "DATABASE_NAME")]
        return connection
    
    def get_sala_by_id(self, sala_id):
        conn = self.getConnection()
        collection = conn[self.collection]
        sala = collection.find_one({"_id": sala_id})
        if sala:
            return sala
        else:
            raise self.SalaNaoEncontradaException("Sala não encontrada")

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