import pandas as pd
import numpy as np

# data fetching fromt he tends_Clean.csv
df = pd.read_csv(r"data\trends_clean.csv")
# using shape to get the matrix
print(f"Loaded data : {df.shape}")

# using head to get first 5 rows
print(f"First 5 rows: {df.head()}")

# using mean to get average of the score and num_comments
print(f"""Average score   : {df["score"].mean()}
Average comments: {df["num_comments"].mean()}""")

# loading the score coulmn in the varaible in array

score = np.array(df["score"])

#assigning the variables with the mean, median, standard deviationm , max and min values

print(score.dtype)
score_mean = np.mean(score)
score_median = np.median(score)
score_std = np.std(score)
score_max = np.max(score)
score_min = np.min(score)

print(f"""--- NumPy Stats ---
Mean score   : {score_mean}
Median score : {score_median}
Std deviation: {score_std}
Max score    : {score_max}
Min score    : {score_min}""")

# using max first occureance of max value

category_max = df["category"].value_counts().idxmax()

# feteching the max value

count_max = df["category"].value_counts().max()

print(f"Most stories in: {category_max} ({count_max} stories)")

# most_comment = df["num_comments"].max()

#using max first occureance whole column of max value with iloc

most_comment = df.loc[df["num_comments"].idxmax()]

print(f"yyyyyyy{most_comment}")

print(f"""Most commented story: "{most_comment['title']}"  — {most_comment['num_comments']} comments""")

# assiging a new table using the given formula

df["engagement"] =  df["num_comments"] / (df["score"] + 1)

avg_scr = df["score"].mean()

# assiging a new table using the given instruction which return boolean

df["is_popular"] = df["score"] > avg_scr

df.to_csv("data/trends_analysed.csv")

print(f"Saved to data/trends_analysed.csv")


