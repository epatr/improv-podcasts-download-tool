# Improv Podcasts Download Tool

This tool will allow you to download an entire podcast's archives when given a 
list of URLs. 

In 2015, Earwolf announced an app called Howl.fm, which was an iPhone-only app 
that was promised to be the future of Earwolf podcasts. It would cost $5/month 
and was the best way to support Earwolf. They offered no Android version nor
support for RSS feeds, so you _had_ to use their iPhone app.

Along with the launch of the app was a huge surprise: all Earwolf episodes
older than 6 months would be removed from Soundcloud and become exclusive to 
Howl.fm.

This was obviously horrifying to me, as I'd gotten so many friends into improv
comedy by showing them old improv4humans episodes. I created this very simple
script to download all the old episodes and keep them safe from Earwolf's
(and now E.W. Scripps') mettling hands. 

## How to Use

1. Clone this repo, or simply download `download.py` from the repository above.
2. Create a file called `urls.txt`. On each line, put the direct download URL 
for the episode. Use the podcast's RSS feed to get the direct URLs. 
3. Run the following command in your terminal:

```sh
python download.py
```

Note: If a file already exists, this will skip over it. Delete the file if you 
find it's corrupted or the transfer failed. 