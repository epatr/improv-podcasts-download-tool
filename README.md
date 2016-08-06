# ImprovPodcasts.com Download Tool

This tool will allow you to download an entire podcast's archives when given a 
list of URLs. 

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

## Contributors

- Eric Patrick ([epatr](https://github.com/epatr))

It's obviously a very basic tool, and its uses extend far beyond improv podcasts, 
so if you have any ideas or want to work together please email improvpodcasts@gmail.com.