import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# for printing each item 
for item in "python":
    print(item) 

for item in ['sansa','john','arya']:
    print(item)

#using range function
for i in range(10):
    print(i)
#for a specific range
for i in range(5,10):
    print(i)

# range with specific step

for  i in range(1,10,2): #here 1 and 10 is starting and ending point sequentialy also 2 is step size
    print(i)

#nested loop
for x in range(1,10,2):
    for y in range(2,11,2):
        print(f"x: {x}, y: {y}")