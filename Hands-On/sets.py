groceries = {"eggs", "veggies", "milk", "chicken", "bread", "milk"}

playlist = {"album1", "album2", "album3", "album4", "album3"}

marvel_movies = {"ironman","spiderman","hilk","black panther"}

fav_movies = {"super man", "ironman","black panther"}


combined_movies = marvel_movies.union(fav_movies)

common_movies = marvel_movies.intersection(fav_movies)


print(groceries)

print(len(groceries))


print(playlist)

print(len(playlist))

playlist.add("album20")

print(playlist)



print(combined_movies)

print(common_movies)


for movies in marvel_movies:
    print(movies)







###FACT ABOUT LIST. 1) CAN NOT HAVE DUPLICATE VALUES   2.) NO ORDER OF VALUES(Values are random, no fix index number)