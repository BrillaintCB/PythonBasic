companyname = "파이썬 쇼핑몰"
invoice = 1078718855
address = "서울시 종로구 종로3가"
nameofboss = "김사장"
phone = "070-1234-5678"

fmtop = """
번호 : {0}\n
주소 : {1}\n
성명 : {2}\n
전화 : {3}\n
        """

printtop = companyname.center(50)


printheader = "\t품명\t\t단가\t\t수량"

print(printtop)
print(fmtop.format(invoice, address, nameofboss, phone))
print('-'*50)
print(printheader)
print('-'*50)


item1 = {"itemname" : "블루투스 이어폰", "price":85000, "qty":1, "sum": item1["price"] * item1["qty"]}
item2 = {"itemname" : "USB 3.0 8G", "price":8000, "qty":1, "sum": item2["price"] * item2["qty"]}
#item2 = {"itemname" : "USB 3.0 8G", "price":8000 "qty":1, "sum": item2["price"]* item2["qty"]}

totalprice = item1["price"] + item2["price"]
receivedprice = 100000
changeprice = receivedprice-totalprice


itemprint = """
"\t{0}\t\t{1}\t\t{2}"
"""
print(itemprint.format(item1("itemname"),))


bottmPrint = """ 
                                        청구금액 {0}\n
                                        받은금액 {1}\n
                                        거스름돈 {2}\n
"""
print(bottmPrint.format(totalprice, receivedprice, changeprice))







