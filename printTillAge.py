a = int(input("How old are you? "))
if a%2 == 0:
    for i in range(2,a+1):
        if i%2  == 0:
            print(i)
        else:
           pass
if a%2 != 0:
    for i in range(1,a+1,2):
        print (i)
