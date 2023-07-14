from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from models.models import User
from config.database import collection
from schema.schemas import list_serialize
from services.twitter_spider import Twitter_Conecction
from bson import ObjectId

router = APIRouter()

# GET Request Methods


@router.get('/')
async def get_account_information():
    info = list_serialize(collection.find())
    return info

# POST Request Methods


@router.post('/login')
async def find_account(user_info: User):

    if not user_info.username_or_email or not user_info.password:
        user_info.username_or_email = 'JjooYadate2397'
        user_info.password = 'ps4plus14'

    account = Twitter_Conecction()
    try:
        account.login(user_info.username_or_email, user_info.password)
        info = account.me
        return info
    except:
        raise HTTPException(
            status_code=400, detail="Username/Password was incorect")
    # inserted_id = collection.insert_one(account)
    # return {'status': 'INSERTED', 'id': str(inserted_id.inserted_id)}

# DELET Request Methods


@router.delete('/{id}')
async def delete_account_information(id: str):
    query = {'_id': ObjectId(id)}
    collection.find_one_and_delete(query)
    return {'status': 'OK'}
