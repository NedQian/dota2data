import dota2api
import sys
from pymongo import MongoClient
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

# STEAMID64 - 299067162755072 = STEAMID32
#  103.59.120.5
# API key 2E049A1901D6BA5294434DCDA681DB3C
mongo = MongoClient("mongodb://10.225.194.47:27017")
test_db = mongo.test

api = dota2api.Initialise("2E049A1901D6BA5294434DCDA681DB3C")

#hist = api.get_match_history()

#match_list = api.get_match_details(match_id=2704599943)
# print api.get_match_history(136501192, date_min=1472688000, date_max=1472774400)
# sys.exit(0)
#output_file = open('../output/test.log', 'w')
start_seq_num = 2293449469
for i in range(0, 10):
    match_history = api.get_match_history_by_seq_num(start_seq_num)
    matches = match_history['matches']
    start_seq_num = matches[-1]['match_seq_num'] + 1
    #for m in matches:
    test_db.matches.insert_many(matches)

#output_file.write(str(match_history) + '\n')
#output_file.write(str(match_history))
#output_file.close()


# league_list = api.get_league_listing()
# print league_list
# print len(league_list['leagues'])