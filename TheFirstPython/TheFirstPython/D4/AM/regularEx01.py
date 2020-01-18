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
