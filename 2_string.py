import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

course="Python for Beginner's"
print(type(course))

course2='Python for Beginner'
print(type(course2))

course='Python for "Beginner"'
print(course)

message='''Hello John,
Congratulation's for your success
Best wishe's 
Robert
'''
print(message)

print(message[0])
print(message[-2]) #print (n+1)'th character from the end

print(message[1:])
print(message[4:15])
print(message[9:12])

message2="Game of Thrones"
print(message2[1:-2])
clone_message2=message2[:]
print(clone_message2)