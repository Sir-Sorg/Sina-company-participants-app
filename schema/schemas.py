def indivual_serialize(mongoData) -> dict:
    return {
        'id': str(mongoData['_id']),
        'name': mongoData['name'],
    }


def list_serialize(datas) -> list:
    return [indivual_serialize(data) for data in datas]
