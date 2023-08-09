movies = ["ironman", "spiderman", "captain america", "batman", "hulk", "black panther", "avengers"]

for movie in movies:
    if movie == "batman":
        print("no tickets allowed")
        continue
    print("booking tickets for: ", movie)