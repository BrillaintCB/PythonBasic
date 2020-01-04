"""
Mutable vs Immutable objects in Python

Whenever an object is instanitated, it is assigned a unique object id.
The type of the object is defined at the runtime and it can't be changed
afterwards. However. It's state can be changed if it is a mutable object.

To summarise the difference, mutable ojbects can change thier state or contents and immutable
ojbects cna't chang ethier state or content.

"""

#Immutable Objects : int, float, bool, string ,unicode, tuple

# an immutable object can't be changed after it is created.

tuple1 = (0,1,2,3,4)
# tuple1[0] = 2  #cause an error

msg = "Welcome to Python"
# msg[0] = 'e' #cause an error

#Mutable Objects: list ,dict, set

color = ["red", "blue", "green"]
color[0] = "black"

for x in color:
    print(x)

"""
Conclusion

1. Mutable and immutable ojbects are handled 
differently in python. Immutable ojbects are quicker
to access and are expensive to change because
it involves the creation of copy.

2. Use of mutable objects is recommended when
there is a need to change 
the size or content or the object

3 Exception: However, there is an exception in 
immutableity as well. We know that tuple in python
is immutable. But the tuple consists of a sequence of
names with unchangeable bindings to objects

Consider a tuple
tup = ([3,4,5], 'myname')

The tuple consists of a string and a list. Strings
are immutable so we can't change its value. But the
contents of the list can change. The tuple itself isn't
mutable but contain items that are mutable.

"""
