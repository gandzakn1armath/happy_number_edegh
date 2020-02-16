while(True):
    a = str(input("input number"))
    if(len(a) > 4 or len(a) < 4):
        print("error") 
    if(str(a)[0] + str(a)[1] == str(a)[2] + str(a)[3]):
        print("Your number is a happy ticket")
    else:
        print("Sorry but your number is not a happy ticket")
    
