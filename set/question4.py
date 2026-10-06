movies_2025 = set(input("Enter movies released in 2025: ").split(","))
watched = set(input("Enter movies you watched: ").split(","))

movies_2025 = {movie.strip() for movie in movies_2025}
watched = {movie.strip() for movie in watched}

print("Movies released in 2025 that you watched:", movies_2025 & watched)
print("Movies released in 2025 that you have not watched:", movies_2025 - watched)
print("Movies you watched that were not released in 2025:", watched - movies_2025)