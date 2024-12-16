import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = list()
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            movies.append(json.load(f))
    return movies


def get_single_comedy(movies: list) -> str:
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]
        

def get_movie_most_nominations(movies: list) -> str:
    top_movie = {"nominations":0, "movie":None}
    for movie in movies:
        # get nominations
        awards_words:list = movie["Awards"].split(" ")
        nomination_index = awards_words.index("nominations.")
        nominations = int(awards_words[nomination_index-1])
        if nominations > top_movie["nominations"]:
            top_movie = {"nominations":nominations, "movie":movie["Title"]}
    return top_movie["movie"]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    longest_movie = {"runtime":0, "movie":None}
    for movie in movies:
        runtime = int(movie["Runtime"].split(" ")[0])
        if runtime > longest_movie["runtime"]:
            longest_movie = {"runtime":runtime, "movie":movie["Title"]}
    return longest_movie["movie"]

