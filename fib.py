def Fibonacci():
    n = int(input("Enter a Positive Integer:"))
    firstnum = 0
    secondnum = 1
    if n<=0:
        print("The Output of your input is", firstnum)
    else:
        # print(firstnum,secondnum)
        for x in range(2,n):
            thirdnum=firstnum+secondnum
            print(thirdnum)
            firstnum=secondnum
            secondnum=thirdnum
Fibonacci()