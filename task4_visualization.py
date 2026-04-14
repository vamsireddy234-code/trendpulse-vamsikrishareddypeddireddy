import pandas as pd
import os
import matplotlib.pyplot as plt

#imporing the analysed data
df = pd.read_csv(r"data\trends_analysed.csv")

#creating output directory if exists skips error
os.makedirs("outputs", exist_ok=True)

#sorting values in desending 
top_10 = df.sort_values("score",ascending=False)

# copying the value sorted of new top 10 to top_10 variable

top_10 = top_10.head(10).copy()

print(top_10)

# slicing the title with 50 letter only

top_10["title"] = top_10["title"].str[:50]
print(top_10)

# creating the plot for horizontal bar graph

plt.barh(top_10["title"], top_10["score"])
plt.title("Top 10 stories based on the scores")
plt.xlabel("score of the story")
plt.ylabel("title of story")
plt.tight_layout()
plt.savefig("outputs\chart1_top_stories.png")
plt.show()


# sertating the keys and values on the value count 
count = df["category"].value_counts()

# creating the plot for bar graph with colors

# getting the index and values of the count and making them on x and y axis

plt.bar(count.index, count.values , color =["blue", "red" ,"green", "orange","purple"] )
plt.title("Num of stories per catergory")
plt.xlabel("catergory")
plt.ylabel("no of stories")
plt.savefig("outputs\chart2_categories.png")
plt.show()


# taking the popular and non popular data set to differtn variables

popular = df[df["is_popular"] == True]
no_popular = df[df["is_popular"] == False]

# creating the plot for bar scttered with colors

plt.scatter( popular["score"],popular["num_comments"], color = "red" , label = "Popular")
plt.scatter(no_popular["score"] ,no_popular["num_comments"], color = "black" , label = "Non Popular")
plt.title("scores vs comments")
plt.xlabel("scores")
plt.ylabel("comments")
plt.legend()
plt.savefig("outputs\chart3_scatter.png")
plt.show()



#creatig a subplot in a sigle plot using rows , column and position using subplot(1,3,1), (1,3,2) ......

plt.subplot(1,3,1)
plt.barh(top_10["title"], top_10["score"])
plt.title("Top 10 stories based on the scores")
plt.xlabel("score of the story")
plt.ylabel("title of story")


plt.subplot(1,3,2)
plt.bar(count.index, count.values , color =["blue", "red" ,"green", "orange","purple"] )
plt.title("Num of stories per catergory")
plt.xlabel("catergory")
plt.ylabel("no of stories")


plt.subplot(1,3,3)
plt.scatter( popular["score"],popular["num_comments"], color = "red" , label = "Popular")
plt.scatter(no_popular["score"] ,no_popular["num_comments"], color = "black" , label = "Non Popular")
plt.title("scores vs comments")
plt.xlabel("scores")
plt.ylabel("comments")
plt.legend()
plt.suptitle("TrendPulse Dashboard")
plt.savefig("outputs\dashboard.png")
plt.show()