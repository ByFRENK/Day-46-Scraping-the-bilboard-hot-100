from bs4 import BeautifulSoup
import requests
CLIENT_ID = "2f51547051f5482d9a57b60237111a57"
CLIENT_SECRET = "91388f2c333f4dc5b3f242ec11e79aca"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
print(song_names)