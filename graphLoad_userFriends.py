# ##################################################################################################################
# This program inserts the data from the user file into the graph. It creates the users and friend relationships.
# Set the sub-setting criteria here: business type, State, etc., based on the businesses of interest.
#
# Created: Mishti Sarkar, 06/10/24
# ##################################################################################################################


import json
from neo4j import GraphDatabase

neoDB = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "Passw0rd"))
session = neoDB.session()

user_file = "yelp_academic_dataset_user.json"
f = open(user_file, "r", encoding="UTF-8")

n = 0
while True:
        userRec = f.readline()
        if userRec == "":
                break;

        try:
                userRec = json.loads(userRec)
                user_id = userRec["user_id"]
                print("User_id " + user_id)
                friends = userRec["friends"]
                list_of_friends = friends.split(",")
                qryString_checkUser = "MATCH (a:USER_REVIEW) WHERE a.USER_ID = '" + user_id + "' RETURN COUNT(a) AS USER_COUNT"
                result = session.run(qryString_checkUser)
                user_count = (result.data()[0]['USER_COUNT'])

                if user_count > 0 and len(friends) < 1000:
                        x = 0
                        while x < (len(friends)):
                                try:

                                        try:
                                                friend = (list_of_friends[x].lstrip())
                                        except:
                                                break;
                                        qryString_createUserUser_Reln = "MATCH (a:USER_REVIEW), (b:USER_REVIEW) " + \
                                                        "WHERE a.USER_ID = '" + friend + "' AND b.USER_ID = '" + user_id + "' " + \
                                                        "CREATE (a) <- [r:HAS_FRIEND] - (b)"
                                        result = session.run(qryString_createUserUser_Reln)
                                        print("Tried to create relation between " + user_id + " and " + friend)
                                except:
                                        print(qryString_createUserUser_Reln)
                                        print("Could not create relation between " + user_id + " and " + friend)
                                x = x + 1
        except:
                print("Failed to read line " + str(userRec))

        n = n + 1

