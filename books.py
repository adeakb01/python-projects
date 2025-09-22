import pandas as pd
df=pd.read_csv('bestsellers.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
df.drop_duplicates(inplace=True)
df.rename(columns={"Name":"Title","Year":"Publication year","User Rating":"Rating"},inplace=True)
df["price"]=df["Price"].astype(float)

# analyzing author popularity
author_counts=df["Author"].value_counts()
print(author_counts)

#analyzing average rating per genre
avg_rating_per_genre=df.groupby("Genre")["Rating"].mean()
print(avg_rating_per_genre)

# saving results to csv
author_counts.head(10).to_csv('top_authors.csv')
avg_rating_per_genre.to_csv('avg_rating_per_genre.csv')