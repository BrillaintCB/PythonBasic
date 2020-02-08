def sort(array=[12,4,5,6,8,1,15]):
    """Sort the array by using quicksort  """
    less = []
    equal = []
    greater = []

    result = []

    if len(array)>1:
        pivot = array[0]
        for x in array:
            if(x<pivot):
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)               

        result = sort(less)+equal+sort(greater)
        #print("*",result)
        return result

    else:
        return array

print(sort())










test = "a:b:c:d"
array = []


for i in test.split(":"):
    array.append(i+"#")
print(array)



#result.append("#")

#print(result)





Is = [10,20,30]
arr = [40, 50 ,60]

print("Is: ", Is)
print("arr: ", arr)

Str = Is + arr
print(Str)

string = Is * 3
print(string)
