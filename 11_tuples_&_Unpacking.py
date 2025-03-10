import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

numbers=(1,2,3,4,2,5) # cant add or change any number from this.
# has only two methods 
# 1. count()
# 2. index()
print(numbers[0])
print(numbers.count(2))
print(numbers.index(3))

# unpacking

coordinates=(3,5,7)
x,y,z=coordinates
print(x)
print(x*y*z)

lists=[4,7,9,10]
m,n,o,p=lists
print(m*n*o*p)