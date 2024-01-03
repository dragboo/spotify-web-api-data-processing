import pandas as pd

# loading datasets into dataframes
artists_df = pd.read_csv("artists.tsv", sep="\t")
tracks_df = pd.read_csv("tracks.tsv", sep="\t")

# artist with max followers 
max_followers_artist = artists_df.loc[artists_df['followers'].idxmax()]                                         # getting the maximum number of followers
print("\nArtist with the maximum number of followers:")
print("Name: ", max_followers_artist['name'])
print("Genre: ", max_followers_artist['genres'],"\n")

# most productive artist in terms of the number of tracks   
most_productive_artist = tracks_df['id_artists'].str.split(', ').explode().value_counts().idxmax()              # splitting the ids and making it into rows then counting the rows then taking max value from it
most_productive_artist_name = artists_df.loc[artists_df['id'] == most_productive_artist, 'name'].values[0]      # using the track id to check for the name of the artist in artists df
print("Most productive artist in terms of the number of tracks performed:", most_productive_artist_name, "\n")

def summarize_genres(genres):
    '''
    returns a dataframe with summary of the genres 
    '''
    genre_counts = []
    avg_followers = []
    for genre in genres:
        genre_artists = artists_df[artists_df['genres'].str.contains(genre)]                                     # filtering artists with each genre
        genre_counts.append(len(genre_artists))
        avg_followers.append(genre_artists['followers'].mean())
    summary_df = pd.DataFrame({'genre': genres, 'total N': genre_counts, 'Av.followers': avg_followers})         # creating a summary df
    return summary_df

def get_genre_variants(genre):
    '''
    returns a list of all variants of a genre
    '''
    genre_variants = set()
    for genres in artists_df['genres']:                                                                    
        for g in genres.split(', '):                                                                            # splitting the values by comma and space
            if genre in g:                                                                                      
                genre_variants.add(g)                                                                           # adding the variants to the set
    return list(genre_variants)

# Example usage with jazz
jazz_variants = get_genre_variants("jazz")
print("Variants of jazz:", jazz_variants)
print("Number of jazz variants:", len(jazz_variants), "\n")

def summarize_artist_performance(name):
    '''
    returns summary of an artist
    '''
    artist = artists_df[artists_df['name'] == name]                                     
    artist_id = artist['id'].values[0]                                                                          # getting the artist id (which is unique for every artist)

    total_tracks = len(tracks_df[tracks_df['id_artists'].str.contains(artist_id)])                                                                    # checking for artist_id in the id_artists column
    solo_tracks = len(tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.split(', ').apply(len)==1)])         # checking the no. of artists in the id_artist column which are equal to 1 

    collaborative_tracks = total_tracks - solo_tracks                                                                                                 # calculating the collaborative tracks

    total_popularity_series = tracks_df[tracks_df['id_artists'].apply(lambda x: artist_id in x)]['popularity']                                        # checking if artist id is present in the list of artists id in each track
    avg_total_popularity = total_popularity_series.mean()
    avg_solo_popularity = tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.split(', ').apply(len) == 1)]['popularity'].mean()              # checking for solo popularity and then getting the average                   
    avg_collaborative_popularity = tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.split(', ').apply(len) > 1)]['popularity'].mean()      # checking for avg popularity and then getting the average
    collaborators = len(tracks_df[tracks_df['id_artists'].str.contains(artist_id)]['id_artists'].str.split(', ').explode().unique())                                                 # filtering and getting the no. of collaborators

    print("Number of tracks:", total_tracks)
    print("Number of solo tracks:", solo_tracks)
    print("Number of collabrative tracks:", collaborative_tracks)

    print("Average popularity of total tracks:", avg_total_popularity)
    print("Average popularity of solo tracks:", avg_solo_popularity)
    print("Average popularity of collaborative tracks:", avg_collaborative_popularity)
    print("Number of collaborators:", collaborators, "\n")                  


# example usage with Michael Jackson
summarize_artist_performance("Michael Jackson")

# passing a list of genres to the summarize_genres function
genres_to_summarize = ["pop", "hip hop", "rock", "metal", "jazz", "blues", "country", "folklore"]
genre_summary = summarize_genres(genres_to_summarize)
print(genre_summary)
