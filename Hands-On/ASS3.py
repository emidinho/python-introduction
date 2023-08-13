movies = [
  {
    "title": "The Adventures of Cloudwatch",
    "genre": "Action",
    "release_year": 2019,
    "director": "John Smith",
    "rating": 7.8
  },
  {
    "title": "VPC Dreams",
    "genre": "Drama",
    "release_year": 2020,
    "director": "Emily Johnson",
    "rating": 8.5
  },
  {
    "title": "The SSL Chronicles",
    "genre": "Science Fiction",
    "release_year": 2022,
    "director": "Michael Brown",
    "rating": 8.2
  },
  {
    "title": "The Network Monitors",
    "genre": "Thriller",
    "release_year": 2017,
    "director": "Jennifer Lee",
    "rating": 6.9
  },
  {
    "title": "Patchman: The Automation Warrior",
    "genre": "Action",
    "release_year": 2021,
    "director": "William Anderson",
    "rating": 8.1
  },
  {
    "title": "Log Files Mystery",
    "genre": "Mystery",
    "release_year": 2018,
    "director": "Jessica White",
    "rating": 7.5
  },
  {
    "title": "The VPC Peers",
    "genre": "Comedy",
    "release_year": 2023,
    "director": "David Johnson",
    "rating": 7.3
  },
  {
    "title": "Elastic Beanstalk Love",
    "genre": "Romance",
    "release_year": 2016,
    "director": "Amy Smith",
    "rating": 6.8
  },
  {
    "title": "The Disaster Recovery Plan",
    "genre": "Action",
    "release_year": 2020,
    "director": "Michael Brown",
    "rating": 7.9
  },
  {
    "title": "CloudFront and CloudWatch",
    "genre": "Documentary",
    "release_year": 2019,
    "director": "Emily Johnson",
    "rating": 8.0
  }
]

# 1) print movie title , movie release year, movie rating ONLY when movie release year is greather than 2020
# 2) in movie list, print when director name is amy smith

######################
#     number 2       #
######################
for movie in movies:
    if movie["director"] == "Amy Smith":
        print(movie["director"])
        break

print()

for movie in movies:
    if movie["director"] == "Amy Smith":
        print(movie)
        break

print()

######################
#     number 1       #
######################

# using diff method
for movie in movies:
    if movie["release_year"] > 2020:
        print("movie title: ", movie["title"], ",   movie release year: ",movie["release_year"], ",   movie rating: ",movie["rating"])

print()
# using continue

for movie in movies:
    if movie["release_year"] <= 2020:
        continue
    print("movie title: ", movie["title"], ",   movie release year: ",movie["release_year"], ",   movie rating: ",movie["rating"])
