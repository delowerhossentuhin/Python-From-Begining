import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

name=["john","sansa","joffery","ned","ramsy","briene"]
print(name)
print(name[1])
print(name[2:5]) # from m'th number to befor n'th nubmer indes value
name[2]="walter"
print(name[:4]) # before nth number index value
print(name[-1]) # nth number from the end
print(name[-3])
name[3]=12
print(name)
name[3]=name[3]+10
print(name)

#finding the largest number from a list

numbers=[2,0,15,8,-1,11,9,6]
max=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>=max:
        max=numbers[i]
print(max)

# finding the minimum number from a list

min=numbers[0]
for i in  range(len(numbers)):
    if numbers[i]<=min:
        min=numbers[i]

print(min)

matrix=[
    [1,2,3],
    [2,9,6],
    [3,6,3]
]
for row in matrix:
    print(row) # for printing each row

for row in matrix:
    for item in row:
        print(item) # for printing each item in matrix

# finding maximum number from 2d matrix
max=matrix[0][0]
for row in matrix:
    for item in row:
        if item > max:
            max=item
print(max)


