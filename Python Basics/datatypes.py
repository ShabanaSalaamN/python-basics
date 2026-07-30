x = 3+1j
com =1+0j
print(com)
print(x)
print(type(com))
print(type(x))
x= None
print(x)
print(type(x))

#example of creation
s1 = 'hello'
s2 ="world"
s3 = '''this is
 multiline'''
print(s1, s2)
print(s1+s2)
print(s3)

s = 'python'
print('s[0]=', s[0])
print('s[-1]=', s[-1])
print('s[1:4]=',s[1:4])
print('s[:3]=', s[:3])
print('s[::2]', s[::2])


shabana = 'sos|shabana|Data Science And Analytics|JULY2026|Morning|Offline'
print(shabana[4:11]+shabana[12]+shabana[17]+shabana[25]+shabana[39:42]+shabana[45:47]+shabana[48]+shabana[56])

myself = 'hi iam shabana'
print(myself.upper())   #full capital
print(myself.lower())   #full small letter
print(myself.title())   #all first letters capital
print(myself.capitalize())   #only first letter capital
print(myself.swapcase())    #opposite to input
print(len(myself))
print(myself.find('b'))
print(myself.find('z')) 

food ='i love biriyani'
print(food.split())
player ='neymar-is-good'
print(player.split('-'))
print(player.replace('good','goat'))    #replace word

# traslate example
orig = 'aeiou'
tr = str.maketrans('aeiou', '12345')
print('translate:', 'education'.translate(tr))
orig = 'ishoc'
tr = str.maketrans('ishoc','12345')
print('translate:','isolation'.translate(tr))
print ('iam shabana from kasargod age 20 graduate')
print('shabana1\nkasargod2')
print('shabana\tfrom')

a= "abc123"
x= "123"    #string
print(type(x)) 

y=int(x)         #convert the string to integer
print(y)
print(type(y))      #integer

a= 45
b= 15
print(a//b)
print(a%b)
print(a**b)

x= 25
y=15
print(x == y)
print(x != y)
print(x >y)
print(x >= y)
print(x <= y)
print(x < 100)

x=5
x+=2
print(x)

a= 25
b= 25
print(b is a)

x=15
print(x<10 and x>13)
