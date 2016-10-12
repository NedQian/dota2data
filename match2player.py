from pymongo import MongoClient
mongo = MongoClient("mongodb://10.225.194.47:27017")
db = mongo.test

matches = db.matches.find({},{'_id': 0})
for m in matches:
    players = m['players']
    del m['players']
    for p in players:
        p['match'] = m
    db.players.insert_many(players)

    db.players.distinct('account_id')
    cursor = db.players.aggregate([
        {"$group": {"_id": "$account_id", "count": {"$sum":1}}}
    ]).find({"$filter": {"input": "count", "as": "p", "cond": {"$gte":[""]}}})

