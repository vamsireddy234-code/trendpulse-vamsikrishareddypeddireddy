# importing the requests module 
import requests
import json
from datetime import datetime 
import time
import os

headers = {"User-Agent": "TrendPulse/1.0"}

# keepinng tje requested data in the form of json to check later in the script for matching the category
catorgeries={
"technology"	:["AI","software","tech","code","computer","data","cloud","API","GPU","LLM"],
"worldnews"	:["war","government","country","president","election","climate","attack","global"],
"sports"	:["NFL","NBA","FIFA","sport","game","team","player","league","championship"],
"science"	:["research","study","space","physics","biology","discovery","NASA","genome"],
"entertainment"	:["movie","film","music","Netflix","game","book","show","award","streaming"]

}


url = "https://hacker-news.firebaseio.com/v0/topstories.json"

try:
#Requesting the data in json from the url
    ids = requests.get(url,headers = headers).json()[:500]
except:
    print("Failed fetching of stories")

# collecting all the catageries in different varibles in the form of json to check the count later
collected = {
    "technology":    [],
    "worldnews":     [],
    "sports":        [],
    "science":       [],
    "entertainment": []
}

# 

# looping the catergory items, where it will give keys and values in cat and kerywords

for cat , keywords in catorgeries.items():
    
    for id in ids:
        #as we are appending below with the category , if it finds any categoty exceeds 25 it will break loop goes for next
        if len(collected[cat]) >= 25:
            break


        url2 = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        #requesting data based on the id we feteched from previous request
        Data = requests.get(url2).json()

        if not Data or "title" not in Data:
            continue

        #print(Data)

        title = Data["title"].lower()
        #print(title)

        #this will come as other catergery which is kept to sort the catergory other than above and will not be collected

        catorgerie = "other"
        
        for keyword in keywords:
            if keyword in title:
                catorgerie = cat
                break
        # if the category is equal to the category of then we are appending the value to above defined json fomate
        if catorgerie == cat:
            collected[cat].append(
                {
                    "post_id" : Data.get("id"),
                    "title"	   : Data.get("title"),
                    "category": cat,
                    "score"	    : Data.get("score"),
                    "num_comments": Data.get("descendants"),
                    "author"	: Data.get("by"),
                    "collected_at" : datetime.now().isoformat()

                })

    time.sleep(2)       
            
            #print(catorgerie.upper() "---"" Data["title"])

# we are adding all catergories in a single list
all_stories = []
for col in collected:
    all_stories += collected[col]

# ew are making directory if not exists
os.makedirs("data", exist_ok=True)
todaytime = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{todaytime}.json"

#we are writing data to file if run 

with open(filename, "w") as f:
    json.dump(all_stories, f, indent=2)

print(f"Collected {len(all_stories)} stories. Saved to {filename}")