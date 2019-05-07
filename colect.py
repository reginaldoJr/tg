import csv
from itertools import islice
from imdb import IMDb,IMDbError

# create an instance of the IMDb class
ia = IMDb()

# get a movie
#movie = ia.search_movie('matrix')
#movie = ia.get_movie(movie[0].movieID)
#print(movie['synopsis'])



import csv
data = []
with open('./dt_small/movies.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
    	print(f"{row['movieId']} : {row['title']}")
    	try:
	    	movie = ia.search_movie(row["title"])
	    	mvId = movie[0].movieID
	    	movie = ia.get_movie(mvId)
	    	synopsis = movie['synopsis'][0]
	    	data.append((row['movieID'],synopsis))
    	except Exception as e:
    		print("Error:",e)

with open('teste.csv', mode='w') as csv_file:
    fieldnames = ['movieID', 'synopsis']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for (movieID,synopsis) in data:
	    writer.writerow({'movieID':movieID,'synopsis':synopsis})
