"""
    Scrape a website for words, writing each one to a file
"""

from bs4 import BeautifulSoup
from requests import get

# print(sauce), print(sauce.content), print(soup.prettify())
sauce = get("https://www.vocabulary.com/lists/52473")
soup = BeautifulSoup(sauce.content, "html.parser")

# to find by class need '_'
words_tags = soup.find_all('li', class_="entry learnable")

# '+' means new file will be created if it does not exist in library
with open('wordlist.txt', 'w+') as f:
    for word in words_tags:
        # type is important; can only write strings, not list or ints
        write_data = f.write(word['word'] + '\n')
