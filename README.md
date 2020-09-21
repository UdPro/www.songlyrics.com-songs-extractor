# www.songlyrics.com songs-extractor

Program to download whole artist songs lyrics from songslyrics.com, Very useful program for people working on Musics related project. I have Demonstrated a video below for Metallica band 

## Dependencies

Selenium
```bash
pip install selenium
```
tqdm
```bash
pip install tqdm
```
Download Chrome Driver as per your current Chrome version. Default driver is Chrome version 85l

To download the recent [Chrome driver](https://chromedriver.chromium.org/downloads)
## Features
* Add blacklisted word in your program. To remove the songs lyrics title which have blacklisted words eg live (adding live to wordlist will not add 'Am I Evil (Live at The Kabuki Theatre')
## Usage
Copy your favroute artist page from songslyrics.com and paste on line no. 46 and run the following code to download lyrics
```python
python song_scrap.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)