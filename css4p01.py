# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

md = pd.read_csv("movie_dataset.csv")

md = md.rename(columns = {'Runtime (Minutes)':'Runtime_(Minutes)'})

md = md.rename(columns = {'Revenue (Millions)':'Revenue_(Millions)'})

new_md = md.dropna(subset=['Revenue_(Millions)'], how='all')

new_md = new_md.drop(columns = "Rank")
new_md = new_md.drop(columns = "Description")
new_md = new_md.drop(columns = "Votes")
new_md = new_md.drop(columns = "Metascore")

#Q01
Highest_rated_movie = new_md.loc[new_md['Rating'].idxmax()]['Title']
print(f"The highest rated movie is: {Highest_rated_movie}")

#Q02
Revenue = 'Revenue_(Millions)'
Average_revenue = new_md[Revenue].mean()
print(f"The average revenue of all movies is: {Average_revenue} Million")

#Q03
Year_column = 'Year'
filtered_md = new_md[(new_md[Year_column] >= 2015) & (new_md[Year_column] <= 2017)]
New_Average_revenue = filtered_md[Revenue].mean()
print(f"The average revenue of all movies  between 2015 and 2017 is: {New_Average_revenue} Million")

#Q04
Target_year = 2016
Movies_in_2016 = md[md[Year_column] == Target_year]
Number_of_movies = Movies_in_2016.shape[0]
print(f"Number of movies released in {Target_year}: {Number_of_movies}")

#Q05
Director_names = 'Director'
Target_director = 'Christopher Nolan'
Director = md[md[Director_names] == Target_director]
Number_of_directed_movies = Director.shape[0]
print(f"The number of movies directed by '{Target_director}' is: {Number_of_directed_movies}")

#Q06
Rating_column = 'Rating'
filtered_rating = md[(md[Rating_column] >= 8.0)]
Number_of_movies__atleast_8_rating = filtered_rating.shape[0]
print(f"The number of movies with a rating of atleast 8.0 rating is: {Number_of_movies__atleast_8_rating}")

#Q07
Median_rating = Director[Rating_column].median()
print(f"The median rating  of all the movies directed by '{Target_director}' is: {Median_rating}")

#Q08
Average_ratings_by_year = md.groupby('Year')['Rating'].mean()
Highest_avg_rating_year = Average_ratings_by_year.idxmax()
print(f"The year with the highest average rating is: {Highest_avg_rating_year}")

#Q09
Movies_2006 = md[md['Year'] == 2006]
Movies_2016 = md[md['Year'] == 2016]
Num_Movies_2006 = len(Movies_2006)
Num_Movies_2016 = len(Movies_2016)
Percentage_increase = ((Num_Movies_2016 - Num_Movies_2006) / Num_Movies_2006) * 100
print(f"The percentage increase in the number of movies between 2006 and 2016 is: {Percentage_increase:.2f} %")

#Q10
Actors_column = 'Actors'
All_names = new_md[Actors_column].str.split(',', expand=True).stack()
Unique_name_counts = All_names.value_counts()
print(Unique_name_counts)

#Q11
Unique_genres = md['Genre'].unique()
Num_unique_genres = len(Unique_genres)
print(f'The number of unique genres in the dataset is: {Num_unique_genres}')

#Q12
md = md.select_types(include =["float", "tat"])
movie_correlation = md.corrr()
sns.heatmap(movie_correlation, annot = True, cmap="coolware", fmt =".2f")
plt.ttle("correction heatmap")
plt.show()
