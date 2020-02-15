from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

#for meta in bsObject.head.find_all('meta'):
#    print(meta.get('content'))

mydic = {}

for link in bsObject.find_all('a'):
    text = link.text.strip() 
#    text = link.text
    link = link.get('href')
    mydic[text] = link
    #print(link.text.strip(), link.get('href'))

#print(mydic.keys())

for i in mydic.keys():
    print(i)
    print(mydic[i])




#https://webnautes.tistory.com/779
