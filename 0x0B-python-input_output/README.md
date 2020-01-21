# 0x0B. Python - Input/Output
> ## Foundations - Higher-level programming ― Python

![Alt](https://qph.fs.quoracdn.net/main-qimg-c47ec0f011ff0bbc9e7ee7d20c4ae107)

### General
#### How to open a file
__open()__ returns a file object, and is most commonly used with two arguments: open(filename, mode).
```
>>> f = open('workfile', 'w')
```
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be __'r'__ when the file will only be read, __'w'__ for only writing (an existing file with the same name will be erased), and __'a'__ opens the file for appending; any data written to the file is automatically added to the end. __'r+'__ opens the file for both reading and writing. The mode argument is optional; __'r'__ will be assumed if it’s omitted. __'w+'__ write and create the file.

####   How to write text in a file
```f.write(string)``` writes the contents of string to the file, returning the number of characters written.
```
>>>
>>> f.write('This is a test\n')
15
To write something other than a string, it needs to be converted to a string first:
>>>
>>> value = ('the answer', 42)
>>> s = str(value)
>>> f.write(s)
18
```

#### How to read the full content of a file

To read a file’s contents, call ```f.read(size)```, which reads some quantity of data and returns it as a string or bytes object. size is an optional numeric argument. 
```
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

#### How to read a file line by line
__f.readline()__ reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline
```
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

#### How to move the cursor in a file

To change the file object’s position, use ```f.seek(offset, from_what)```. The position is computed from adding offset to a reference point; the reference point is selected by the from_what argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
```
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)     # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2) # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

#### How to make sure a file is closed after using it
When you’re done with a file, call ```f.close()``` or ```f.close() ``` to close it and free up any system resources taken up by the open file. After calling f.close(), attempts to use the file object will automatically fail.

#### What is and how to use the with statement

* __with statement in Python__

with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Observe the following code example on how the use of with statement makes code cleaner.
```
\# file handling

\# 1) without using with statement__
file = open('file_path', 'w') 
file.write('hello world !') 
file.close() 

\# 2) without using with statement__ 
file = open('file_path', 'w') 
try: 
     file.write('hello world') 
finally: 
	 file.close()
\# using with statement__ 
with open('file_path', 'w') as file: 
     file.write('hello world !') 

```
#### What is JSON what is serialization and What is deserialization

__JSON__ JAVASCRIPT OBJECT NOTATION is a format that encodes objects in a string. __Serialization__ means to convert an object into that string, and __deserialization__ is its inverse operation (convert string -> object).

When transmitting data or storing them in a file, the data are required to be byte strings, but complex objects are seldom in this format. Serialization can convert these complex objects into byte strings for such use. After the byte strings are transmitted, the receiver will have to recover the original object from the byte string. This is known as deserialization.

Say, you have an object:
```
{foo: [1, 4, 7, 10], bar: "baz"}
serializing into JSON will convert it into a string:
'{"foo":[1,4,7,10],"bar":"baz"}'
```

which can be stored or sent through wire to anywhere. The receiver can then deserialize this string to get back the original object. ```{foo: [1, 4, 7, 10], bar: "baz"}.```

#### How to convert a Python data structure to a JSON string

If you have an object x, you can view its JSON string representation with a simple line of code:
```
>>>
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
```
Another variant of the __dumps()__ function, called __dump()__, simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:
```
json.dump(x, f)
```

#### How to convert a JSON string to a Python data structure

To decode the object again, if f is a text file object which has been opened for reading:
```
x = json.load(f)
```
