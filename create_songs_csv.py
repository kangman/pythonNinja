import csv

with open('songs.csv', 'wb') as csvfile:
    song_writer = csv.writer(csvfile)
    headers = ['Title', 'Artist']
    song_writer.writerow(headers)
    song_writer.writerow(["Blank Space","Taylor Swift"])
    song_writer.writerow(["Young and Beautiful", "Lana Del Ray"])
    song_writer.writerow(["Anaconda", "Nicky Minaj"])
    song_writer.writerow(["0 to 100", "Drake"])
