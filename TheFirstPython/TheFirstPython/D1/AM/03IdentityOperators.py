
"""
    Python Identity Operators
    
"""
if(int(5) is float(5)):
    print("int 5 is equal to float 5")
else:
    print("Not eqaul")


if(int(5) == float(5)):
	print("int 5 is equal to float 5")
else:
    print("Not eqaul")


if(int("5") == 5):
	print("Int(\"5\")==5 is true")
else:
	print("Int(\"5\")==5 is false")

"""
    Python Membership Operators
"""




x = [ "1","3","5","7","9"]

print("membership operator","1" in x) #true 
print("true","2" not in x) #True

y = [1,3,5,7] 
print("true", 3 in y) #true
print("true", 2 in y) #False


names = ["Reece", "Emliy", "Paul"]

print("true", "Paul" in names) #true
print("true", "paul" in names) #true























