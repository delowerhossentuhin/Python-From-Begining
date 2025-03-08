#import sys
#sys.stdin=open('input.txt','r')
#sys.stdout=open('output.txt','w')
i=1
while i<=5:
    print(i,end=" ")
    i+=1
print("\nDone")

i=1
while i<=10:
    print('*'*i)
    i+=1

# make a gussing game
# In Python, the while loop can have an else statement
# secret=9
# count=0
# while count<3:
#     guess=int(input("Enter a number that you guess: "))
#     if guess==secret:
#         print("You Won!!!!!")
#         break
#     count+=1
# else: 
#     print("You Failed")

# building car game
message='''Welcome to this car game
      use command 'start' for starting car
      use command 'stop' for make the car stop
      use command 'quit' for exit 
      use command 'help' for see the command
'''
rules='''If car is already started and you trying to start again Then You will loose 1 point
          If car is alreaey stopped and you trying stop again then You will loose 1 point
          For every correct command you will gain 3 points
          For every wrong commad you will loose 2 points'''
print(message)
print(rules)
print("Car is now stopped")
command=""
is_start=False
point=0
while command!="quit":
    command=input(">").lower()
    if command=="start" and is_start==False:
        is_start=True
        print("Car is started...")
        point+=3
    elif command=='start' and is_start:
        print("Car is Already Started")
        point-=1
    elif command=="stop" and not is_start:
        print("At first start the car")
        point-=1
    elif command=="stop":
        is_start=False
        print("Car is stopped...")
        point+=3
    elif command=='help':
        print(message)
    elif command=='rules':
        print(rules)
    elif command == 'quit':
        temp=input("Are you sure for leaving this game (Yes/No): ").lower()
        if temp=="yes":
            print(f"Thanks for attending this game. Your total Point is: {point}")
        else:
            command=""
    else:
        print("Command is not correct. Try Again")
        point-=2