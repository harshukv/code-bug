class_list = dict()
while (1):
    a= int(input("enter 0 if you want to add or 1 if you want to search or 2 if you want to delete or 3 if you want to update"))
    if a==0:
        key = input ("Enter your name")
        value = input ("Enter your grade")
        class_list[key] = [value]
    elif a==1:
        key = input("Enter your name")
        print(class_list[key])
    elif a==2:
        key = input("Enter your name")
        del class_list[key]
    elif a==3:
        key = input("Enter your name")
        b=int(input("enter 0 if you want to update the name or 1 if you want to update the grades"))
        if b==0:
            key1=input("enter you new name")
            class_list[key1]=class_list[key]            
        elif b==1:
            key = input("Enter your name")
            value1=input("enter the new grade")
            class_list[key]=value1
        else:
            print("enter valid input")
    else:
        print("invalid input")
    