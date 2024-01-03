# spotify-web-api-data-processing

This Python script utilizes the pandas library to process a dataset of artists and their tracks downloaded from the Spotify Web API. The dataset comprises two files: artists.tsv and tracks.tsv, both containing tab-separated values. These files provide information about 240K uniquely identified artists and 450K tracks performed by these artists.

**Questions Addressed:**

**Artist with Maximum Followers:**
Identify and print the name and genre of the artist with the maximum number of followers.

**Most Productive Artist:**
Identify and print the name of the most productive artist in terms of the number of tracks performed.

**Genre Summary:**
Write a function, summarize_genres(genres), that takes a list of genres and returns a dataframe with three columns: "genre," "total N" (total number of artists in each genre), and "Av. followers" (average number of followers of artists in each genre).

**Genre Variants:**
Write a function, get_genre_variants(genre), that takes a genre string and returns an array with all variants of that genre. For example, for "jazz," find how many variants exist in the dataset.

**Artist Performance Summary:**
Write a function, summarize_artist_performance(name), that takes an artist's name and prints various performance-related metrics, such as the number of tracks, solo tracks, collaborative tracks, average popularity of total/solo/collaborative tracks, and the number of collaborators.

**Library used:** <br />

pandas
