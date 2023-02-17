'''
    Program that defines and implements movie_similarity
    for comparing movie description's similarity
'''

import spacy

nlp = spacy.load('en_core_web_md')

def movie_similarity(target_desc: str) -> str:
    '''Reads from 'movies.txt' a list of movies and descriptions.
        For each description, it will compare the similarity with
        the provided description and return the title of the movie
        with the most similar movie description'''

    # Read the movies and descriptions from 'movies.txt'    
    file_movies = []
    try:
        with open('movies.txt', 'r') as file:
            for line in file:
                file_movies.append(line.strip().split(':'))
    except:
        print("Couldn't read file")
        return None

    # Find movie with best similarity
    best_similarity = 0
    best_movie = None
    target_doc = nlp(target_desc)
    for title, desc in file_movies:
        doc = nlp(desc)
        similarity = target_doc.similarity(doc)
        if similarity > best_similarity:
            best_similarity = similarity
            best_movie = title.strip()

    return best_movie



planet_hulk = ("Will he save their world or destroy it? When the Hulk becomes too dangerous for the "
                "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a "
                "planet where the Hulk can live in peace. Unfortunately, Hulk land on the "
                "planet Sakaar where he is sold into slavery and trained as a gladiator.")

best_match = movie_similarity(planet_hulk)
print(f'The movie to watch is {best_match}')

