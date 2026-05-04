import re

text = "Links: https://example.com and http://site.ru/page"
links = re.findall(r"https?://[^\s]+", text)
print(links)
