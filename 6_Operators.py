import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# logical operator [and or]
is_rain=True
is_storm=False
if is_rain and is_storm:
    print("Very Bad day")
elif not is_rain or is_storm:
    print('Bad day')
elif is_rain and not is_storm:
    print("rainy day")

# Comparison Operation [< > >= <=]

temparatue=30
humidity=90

if temparatue<25:
    print('good Day')
elif temparatue >=30 and humidity <=90:
    print("Not a Bad day")
else: 
    print("Bad day")

name =input("enter your name: ")
if len(name)<5:
    print("Name is too short")
elif len(name)>15:
    print("Name is too long")
else: 
    print("Name is good")