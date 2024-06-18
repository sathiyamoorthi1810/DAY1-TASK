'''Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range 2of5  to , print Not Weird
If n is even and in the inclusive range 6of20  to , print Weird
If  is even and greater than 20, print Not Weird'''

n = int(input("Enter your number:"))
if n%2!=0:
    print("Weird")
elif (n>=2 and n<=5):
     print("Not Weird")
elif (n>=6 and n<=20):
     print("Weird")
else:
    print("Not Weird")
