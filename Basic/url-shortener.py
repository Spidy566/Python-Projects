import pyshorteners


def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)


url = input("Enter a url to shorten: ")
print(f"Shortened URL: {shorten_url(url)}")
