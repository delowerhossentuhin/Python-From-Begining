import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

firstname="Robert"
Lastname="Moore"
Statement=firstname+" ["+Lastname+"] is a tech expert"
print(Statement)
#but this approach is not ideal
Statement2=f"{firstname} [{Lastname}] is a tech expert"
print(Statement2)

print(Statement.upper())
print(Statement.lower())
print(Statement.title()) #make Capitalize first alphabet of every words
print(Statement.find('e')) # Return index number
print(Statement.find("tech"))
print(Statement.replace('a','an'))
print(Statement.replace('[Moore]',"Moore"))
print("Moore" in Statement)
print('Moore' in Statement)
print('moore' in Statement)

print('mugabe' in Statement.replace("Moore",'mugabe'))
print('MUGABE' in Statement.replace("Moore",'mugabe').upper())

