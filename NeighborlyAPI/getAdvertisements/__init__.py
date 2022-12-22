import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://cmsdatabasenp:5qHfQVRicZBP8B7iCVoykOcJmVgyP5TEuCS02SHeC94qH4LkAn6EJt7h45SkO2T5b0rQAgazFj7RACDbS6tsig==@cmsdatabasenp.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cmsdatabasenp@"  # TODO1: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

