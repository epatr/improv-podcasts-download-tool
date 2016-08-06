import os
import urllib2

print("Opening urls.txt...")
for url in open('urls.txt'): 
	filename = url.split('/')[-1].rstrip()

	if not os.path.exists(filename):
		print("Downloading"), 
		print filename
		outfile = open(filename, "wb")
		outfile.write(urllib2.urlopen(url).read())
		outfile.close
		print("Complete!")
print("All files are complete!")