# Improv Podcasts Download Tool

This is a very small Python script to facilitate creating an archive of podcast episodes.


### Why create this?

In 2015, Howl.fm was announced, which threatened to hide any Earwolf episodes older than 6 months behind a paywall. As a fan of so many podcasts on the Earwolf network, this was a frightening prospect. How.fm launched exclusively as an iPhone app, so I didn't have a great amount of trust in their ability to host their own archives. It's now been a year and there still isn't a way to listen to Howl Premium exclusives in any other program.

I created this tool because I don't want these shows to disappear forever.  


## Usage

If you create a flatfile text document with a list of podcast URLs, this tool will download them to your local machine for permanent safe-keeping. 

Simply put your list of files into `urls.txt` and run 

```sh
python download
```

And sit back as your computer checks if the file exists on your local machine and downloads it if it doesn't.