from urllib.parse import urlsplit
import sys

url = sys.argv[1]
base_url = "{0.netloc}".format(urlsplit(url))
print(base_url)
