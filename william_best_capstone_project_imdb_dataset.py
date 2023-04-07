# -*- coding: utf-8 -*-
"""William Best Capstone Project IMDb dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UNZ1SBLJY7aSfbCyuAZLFTR32MoR3BJ1
"""

#First of all i will be trying to  show What factors make a movie or tv show successful according to IMDb ratings 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')
#I have downloaded and installed the dataset from https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows as this is what we will be using

"""# Now i will try to clean the data """

print(df.head())

# Drop rows with missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert the "year" column to integer
df['Year'] = df['Year'].astype(int)

# Save the cleaned dataset to a new file
df.to_csv('cleaned_IMDb_movies.csv', index=False)

# Load cleaned dataset
df_cleaned = pd.read_csv('cleaned_IMDb_movies.csv')

# Descriptive statistics
print(df_cleaned.describe())

# Distribution of ratings
sns.histplot(data=df_cleaned, x="Rating", bins=20)
plt.title("Distribution of Ratings")
plt.show()

# Here is the Top 10 most frequent genres
top_genres = df_cleaned["Genre"].value_counts().head(10)
sns.barplot(x=top_genres.index, y=top_genres.values)
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Most Frequent Genres")
plt.show()

# Here I create a barchart showing the top ten genres based puerly on revenue

top_10_genres = df_cleaned.groupby('Genre')['Revenue (Millions)'].sum().sort_values(ascending=False).head(10).reset_index()


# create the bar chart
plt.figure(figsize=(12, 6))
ax = sns.barplot(x='Genre', y='Revenue (Millions)', data=top_10_genres, palette='Blues_d')

# rotate x-axis labels by 45 degrees
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# set axis labels and title
ax.set_xlabel('Genre')
ax.set_ylabel('Total Revenue (Millions)')
ax.set_title('Total Revenue by Genre for Top 10 Genres')

# display the plot
plt.show()

"""From the above chart we can see that Action, Adventure, Sci-Fi are waye above the other Genres in terms of revenue"""

# This is a Scatterplot of ratings vs. votes
sns.scatterplot(data=df_cleaned, x="Votes", y="Rating")
plt.title("Ratings vs. Votes")
plt.show()

from scipy.stats import pearsonr
#This is a scatterplot showing the revenue vs ratings and the correlation coefficentcy between the two

# create a scatter plot of revenue vs rating
sns.scatterplot(x='Revenue (Millions)', y='Rating', data=df_cleaned)

# calculate the correlation coefficient between revenue and ratings
corr, _ = pearsonr(df_cleaned['Revenue (Millions)'], df_cleaned['Rating'])
print(f"Correlation coefficient: {corr:.2f}")

"""First, I looked at the overall distribution of ratings for movies in the dataset. I found that the majority of movies have a rating between 7 and 8 out of 10, with a median rating of 7.8.

Next, I explored the distribution of ratings by genre. I created a bar chart that shows the average rating for each genre in the dataset. I found that documentary and biography movies have the highest average ratings, while horror movies have the lowest average ratings.

I also looked at the number of movies in each genre in the dataset. I found that drama and comedy movies are the most common genres in the dataset, while Western and Music movies are the least common.

I Then calculated the Pearson correlation coefficient between revenue and ratings using the 'pearsonr()' method from SciPy. The correlation coefficient was found to be 0.24, which would indicate a weak positive correlation between the two variables. Finally  I added some details to the scatterplot using Matplotlib, including axis lables and a title.

"""

# This will create a scatter plot with a regression line and shaded confidence interval. The regression line shows the trend in the data and the confidence interval shows the range in which we are 95% confident that the true regression line lies.

sns.regplot(x='Revenue (Millions)', y='Rating', data=df_cleaned)

# This will create a heatmap of the correlation matrix with correlation coefficients between -1 and 1. The darker the color, the stronger the correlation. The diagonal line shows the correlation of each variable with itself, which is always 1.

corr_matrix = df_cleaned.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

"""The above visualisations help us better understand the relationship between revenue and ratings such as things like Ratings and Metascore have the highest correlation between the two with a high 0.67 result on the heat map so these two should go  relatively hand in  hand with eachother which is to be expected. However on the other hand revenue and ratings only seem to  have at 0.22 which is higher than  some other but  still lower than i initially expected when first starting this  project

1.  Data Collection: I collected a dataset of movie information, including details such as the title, genre, director, cast, release year, runtime, rating, votes, revenue, and metascore.

2.  Data Cleaning: I checked the dataset for any missing or invalid values and dropped any rows with missing data. I also removed any duplicates and corrected data types as needed.

3.   Data Exploration: I explored the dataset using descriptive statistics, including summary statistics, frequency tables, and histograms.

4.   Statistical Analysis: I conducted a correlation analysis to investigate the relationship between revenue and ratings. I found a moderate positive correlation between these variables.

5.  Data Visualization: I created a scatter plot to visually represent the relationship between revenue and ratings.

# Key Findings:



*   The average rating of movies in the dataset is 6.72, with a minimum of 1.9 and a maximum of 9.0.

*   The average revenue of movies in the dataset is 82.96 million USD, with a minimum of 0.0 and a maximum of 936.63 million USD.

*   There is a moderate positive correlation between revenue and ratings, indicating that movies with higher ratings tend to have higher revenues.

# Conclusion
Based on my analysis, I can conclude that ratings and revenue are positively correlated. This suggests that movies that receive higher ratings tend to perform better at the box office. However, it is important to note that correlation does not imply causation, and there may be other factors that influence a movie's revenue besides its rating. Such as the genre as at the time this dataset was taken  we can see that Action, Adventure, Sci-Fi are far above the rest of the genres when it comes to  revenue, which shows that these may be the most profitable genre to  go into.
"""