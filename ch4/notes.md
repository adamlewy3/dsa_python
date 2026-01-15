# Chapter 4 
## Recursion

Recursion is a technique by which a function makes one or more calls to itself during execution, or by which a data structure relies upon smaller instances of the very same type of structure in its representation. 

Most modern languages support functional recursion using the identical mechanism that is used to support traditional forms of function calls. When one invocation of the function makes a recursive call, that invocation is suspended until the recursive call completes.

A recursive definition typically consists of one or more base cases, and one or more recursive cases- such as the factorial function. 

In Python, each time a function is called, a structure known as an *activation record* or *frame* is created to store information about the progress of the invocation of the function. It includes a namespace for storing the function call's parameters and local variables, and information about which command in the body of the function is currently executing.

When the execution of a function leads to a nested function call, the execution of the former call is suspended and its activation record stores the place in the source code at which the flow of control should continue upon return of the nested call. 

If a recursive function is designed so that each invocation of the body makes at most one new recursive call, this is known as linear recursion. Binary recursion is when each invocation of the much makes two recursive calls, and multiple recursion is when there are more than two recursive calls. 


