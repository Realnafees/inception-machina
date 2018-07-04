
try:
    p = 2345
    b = 43223
    f = open("ab.txt")
    p = b/0


    for line in f:
        print(line , end="")
except FileNotFoundError as e :
    print(e.filename)
#except ZeroDivisionError :
   # print("Divided by zero you moron")



#i = 0/0
#we added it here just for fun
