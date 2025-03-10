import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

list=[1,2,3,4,5,6,7,8]
print(list)
list.append(44)
print(list)
print(list.pop())
print(list)
list.insert(4,70)
print(list)
print(list.remove(5)) # print(list.remove(5)) prints None is that the .remove() method in Python does not return anything. Instead, it modifies the list in place by removing the specified element.
print(list)
print(list.index(4)) # return index value
print(4 in list) # return boolean output
print(44 in list)

print(list.count(44))
print(list.count(3))
list.append(70)
print(list.count(70))

list.sort()
print(list)
list.reverse()
print(list)

list2=list.copy()
list.append(774)
print(list2)

# a program for removing duplicate number from a list
numbers=[2,3,4,5,2,3,4,7,8,6,2,6]
unique=[]
for num in numbers:
   if num not in unique:
      unique.append(num)

print(unique) 