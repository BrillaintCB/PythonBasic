from urllib.request import urlopen
from  bs4 import BeautifulSoup

html = urlopen('http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num=800513770394')
bsObject = BeautifulSoup(html, "html.parser")

tracking = []
detail = []

for t in bsObject.find_all('div', {'id':'result_waybill2'}):
    #tracking.append(str(t.select('tbody')[1].select('tr')))
    #tracking.append(t.select('tbody')[1].select('tr'))
    #tracking.append(t.select('tbody')[1].select('tr'))
    tracking.append(t.select('tbody')[1].select('td'))


names = []
date = []
time = []
stat = []


#print(tracking)

for index, stat in enumerate(tracking):
    #print(index, str(stat).replace('<td>','').replace('</td>','').splitlines())
    names.append(str(stat).replace('<td>','').replace('</td>','').splitlines())
    
    

#print(str(names[0][0]).split(','))
#for index, content in enumerate(names):
    #date.append(str(str(names[0][0]).split(',')[0]).strip('['))
    #time.append(str(names[0][0]).split(',')[1])
    #stat.append(str(names[0][0]).split(',')[2])
#print(date)



#print("Date" ,str(str(names[0][0]).split(',')[0]).strip('['))
#print("Time" ,str(names[0][0]).split(',')[1])
#print("Name" ,str(names[0][0]).split(',')[2])

#print("Name" ,str(names[0][1]).split(',')[3])


#print(str(names[0]).split('<div align="left">')[0])
#print(str(names[0]).split('<div align="left">')[1])
#print(str(names[0]).split('<div align="left">')[2])
#print(str(names[0]).split('<div align="left">')[3])



print(str(str(str(names[0]).split('<br/>')[0]).split(',')[0]).lstrip("\['["))
print(str(str(str(names[0]).split('<br/>')[0]).split(',')[1]).strip(' '))
print(str(str(str(names[0]).split('<br/>')[0]).split(',')[2]).strip(' '))
print(str(str(str(names[0]).split('<br/>')[0]).split(',')[4]).strip(' ').lstrip("'<div align=\"left\">'"))
    