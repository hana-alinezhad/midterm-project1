j = "hELLO mY nAME IS hANA"
x = j.swapcase()
print(x)

a = "Hello, Welcome"
x = a.casefold()
print(x)

a ='sun'
x=a.capitalize().center( 14 ,'*')
print(x)

n = "Hello hana!"
m = str.maketrans("h", "s")
print(n.translate(m))


a ='sun is yellow'
x =a .find('sun')
print(x)


b= 'abcd'
y=b .index('d')
print(y)

txt='sun is yellow sun sun'
x=txt.count('sun')
print(x)

txt='New world.'
x=txt.endswith('7')
print(x)

txt='547'
x=txt.endswith('7')
print(x)

b ='I am {age} years old.'
x=b.format(age =19 )
print(x)

t='sunny day '
print(t.isalnum())
print(t.isalpha())
print(t.isdigit())

t='2sunnydays'
print(t.isalnum())

t='sunnydays'
print(t.isalpha())

txt = "sun is yellow"
print(txt.isspace())

p = " "
print(p.isspace())

c = "hananeh alinezhad"
x = c .title()
print(x)

txt = "world"
x = txt.upper()
print(x)

txt='sun is yellow '
print(txt.startswith('sun'))
