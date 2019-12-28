varstr = "Hello Python! Nice to meet ya"
lecturer = "Mr.Kim"
weight = ["Skinny", "Normal", "Chubby","Fat"]

sentence = "{0} is {1}"
print(varstr)
print(sentence.format(lecturer,weight[3].casefold()))

castedint = int(5.5)
castedfloat = float(5.5)

if (castedint is castedfloat):
    print("Same")
else:
    print("Different")
    
print(123+123)
print(123 + 123)