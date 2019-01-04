import os.path
import urllib.request

links = open("urls.txt", "r")
path = "E:/Downloads/tmp/"
for link in links:
    link = link.strip()
    name = link.rsplit("/", 1)[-1]
    filename = os.path.join(path, name)

    if not os.path.isfile(filename):
        print("Downloading " + name)
        try:
            urllib.request.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print(" Error unknown. Continuing.")
print("Complete. Files are available in " + path)