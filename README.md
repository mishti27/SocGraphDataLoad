# SocGraphDataLoad
Python code for loading public Yelp data (businesses, users, reviews) into the graph database Neo4j. 
This data includes:
- Businesses, as well as their type, location, total reviews, and average star rating. This code loads businesses in the categories of ‘RESTAURANT’ or ‘HEALTH’, as those were the business types that I used for my analysis of the Yelp data. 
- Reviews, including the user id, business id, review id, and star rating.
- User-friends data. For the purposes of my analysis, I have only included the friends data.
A special thanks to the folks at Yelp for providing these very interesting and comprehensive datasets for research work. I have abided by the Dataset user agreement, and I encourage anyone else who uses this code to do the same. 
a)	The purpose is purely academic; there is no commercial intent.
b)	The contents of the dataset are never disclosed.
c)	The method and conclusions here are my own and not endorsed by Yelp.
d)	All code and artifacts are published under an open-source (MIT) license.
