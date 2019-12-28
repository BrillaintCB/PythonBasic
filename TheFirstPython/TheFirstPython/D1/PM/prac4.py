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
    
print("abc\ta\tabcdefg\tabcdefgh\t")
print(123 + 123)



nums = [12,54,268,42,2,23,120,3]

result = "{0}+{1}={2} 입니다\n{3}-{4}={5} 입니다\n{6}*{7}={8} 입니다\n{9}/{10} = {11} 입니다"

print(result.format(nums[0],nums[1],nums[0]+nums[1],
                    nums[2],nums[3],nums[2]-nums[3],
                    nums[4],nums[5],nums[4]*nums[5],
                    nums[6],nums[7],nums[6]/nums[7]))








