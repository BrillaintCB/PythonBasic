class ConvertGbyte:    
    def __init__(self, gb):
        self.gb = gb
    
    def convertToKByte(self, gb):
        return gb*2**10

    def convertToMByte(self, gb):
        return gb*2**20

    def convertToByte(self, gb):
        return gb*2**30

i = 0

while i < 5:
    print("""Please input Gbyte
    """)
    userGbyte = int(input())
    print("""Please input Gbyte 1~3
    1. Byte
    2. MByte
    3. KByte
    """)

    userinput = int(input())
    result = 0

    c1 = ConvertGbyte(userinput)
    if userinput not in range(1,4,1):
        print("Out of range")

    elif userinput == 1:
       result = c1.convertToByte(userinput)
    elif userinput == 2:
       result = c1.convertToMByte(userinput)
    else:
        result = c1.convertToKByte(userinput)
    print(result)
    
    i += 1
    





