#count the total number of digit in number
#45678 output(5)

num = int(input("Enter your number:"))
count = 0
while num!=0:
    num+num//10
    print(num)
    count = count+1
print(count)
