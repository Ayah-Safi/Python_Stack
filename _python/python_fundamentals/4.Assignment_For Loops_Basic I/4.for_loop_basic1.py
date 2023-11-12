#1
for i in range(0, 151, 1):
    print(i)
#2
for i in range(5,1001,5):
    print(i)
#3
for n in range(1,101,1):
    if(n%5 == 0):
        print("Coding")
        if(n%10 == 0):
          print("Coding Dojo")
    else:
        print(n)  
#4
sum = 0
for i in range(0, 500001, 1):
    if(i%2):
        sum+=i
print(sum)

#5
lowNum = 2
highNum = 9
mult = 3
for n in range(lowNum, highNum+1, 1):
    if(n%mult==0):
        print(n)
        