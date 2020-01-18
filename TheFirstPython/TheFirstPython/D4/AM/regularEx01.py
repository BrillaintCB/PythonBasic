"""
regular Expressions

A regular expression is a special sequence of characters that
helps you match or find other strings or sets of strings, 
using a specialized syntax held in a pattern.
Regular expressions are widely used in UNIX world.

The python module re provides full support for Perl-like regular ex
"""


import re

data = """
PARK 910422-1234567
LEE  010428-1234568
"""


matchObj = re.compile("(\d{6})[-]\d{7}")
print(matchObj.sub("\g<1>-*******", data))



# Charaters class []
# [0-5] = [012345]







#Dot(.)
# a.b         abc, a0b




# *
# ca*t                ct , cat , caaat


#(+)
# ct No              cat caaaat true





# ({a,b})  
#  ca{2}t         cat No             caaat yes

#{m,n}
#ca{2,5}t         cat no , caat      true , caaaaat true


#?         0 or 1
#ab?c          ac yes  abc yes     abbc no


#match
p = re.compile('[a-z]+')

m = p.match("python")
print(m)


m = p.match("3 python")
print(m)
m = p.match("python")
if m:
    print("Match found", m.group())
else:
    print("No match")

#search
print("search"+"*"*50)
m = p.search("python")
print(m)


m = p.search(" 3 python")
print(m)

#findall
print("findall"+"="*50)

result = p.findall("life is too short")
print(result)

for r in result:
    print(r)


print("finditer"+"="*50)
result = p.finditer("life is too short to worry")
print(result)

for r in result:
    print(r)

print("@"*50)
#match
#group()
#start()
#end
#span

p1 = re.compile('[a-z]+')
m = p.match("python")

if m:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("No match")

#When you use one object and it's called often
print("#"*50)
m = p.search(" 3 python")

#else m.re.match('[a-z]+', "python")
#m.re.match('[a-z]+', "python")

if m:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("No match")

#Compie Options
# DOTALL        S
# IGNORECASE    I
# MULTILINE     M
# VERBOSE       X


# DOTALL        S
p3 = re.compile('a.b')
m = p3.match('a\nb')
print(m)

p4 = re.compile('a.b', re.DOTALL)
m = p4.match('a\nb')
print(m)


# IGNORECASE    I
print("#IGNORECASE", "#"*50)
p5 = re.compile('[a-z]')
m = p5.match('python')
print(m)
m = p5.match('Python')
print(m)
m = p5.match('PYTHON')
print(m)

p5 = re.compile('[a-z]', re.I)
m = p5.match('python')
print(m)
m = p5.match('Python')
print(m)
m = p5.match('PYTHON')
print(m)

p5 = re.compile('[a-z]', re.IGNORECASE)
m = p5.match('python')
print(m)
m = p5.match('Python')
print(m)
m = p5.match('PYTHON')
print(m)

#MULTILINE     M           ^: the first string  $: the last string
print("#MULTILINE", "M"*50)


# \d       integer same with [0-9]        \D  not integer[^0-9]
# \s       whitespace (space or tab )  [\t\n\r\f\v]    \S not \s      [^\t\n\r\f\v]
# \w       integer + string  same with[a-zA-Z0-9_]            \W not \w [^a-zA-Z0-9_]
#

p6 = re.compile("^python\s\w+")       
data = """python one
life is too short
python two
you need python
python three
"""

print(p6.findall(data))


p7 = re.compile("^python\s\w+", re.MULTILINE)        # == p7 = re.compile("^python\s\w+", re.M) 

print(p7.findall(data))




# VERBOSE       X
print("#VERBOSE", "X"*50)

charref = re.compile(r'12d12d2d12d12d')


charref = re.compile(r"""
&[#]                   # Start of a numeric entity reference
(
0[0-7]+                #Octal form
:


)
""", re.VERBOSE)

# escape \            ex ) \section     = [\t\n\r\f\v]ection
# \\section

p = re.compile(r'\\section')

print(p.match("section"))
#print(p.match("\section"))
print(p.match("\\section"))
