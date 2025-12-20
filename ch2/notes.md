# Chapter 2 Notes

Goals of OOP are: Correctness, Robustness (your software is capable of handling unexpected inputs), Adaptability (the ability for software to evolve through time), Portability (the ability for software to run with minimal change on different hardware and operating systems), Reusability (the same code should be usable as a component of different systems in various applications.

Principles of OOP:
- Modularity
- Abstraction (ADTs - which specify a public interface, but not implementation)
- Encapsulation (Different components of a software system should not reveal the internal details of their respective implementations.)

Python provides loose support for encapsulation (no private keyword like java or C++), by convention, names of members of a class that start with a single underscore character are assumed to be nonpublic and should not be relied upon.

### Software Development

Involves three major steps, Design, Implementation, Testing and Debugging.

The design step is probably the most important. Here, we divide our program into classes, decide how each class interacts, what data each will store, and what actions each will perform. Some rules of thumb when designing classes:

- Divide the work into different actors, each with a different responsibility. Describe responsibilities using action words.

- Make each class as independent from each other class as possible.

- Define the behaviours for each class carefully and precisely. 

A common tool for the initial high-level design of a project is the use of CRC (Class-Responsibility-Collaborator) cards. Each card represents a component (which will eventually become a class). Name  on the top of the card, responsibilities on the left-hand side, the collaborators (other classes it has to interact with) on the right hand side. 

The design process iterates through an action/actor cycle, first identifying an action (responsibility), then assigning it to an actor (a component) that is best suited. We iterate until all actions are assigned. Using index cards helps keep classes of managable. 

A standard approach to explain and document the design is the use of UML (Unified Modeling Language) diagrams. One type of UML is known as a class diagram. It has three portions, the first giving the name of the class, the second the recommended instance variables, the third the methods. 

### Python Style Guide

- 4 space indentation.
- Classes should have names that serve as a singular noun, should be capitalised. If more than one word, use CamelCase.
- Functions (including methods) should be lowercase, multiple words seperated by underscores, describing the function/method.
- Names that identify an individual object should be a lowercase noun.
- Identifiers that represent a value considered to be constant are all capital, underscores to seperate words.
- Inline comments for quick explanations, multiline block comments for longer comments.

Any comment that appears as the first statement within the body of a module, class, function, method will be considered to be a docstring. By convention, should be delimited with triple quotes.

### Iterators

Recall from Chapter 1 what an iterator is: it provides one key behaviour: it supports a specia method names next that returns the next element of the collection, if any, or raises a StopIteration exception to indicate that there are no further elements. 

Rare to have to implement an iterator class. We can simply use generator syntax. Python also helps by providing an automatic iterator implementation for any class that defines both len and getitem. But we implement an iterator class as an instructive example.

### Inheritance

Arrows in inheritance diagrams correspond to "is a" relationships. A hierarchical design is useful in software development, so that common functionality can be grouped at the most general level, promoting reuse of code. This promotes modularity. The mechanism for this is called inheritence. The existing class is typically described as the base class/parent class/super class, while the newly defined class is known as the subclass or child class.

Two ways in which a subclass can differentiate itself from its superclass. It may specialise an existing behaviour by providing a new implementation that overrides an existing method. A subclass may also extend its superclass by providing brand new methods.

An example of this is Python's Exception Hierarchy - see pg83. 

As a demonstration, we extend the CreditCard class.
 
The PredatoryCreditCard subclass directly accesses the data member self._balance, the underscored name, by convention, suggests that it is a nonpublic member - so is it okay that we access it? Yes - there are two 'levels' of access control in most OOP-supporting languages. Protected variables, which are accessible to subclasses, but not to the general public. Private variables, which are not accessible to either. _balance is protected but not private. Python does not support formal access control, so convention for private variables is a double underscore. 

