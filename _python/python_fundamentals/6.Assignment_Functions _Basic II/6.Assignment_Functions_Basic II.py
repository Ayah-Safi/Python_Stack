#1Countdown
def countDown(n):
    countDownList = []
    for i in range(n,-1,-1):
        countDownList.append(i)
    return(countDownList)
y = countDown(5)
print(y)

#2Print and Return
def printandReturn(list):
    print(list[0])
    return list[1]
y = printandReturn([1,2])
print(y)

#3First Plus Length
def firstPlusLength (list):
    return list[0]+len(list)
y = firstPlusLength([5,6,7,8,9,10])
print(y)

# 4Values Greater than Second
def valuesGreaterthanSecond(list):
    list1 = []
    list_second_value = list[1]
    for n in range(len(list)):
        if(list[n]> list_second_value):
            list1.append(list[n])
    print(list1)
y = valuesGreaterthanSecond([-5,0,3,2,1,-4])
print(y)

#5This Length, That Value
def thisLengthThatValue(size, value):
    new_list = []
    for i in range(size): 
       new_list.append(value)
    print(new_list)
thisLengthThatValue(5,3)
