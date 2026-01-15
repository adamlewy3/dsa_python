### Chapter 1 Notes.

When we define an instance of an object in python, we are simply giving a name to its assignment in memory. For instance, when I write:

'''
temperature = 98.6
original = temperature
'''

I have assigned the identifier "temperature" to the object (instance of the float type) 98.6, and inthe second line, I have declared an alias "original" for the same object. Both temperature and object point to the same thing in memory. If the object supports behaviours that change its state, changes enacted through one alias will be apparent when using the other alias. 

However, if one of the names is reassigned to a new value using an assignment statement, then it breaks the alias.

'''
temperature = temperature + 5.0
'''

Now, temperature is reassigned 103.6, while original still points to 98.6.

The process of creating a new instance of a class is known as instantiation. In general, we do this by invoking the constructor of the class (but many of pythons classes support a "literal" form for designing new instances.

Another way to indirectly create a new instance of a class is to call a function that creates and returns such an instance. E.g. python has a built-in function 'sorted' that takes a sequence of comparable elements as a parameter and returns a new instance of the list class containing those elements in sorted order. 

Traditional functions are invoked in a syntax such as sorted(data), where data is a parameter sent to the function. We may also defined methods, which are invoked on a specific instance of a class using the . operator. 

There are two types of method. Accessor methods return information about the state of the object, but don't change it. Mutator methods change the state of the object.

A class is immutable if each object of that class has a fixed value upon instantiation and cannot subsequently be changed. For instance, float is immutable, as is bool and tuple. list is mutable. 

A list is a referential structure - it stores a sequence of references to its elements. 

Python provides means for functions to support more than one possible calling signature. Such a function is said to be polymorphic.

'''
def foo(a, b=15, c=27)
'''

The function foo has default values 15, 27 for b,c. For instance foo(8,20) executes with a=8, b=20, c=27. We can not define a function with a signature such as bar(a, b=15, c). If one parameter has a default value then it must be present for all further parameters.

Reading and writing to files is done with the fp class. See 1.6.2 for details.

An exception is thrown by executing the raise statment. Checking the type of a function can be performed at run-time using the builti-in function isinstance(obj, cls). cls can be a tuple, for instance, then isinstance will check whether obj is any one of the types in the tuple. 

##### Iterators and Generators.

There are many type of objects in python that qualify as being iterable. For instance, basic container types: list, tuple, set. But str and dict can also produce an iteration of its keys, and a file can produce an interation of its lines.

An iterator is an object that manages an iteration through a series of values. If the variable, i, identifies an iterator object, then each call to the built-in function next(i), produces a subsequent element from the underlying series, with a StopIteration exception raised to indicate that there are no further elements.

An iterable is an object obj that produces an iterator via the suntax iter(obj).

A convenient way for creating iterators in python is through the use of generators. Similar syntax to a function, but instead of returning values, a yield statement is exercuted to indicate each element of the series. 

'''
def factors(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k
'''

This is an example of a generator rather than a traditional function. It returns a generator object.

We have comprehension syntax in python. As a first example, consider list comprehension

'''
[ expression for value in iterable if condition ]
'''

For instance, 
'''
squares = [k^2 for k in range(1,n+1)]
'''
This will produce a list of square numbers.

'''
factors = [k for k in range(1,n+1) if n % k = 0]
'''
This will produce a list of all factors for a number.

There are similar comprehensions for sets, generators and dictionaries. For instance, when computing the sum of the first n squares, we can use generator syntax, and then we need not store the sums of squares in memory. 

'''
total = sum(k*k for k in range(1,n+1))
'''

### Scopes and Namespaces

Suppose we run x+y in Python. The names x and y must have been associated with objects that serve as values, and a NameError will be raised if there is no such definition. This process of determining a value associated with an identifier is known as name resolution.

When an identifier is assigned to a value, that definition is made with a specific scope. Each distinct scope is represented using an abstraction known as a *namespace*. This manages all identifiers that are currently defined in a given scope.

When an identifier is indicated in a command, Python searches a series of namespaces in the process of name resolution. First, the most locally enclosing scope is search. If not found, the next outer scope is searched and so on. 

Each instance of a class has its own namespace to store its attributes, and each class has a namespace too.

