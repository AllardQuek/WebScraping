from bs4 import BeautifulSoup
from requests import get

# practice scraping the local HTML file alice.html
def main():
    # open alice.html as read-only and read
    f = open('alice.html', 'r')
    s = f.read()

    # use BeautifulSoup to parse the HTML file
    soup = BeautifulSoup(s,'html.parser')

    # print out the HTML page with BeautifulSoup's prettify function

    print(soup.prettify())
    # print(soup.find('a').get('href'))

    # links = soup.find_all('a')    ;returns a list
    # for link in links:
    #     print(link.get('href'))

    # print(soup.find(id='link2'))
    # print(soup.find(id='link2')).attrs    ;returns a dict
    # print(soup.find(id='link2')['href'])

    # print(soup.p.name)
    # print(soup.find('title').text)
    # print(soup.find('title').string)


if __name__ == "__main__":
    main()
