## Anime Recommendation System

First of all I had to scrape data from myanimelist.net. Fot this purpose I used BeautifulSoup and requests library in Python.

After Fetching all the required data from myanimelist.net, I then preprocessed the data and brought it to the required format.

Then using CountVectorizer I made a file of vectors which was too big to upload on github, so I made a compressed pickle and loaded that.

In the end I created a Streamlit App with my data.

## Files:

MyAnimeList_allLinks.csv      --> I scraped links to all the anime pages on myanimelist.net and stored them in this file.

MyAnimeListScraper.py         --> It is the crawler that I created to scrape data.

MyAnimeList_Complete_Dataset  --> It is the dataset in the raw format that I scraped using MyAnimeListScraper.py

app.py                        --> Streamlit App

data.pkl                      --> Contains preprocessed data

vectors.pbz2                  --> Contains vectors created using CountVectorizer in a compressed format
