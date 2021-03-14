# n=int(input("Enter a number "))
# if n%2!=0:
#     print("weird")
# elif n%2==0 and 2<=n and n<=5:
#     print("weird")
# elif n%2==0 and n>20:
#     print("not weird")


n = int(input("Enter a number"))
if n%2 != 0:
    print("Weird")
else :
    if n>=2 and n<=5 or n>20:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    #elif n>20:
        #print("Not Weird")