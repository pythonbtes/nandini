import re
r=re.search("[ab]","this is aba absolute value")
print(r.group())
print(r.start())
print(r.span())
print()