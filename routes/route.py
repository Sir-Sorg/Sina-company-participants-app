from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from models.models import User, Viwer
from config.database import collection
from schema.schemas import list_serialize, following_names
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
async def login_account(user_info: User):

    if not user_info.username_or_email or not user_info.password:
        user_info.username_or_email = 'JjooYadate2397'
        user_info.password = 'ps4plus14'

    account = Twitter_Conecction()
    try:
        account.login(user_info.username_or_email, user_info.password)
        info = account.me
        info['password'] = user_info.password
        inserted_id = collection.insert_one(info)
        return {'Status': 'INSERTED', '_id': str(inserted_id.inserted_id)}
    except:
        raise HTTPException(
            status_code=400, detail="Username/Password was incorect")


@router.post('/view')
async def view_account(viewer_info: Viwer):

    if not viewer_info.username or not viewer_info.db_id:
        viewer_info.username = 'JjooYadate2397'
        viewer_info.db_id = '64b191fa90b8e5e94ae68d22'

    try:
        viewer_info.db_id = ObjectId(viewer_info.db_id)
        query = {'_id': viewer_info.db_id}
        account_info = collection.find_one(query)
        username_in_db = account_info['data']['viewer']['user_results']['result']['legacy']['screen_name']
        if username_in_db == viewer_info.username:
            print('Username matched')
            user_id = account_info['data']['viewer']['user_results']['result']['rest_id']
            account = Twitter_Conecction()
            account.login(username_in_db, account_info['password'])
            followings = account.get_friends(user_id, following=True)
            return following_names(followings)
        else:
            return {'Status': 'Failed', 'detail': 'Username dose not match with Database Id'}
    except:
        raise HTTPException(
            status_code=400, detail="Database Id/Username was not valid")


# DELET Request Methods


@router.delete('/{id}')
async def delete_account(id: str):
    query = {'_id': ObjectId(id)}
    collection.find_one_and_delete(query)
    return {'Status': 'DELETED'}
