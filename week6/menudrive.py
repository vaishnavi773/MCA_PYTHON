numbers=list(map(int,input("Enter integers of list seperated by comma : ").split(",")))
print("list of numbers :",numbers)
print("1.find greatest and lowest")
print("2.sort in ascending order")
print("3.create even number list ")
choice=int(input("Enter your choice :"))
if choice==1:
    print("gretesr value in the list :",max(numbers))
    print("lowest value in the list :",min(numbers))
elif choice==2:
    numbers.sort()
    print("List in sorted order:",numbers)
elif choice==3:
    even=[]
    for i in range(0,len(numbers)):
        if numbers[i]%2==0:
            even.append(numbers[i])
    print("even number in list :",even)
else:
    print("invalid choice")
