def indivual_serialize(mongoData) -> dict:
    return {
        '_id': str(mongoData['_id']),
        'data': mongoData['data'],
        'password':mongoData['password']
    }


def list_serialize(datas) -> list:
    return [indivual_serialize(data) for data in datas]


def following_names(followings) -> dict:
    following_name = []
    for counter, following in enumerate(followings['data'], 1):
        following_name.append(
            (counter, following['content']['itemContent']['user_results']['result']['legacy']['screen_name']))
    return {'following': following_name}
