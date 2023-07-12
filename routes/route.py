from fastapi import APIRouter
from models.twitter import Twitter
from config.database import collection
from schema.schemas import list_serialize
from bson import ObjectId

router = APIRouter()

# GET Request Methods


@router.get('/')
async def get_account_information():
    info = list_serialize(collection.find())
    return info

# POST Request Methods


@router.post('/')
async def find_account(data: Twitter):
    account = dict(data)
    inserted_id = collection.insert_one(account)
    return {'status': 'INSERTED', 'id': str(inserted_id.inserted_id)}

# DELET Request Methods


@router.delete('/{id}')
async def delete_account_information(id: str):
    query = {'_id': ObjectId(id)}
    collection.find_one_and_delete(query)
    return {'status': 'OK'}
