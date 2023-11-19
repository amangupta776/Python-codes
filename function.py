def rev(num):
    num2=num
    while(num2>0):
        rem = num2 % 10
        print(rem, end="")

        num2=int(num2/10)

a=int(input())
rev(a)

