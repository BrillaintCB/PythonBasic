from urllib.request import urlopen
from  bs4 import BeautifulSoup

html = urlopen('http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num=800513770394')
bsObject = BeautifulSoup(html, "html.parser")

tracking = []

detail = []
#print(bsObject)

for t in bsObject.find_all('div', {'id':'result_waybill2'}):
    #tracking.append(str(t.select('tbody')[1].select('tr')))
    #tracking.append(t.select('tbody')[1].select('tr'))
    #tracking.append(t.select('tbody')[1].select('tr'))
    tracking.append(t.select('tbody')[1].select('td'))




#print(tracking)






