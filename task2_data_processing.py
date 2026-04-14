import pandas as pd
import glob

#Read teh json in dataframes
jsn = glob.glob(r"data\trends_*.json")
df = pd.read_json(jsn[0])

#we are taking 0 insex of shape funtion

print(f"Loaded {df.shape[0]} stories from {jsn[0]}")

#we are taking 0 insex of shape funtion

len_of_dup_post_id = len(df[df.duplicated(subset="post_id")].sort_values(by="post_id"))

#print(f"no of post_id duplicates {len_of_dup_post_id}")

#Dropping the duplicates on post_id

df = df.drop_duplicates(subset="post_id")

print(f"After removing duplicates: {df.shape[0]}")

# Dropping the null values on the below rows

df = df.dropna(subset=["post_id","title","score"])

print(f"After removing nulls: {df.shape[0]}")

#Ensuring type as int here

df[["score","num_comments"]] = df[["score","num_comments"]].astype("int64")

#removing scores less than 5

df = df[df["score"] >= 5]

print(f"After removing low scores: {df.shape[0]}")

#stripping spaces on the title

df["title"] = df["title"].str.strip()

# print(df)

df = df.reset_index(drop=True)

df.to_csv("data/trends_clean.csv")

print(f"Saved {df.shape[0]} rows to data/trends_clean.csv")


print (f"Stories per category:")

#using value count on catergory which gives the keys and values 
       
category_count = df["category"].value_counts()

# print(category_count)

#we are using the catergory and count as temperaly variables and looping all using for loop to print output

for catergory , count in category_count.items():
    print(f"{catergory}      {count}")

    