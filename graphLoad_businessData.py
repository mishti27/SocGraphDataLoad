# ##################################################################################################
# This program inserts the data from the business file into the graph.
# Set the sub-setting criteria here: business type, State, etc., based on the businesses of interest.
#
# Created: Mishti Sarkar, 06/09/24
# ##################################################################################################

import json
from neo4j import GraphDatabase

neoDB = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
session = neoDB.session()

business_file = "yelp_academic_dataset_business.json"
f = open(business_file, "r", encoding="UTF-8")
# business_file = f.read()

n = 0
while True:
        businessRec = f.readline()
        if businessRec == "":
                break;

        try:
                businessRec = json.loads(businessRec)
                businessType = ""

                if ("Restaurant" in businessRec["categories"]):
                        businessType = "RESTAURANT"
                elif ("Health & Medical" in businessRec["categories"]):
                        businessType = "HEALTH"

                if not(businessType == ""):
                        try:
                                qryString_createBusinessNode = ("CREATE (a:BUSINESS) " + \
                                                "SET a.BUSINESS_ID = " + "'" + businessRec["business_id"] + "', " + \
                                                "a.BUSINESS_TYPE = " + "'" + businessType + "', " + \
                                                "a.BUSINESS_STATE = " + "'" + businessRec["state"] + "', " + \
                                                "a.BUSINESS_POSTAL_CODE = " + "'" + businessRec["postal_code"] + "', " + \
                                                "a.BUSINESS_LATITUDE = " + str(businessRec["latitude"]) + ", " + \
                                                "a.BUSINESS_LONGITUDE = " + str(businessRec["longitude"]) + ", " + \
                                                "a.BUSINESS_STARS = " + str(businessRec["stars"]) + ", " + \
                                                "a.BUSINESS_REVIEW_COUNT = " + str(businessRec["review_count"]) + ", " + \
                                                "a.BUSINESS_IS_OPEN = " + str(businessRec["is_open"]) )
                                result = session.run(qryString_createBusinessNode)
                                print("Loaded Business ID " + businessRec["business_id"])
                        except:
                                print("Failed to create business node " + businessRec["business_id"])
        except:
                print("Failed to read line " + str(businessRec))
        n=n+1