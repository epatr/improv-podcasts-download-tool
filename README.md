# Improv Podcasts Download Tool

This is a very small Python script to facilitate creating an archive of 
podcast episodes.

### Why create this?

In 2015, Howl.fm was announced, which threatened to hide any episodes older 
than 6 months behind a paywall. 

## Usage

If you create a flatfile text document with a list of podcast URLs, 
this tool will download them to your local machine for permanent safe-keeping. 

Simply put your list of files into `urls.txt` and run 

```sh
python download
```

And sit back as your computer checks if the file exists on your local machine
and downloads it if it doesn't.