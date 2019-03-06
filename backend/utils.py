from flask_restful import reqparse

import pymongo
import json
import copy
from bson import json_util

def encoder(input):
    return copy.copy(json.loads(json_util.dumps(input)))

client = pymongo.MongoClient("mongodb://0.0.0.0:27017/")
db = client["driplet"]
col = db["users"]

def gen_fields(parser, fields):
    for field in fields:
        parser.add_argument(field)
    return parser.parse_args()

def user_get(clientid=None, username=None, email=None):
    if clientid != None:
        return col.find({"id": clientid})
    if username != None:
        return col.find({"username": username})
    if email != None:
        return col.find({"email": email})

