x = 'Hello'
for ch in x:
    print(ch)

copy = ""
for ch in x:
    copy = copy + ch
    print(copy)

a=x[:3]
print(a)
b=x[2:]
print(b)
c=x[::-1]
print(c)
d=x[::2]
print(d)

# understand that strings can't be change
# but you can copy and slice pieces of it to create a new string.

p=x[0]+'y'+x[2:]
print(p)


r= "drox"+p[1:]
print(r)

# Using replace
# Takes an area of the string and enters a new string

s=x.replace('el', 'orph')
print(s)

t=x.replace('l', 'opo')
print(t)
# Split
# Most useful

u= "Not all dog's go to heaven"
y= u.split()
print(y)
print(y[1])
print(y[2])
print(u.capitalize())

e='Mississippi'
for i,ch in enumerate(e):
    if ch == 'i':
        print(i)
        
    
s= 'radar'
y= s[::-1]
if s==s[::-1]:
    print('is palindrome')
