# display numbers from a list using loop
# the number must be divisible by 5
# if the number is > 150 then skip it and moove to the next number
# if the number > 500 , stop the loop

num_list = [10,20,30,46,50,60,70,82,90,100,140,180]
for n in num_list:
    if n>500:
        break
    elif n>150:
        continue
    elif n%5==0:
        print(n)
