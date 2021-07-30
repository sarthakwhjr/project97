name=input("enter your name")
no=int(input("hi! " +name +" enter your no between 1-10"))
count=2

if(count==0):
     print("you are loss")
     
if(no<9):
 print("your guess was too low guess the no higher than",no)
 count-1
if(no>9):
    print("your guess was too high guess the no lower than",no)    
    count-1
if(no==9):
     print("Congratulation You Won!!!")