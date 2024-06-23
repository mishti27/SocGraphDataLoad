# ##################################################################################################################
# This program inserts the data from the reviews file into the graph. It creates the user before creating the review.
# Set the sub-setting criteria here: business type, State, etc., based on the businesses of interest.
#
# Created: Mishti Sarkar, 06/10/24
# ##################################################################################################################

import json
from neo4j import GraphDatabase

neoDB = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
session = neoDB.session()

review_file = "yelp_academic_dataset_review.json"
f = open(review_file, "r", encoding="UTF-8")

n = 0
while True:
        userRec = f.readline()
        if userRec == "":
                break;

        try:
                userRec = json.loads(userRec)
                user_id = userRec["user_id"]
                business_id = userRec["business_id"]
                review_id = userRec["review_id"]
                print("Review :" + review_id)

                try:
                    qryString_checkUser = "MATCH (a:USER_REVIEW) WHERE a.USER_ID = '" + user_id + "' RETURN COUNT(a) AS USER_COUNT"
                    result = session.run(qryString_checkUser)
                    user_count = (result.data()[0]['USER_COUNT'])

                    if user_count == 0:
                        qryString_createUser = "MATCH (a:BUSINESS) WHERE a.BUSINESS_ID = '" + business_id + "' " + \
                                        "CREATE (b:USER_REVIEW) SET b.USER_ID = '" + user_id + "'"
                        result = session.run(qryString_createUser)

                    qryString_createUserBusiness_Reln = "MATCH (a:BUSINESS), (b:USER_REVIEW) " + \
                                                    "WHERE a.BUSINESS_ID = '" + business_id + "' AND b.USER_ID = '" + user_id + "' " + \
                                                    "CREATE (a) <- [r:RATED {STARS: " + str(userRec["stars"]) + ", REVIEW_ID: '" + review_id + "'}] - (b)"
                    # print(qryString_createUserBusiness_Reln)
                    result = session.run(qryString_createUserBusiness_Reln)
                    print("Review created " + review_id)

                except:
                    print("Failed to create node or relation for review " + review_id)
        except:
                print("Failed to read line " + str(userRec))


        n=n+1

