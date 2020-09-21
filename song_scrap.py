from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from tqdm.auto import tqdm

blacklist_word = []

# path = "C:\chromedriver.exe"
path = 'chromedriver.exe'

def save_to_file(filename, lyrics):

	if os.path.exists('Metallica') == False:
		os.mkdir('Metallica')


	if 'Lyrics' in filename:
		filename = filename.replace('Lyrics', '')
		# removing char which are not allowed in windows rule for renameing
		for not_allowed_char in ['/', '\\', ':','*', '"', '?', '<', '>','|']:
			filename = filename.replace(not_allowed_char, '')
		filename = filename.strip()

	f = open("Metallica/" + filename + ".txt", "w")
	f.write(str(lyrics))
	f.close()


def read_file():
	filename = os.listdir('Metallica')
	songs = {}
	# all songs name with their Lyrics are saved in dict
	for file in filename:
		f = open('Metallica/' + file, 'r')
		songs[file.replace('.txt', '').strip()] = f.read()

# Uncomment if you want to use without opening browser
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(path, options = options)
driver.get("http://www.songlyrics.com/metallica-lyrics/")
# find songs in box css
box_of_song = driver.find_elements(By.CLASS_NAME, 'listbox')
# finding element with song a tag
songs_list = box_of_song[0].find_elements(By.TAG_NAME, 'a')
songs_link = []
print()
for song in tqdm(songs_list, desc = 'Extracting Links'):
	# extracting link value
	songs_link.append(song.get_attribute('href'))
print()
for link in tqdm(songs_link ,desc = 'Downloading Lyrics'):
	# link = 'http://www.songlyrics.com/metallica/the-unforgiven-ii-lyrics/'
	driver.get(link)
	try:
		song_name = WebDriverWait(driver,10).until(lambda d: d.find_elements(By.TAG_NAME, 'h1'))
		# song_name = driver.find_elements(By.TAG_NAME, 'h1')
		song_title = song_name[0].text
		lyrics_songs = driver.find_elements(By.ID, 'songLyricsDiv')
	except:
		driver.quit()
	for lyrics in lyrics_songs:
		save_to_file(song_title,lyrics.text.encode("utf-8"))
driver.quit()



