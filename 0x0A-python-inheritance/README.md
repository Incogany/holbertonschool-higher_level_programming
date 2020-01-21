# 0x0A. Python - Inheritance

> ## Foundations - Higher-level programming ― Python


### What is a superclass and Subclass
* Super Class: also know like baseclass or parentclass The class whose features are inherited is known as super class(or a base class or a parent class).
*  Sub Class: The class that inherits the other class is known as sub class(or a derived class, extended class, or child class). The subclass can add its own fields and methods in addition to the superclass fields and methods.

##@ How to list all attributes and methods of a class or instance

Try the inspect module. getmembers and the various tests should be helpful.
```
For example,
class MyClass(object):
    a = '12'
    b = '34'
    def myfunc(self):
        return self.a
```
```
>>> import inspect
>>> inspect.getmembers(MyClass, lambda a:not(inspect.isroutine(a)))
[('__class__', type),
 ('__dict__',
  <dictproxy {'__dict__': <attribute '__dict__' of 'MyClass' objects>,
   '__doc__': None,
   '__module__': '__main__',
   '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
   'a': '34',
   'b': '12',
   'myfunc': <function __main__.myfunc>}>),
 ('__doc__', None),
 ('__module__', '__main__'),
 ('__weakref__', <attribute '__weakref__' of 'MyClass' objects>),
 ('a', '34'),
 ('b', '12')]
```
```
>>> attributes = inspect.getmembers(MyClass, lambda a:not(inspect.isroutine(a)))
>>> [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
[('a', '34'), ('b', '12')]
Other option
>>> dir(MyClass)
['__doc__', '__module__', 'a', 'b', 'myfunc']
```

### When can an instance have new attributes
### How to inherit class from another

Of course, a language feature would not be worthy of the name “class” without supporting inheritance. The syntax for a derived class definition looks like this:
```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
### How to define a class with multiple base classes

#### Multiple Inheritance

Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:
```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

### What is the default class every class inherit from
By default, all classes in Python inherit from the Object class. Therefore, the Object class is the superclass to all other classes and it defines methods that all its subclasses share. While the Object class only defines the methods its subclasses share, superclasses can define fields their subclasses share as well.
### How to override a method or attribute inherited from the base class
A subclass can override the methods of its superclass to implement its own behavior if it is necessary. Method overriding allows a subclass to decide how to implement behavior expected by the user through the inheritance contract.
A method of a parent class gets overridden by simply defining in the child class a method with the same name.
### Which attributes or methods are available by heritage to subclasses
A subclass does not inherit the private members of its parent class. However, if the superclass has public or protected methods for accessing its private fields, these can also be used by the subclass.
### What is the purpose of inheritance
The primary purpose of inheritance is to reuse code from an existing class.  Inheritance allows you to create a new class that starts off by including all data and implementation details of the base class.  You can then extend the derived class, to add data or behavior

### What are, when and how to use isinstance, issubclass, type and super built-in functions

#### isinstance()

The __isinstance()__ function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
The syntax of isinstance() is:
```
isinstance(object, classinfo)
```

##### isinstance() Parameters
The isinstance() takes two parameters:
* object - object to be checked
* classinfo - class, type, or tuple of classes and types

##### Return Value from isinstance()
The isinstance() returns:
* True if the object is an instance or subclass of a class, or any element of the tuple
* False otherwise
If classinfo is not a type or tuple of types, a TypeError exception is raised.

#### issubclass()

The __issubclass()__ function checks if the object argument (first argument) is a subclass of classinfo class (second argument).

The syntax of issubclass() is:
```
issubclass(object, classinfo)
```

##### issubclass() Parameters
The issubclass() takes two parameters:
* object - class to be checked
* classinfo - class, type, or tuple of classes and types

Return Value from issubclass()

* True if object is subclass of a class, or any element of the tuple
* False otherwise

#### type()
The __type()__ function either returns the type of the object or returns a new type object based on the arguments passed.
The type() function has two different forms:
```
type(object)
type(name, bases, dict)
```
type() With a Single Object Parameter
If a single object is passed to type(), the function returns its type.

If you need to check the type of an object, it is better to use the Python isinstance() function instead. It's because the isinstance() function also checks if the given object is an instance of the subclass.


#### super()
The __super()__ builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.
In Python, super() has two major use cases:
* Allows us to avoid using the base class name explicitly
* Working with Multiple Inheritance
