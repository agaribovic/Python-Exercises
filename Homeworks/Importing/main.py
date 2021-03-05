import string
from string import Formatter
from string import Template

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)  
print(string.punctuation)

formatter = Formatter()
print(formatter.format('{website}', website='Pirple'))
print(formatter.format('{} {website}', 'Welcome to', website='Pirple'))


print('{} {website}'.format('Welcome to', website='Pirple'))

t = Template('$name is the $title of $company')
s = t.substitute(name='CEO', title='Founder', company='Pirple.')
print(s)