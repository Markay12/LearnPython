 Learning Python CSE220 Notes


# Table of Contents
1. [Python](https://github.com/Markay12/LearnPython#python)
2. [History](https://github.com/Markay12/LearnPython#history)
3. [Python Structure](https://github.com/Markay12/LearnPython#python-structure)
4. [Building Main](https://github.com/Markay12/LearnPython#building-main)
5. [Print]https://github.com/Markay12/LearnPython#print)
6. [Variables](https://github.com/Markay12/LearnPython#variables)
7. [Underscore Prefixes](https://github.com/Markay12/LearnPython#underscore-prefixes)
8. [Easy Commands](https://github.com/Markay12/LearnPython#easy-commands)
9. [Operators](https://github.com/Markay12/LearnPython#operators)
10. [Truthiness and Falsiness](https://github.com/Markay12/LearnPython#truthiness-and-falsiness)
11. [Conditionals and Loops](https://github.com/Markay12/LearnPython#conditionals-and-loops)
12. [Missing Operators](https://github.com/Markay12/LearnPython#missing-operators)
13. [Functions](https://github.com/Markay12/LearnPython#functions)
14. [Parameters](https://github.com/Markay12/LearnPython#parameters-and-python)
15. [Assert and Exception Handling](https://github.com/Markay12/LearnPython#assert)
16. [Array Like Structures](https://github.com/Markay12/LearnPython#array-like-structures)
17. [Lists](https://github.com/Markay12/LearnPython/#lists)
18. [Tuples and Strings](https://github.com/Markay12/LearnPython/#tuples-and-strings)


## Python
Taking over the world, rapidly became the number one most popular language analytically
- Python is an extremely versatile language

---

## History
Began development in 1989
- started as a hobby over Christamas vacation
- appeal to UNIX and C programmers


---

## Python Structure
- Python does not follow '{}' code blocking

Python identifies code blocks through common tab structure
* Python is going to force you to be structured
* Even one space off can mess up your program
* Be wary of tool usage
	* Use the tab key
	* Do not mix tabs and space when defining a code block
	* Python uses 4 space as indentation by default

### Syntax Structures
1. One of the really nice things about Python Structure is a more regular syntax
2. The major structures are all very similar, close to the same as english language

---

## Building Main

```python
{
	def main():
		print("Hello World")

	if __name__ = "__main__":
		main()
}
```

* Now we have a main function
* However, we need to be aware of the way that python reads and understands code. Python does not read code like other
interpreters (java). The code is read from top down. Therefore this would happen

```python
{
	def main():
		print("Hello World!")

	print("This is executed first\n")

	if __name__ = "__main__":
		main()
}
```

Output:
This is executed first
Hello World!

---

## Print

`print("Hello","this","is","test")`

Output:
Hello this is test

```python
{
	var1 = 1
	var2 = 2
	var3 = 3
	print(var1, var2, var3)
}
```

Output:
1 2 3

---

## Variables
- There is no command for creating a variable in Python
- Creating variables in Python is done through the assignment operator '='

Identifiers can start with an uppercase/lowercase letters
- cannot start with _

All other identifiers start with a lowercase letter
- Starting an identifier with a single leading underscore means that it is protected
- Using two leading underscores triggers the mangling mechanism and a strongly private modifier 

---

## Underscore Prefixes
It is a python convention to prefix _ or __ varibales to be private/protected
- _ as the first character in a scall is an "implementation of detail"
- This is the python equivalent to *Protected*, which is semantic and offers one language feature


### \'__\' triggers a name mangling mechanism
- protects a name from being accidently overriden

---

## Data Types
Python is Dynamically and Strong typed 
- Often known as duck typing
* Strong typing means that vars act as their type and not in unexpected ways
  * Less or no data coercion
  * Strings don't magically become numbers
  * Required explicit conversions

* Dynamic Typing means that vars are not fixed from one type line to line
  *  Not necissarily contradictory
  * Strong speaks to how the variable is used, not to how it is changed
  * We can change from line to line and how we change it will link it to that data type

Variables will remain strongly typed
`var1 = 1` is an integer
However we can convert this integer to a string
`print(str(var1))`

We can change a variable between different types without classifying the change. Use quotes to change from int to string
```python
{
	var1 = 1
	var1 = "foo"
}
```

- This var just changed from an integer to a String

### Nuances
When declaring vars you want to create with a default value to represent this data type

```python
{
	myNum = 100 #Integer
	myNum = 100.0 #Float
	myNum = "100" #String
	myNum = 0 #Integer
	myNum = 0.0 #Float
}
```
- Decimal will always create a float value

---

##  Easy Commands
To get basic information from the user we use the `input()` command/function
- `input()` is a value returning function so it will be coupled with an assignment statement

Example.
```python
{
	name = input("What is your name? --> ")
}
```

Be Careful!
- Everything that is put through the input command is evaluated as a String so we would need to cast this variable to something else once formatted

Example.
```python
{
	num = input("Choose a number? --> ")
	
}
```

This is something different in Python3. In Python2 this wasn't and issue and python used to make the decision on the type of variable for you


---

## Operators
### _Math Operators_
There are a few differences but mostly the same
1. + ; addition 
2. - ; subtraction
3. * ; Multiplication
4. / ; Floating Point Division
5. // ; **Integer Division**
6. ** ; Exponent


### _Bitwise Operators__
Python allows us to manipulate binary as well and gives standard bitwise operators

Operator     | Description
------------ | -------------
& Binary AND | Performs a bit by bit AND if the bits are 1 in the same spot
| Binary OR | Performs an OR – 1 in either results in a 1 in the result
^ Binary XOR | XOR if there is a 1 in either, but not both there is a 1 in the result
~ Binary Ones Complement | Flip all the bits in the variable
<< Binary Left Shift | The left operands value is moved left by the number of bits specified by the right operand
\>> Binary Right Shift | The left operands value is moved right by the number of bits specified by the right operand

### _Logic Operators_
Logic operators are used by the word.
Rather than using || or && we type the word 'or' and 'and'
* True and False keywords in python are capitalized

Operator | Description | Example
-------- | ----------- | ----------
and      | Logical AND | True and False = False
or       | Logical OR  | True or False = True
not      | Logical NOT | not True = False
is       | Evaluates to True if the two vars point to the same object | obj1 is obj2
is not   | Evaluates to True if the two variables do NOT point at the same object | obj1 is not obj2




## Truthiness and Falsiness

### False Things
Many things can be considered false.
Follow this structure.
* if it is representative of the idea of ZERO... then it is false

### True Things
* Easy to lock down
* if it isn't false, then it is true

* be aware of what things return within our code
	* this is a problem in C/C++ where the '=' operator will return \*this


## Conditionals and Loops

Standard, however some important differences
* if
* Else
* Else If
* While

However it is missing:
* Do While
* For


```python
{
def main():
    print("Hello")


    grade = int(input("Enter your grade: "))

    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D");
    else:
        print("E")


if __name__ == '__main__':
    main()
}
```

### While Loops

While loops are exactly the same as other languages
* while something is true, do the loop body
	* while continues to follow the colon-tab structure

```python
{

count = 0
while count < 10:
	print(count)
	count+=1

}
```

### Break and Continue
* break and continue are part of the python language as well
* However, using them sparingly is advised. They can eaily crutch bad programming practices

As Author Matthew Read noted:

> Bad programmers speak in absolutes. Good programmers use the clearest solution possible (all other things being equal).
> Using break and continue frequently makes code hard to follow. 
> But if replacing them makes the code even harder to follow, then that's a bad change.


## Missing Operators
In Python there are no:
* Switch-Case Statements
	* must use if-elif-else chain

* Post-Test Loop (Do-while)
	* Rewrite loops as pre-test loops
	* Do priming read before the loop and go

* For Loop... kind of
	* For loops are different

These loops don't work like we have seen them before. In languages such as Java we write

```Java

	for (int i=0; i<5; i++){

	}

}
```

However, in python we write them as:

```python
{

	for i in range(5):
		[code]

}
```

## Functions
Coding with functions and coding with methods are two different things

Here are the main differences

_Method_
* Belongs to a class
	* Important distinction
* Methods are generally expressed behaviors of a class/object
	* Semantically tied to the class they are a part of
* Can only be acces via an object
	* Unless they are static

_Function_
* Does NOT belong to a class/object
* Expresses a useful idea or operation
* Generally semantically tied to the program as a whole rather than the behaviors of a piece of it
* Can be called anywhere in the program

This is important for Python because it can act as many of these. Works with methods and functions
* Java is different in this respect and can only create methods
	* C++ and Python can create functions

### Functions in Python
* `__main__` was already our first function
* Here we can now formalize the syntax

```Python
{

	def <function name>(<param list>):
		<body>

}
```

* Like many languages a function must be defined before you use it
	* Unline javascript, functions are not hoisted
	* They are interpreted n place which means if they are not defined by the time the interpreter gets to the call, there will be an error


* Names can be any valid identifier
* The param list is just a series of variable names separated by commas
	* which means that params are untyped until the function call
* The func body is tabbed over and un-tab indicates body is done
	* Further functions within the same will be further tabbed
* Single values can be returned with a return statement
	* Can be multiple return statements but we can only have one final return

```Python
{

	def isEven(value):
		if (value % 2 == 0):
			return True
		else:
			return False

}
```

What if we call a non-numerical value here?
* Wrong variable type so we would have an issue here


## Parameters and Python
Python passes parameters in a similar manner to Java.
Primitive and immutable types are passed by value
Mutable objects are passed by object reference
* AKA 'Passed by Pointer'
* When obj ref is passed that means we can change the object but can't reassign the object reference
	* Pass in an array
		* You can change the contents of that array
		* You cannot have that array store a brand new array


Parameters are like every other variable
* While semantics can be added we can be more explicit with code
	* Example `def isEven(value:int):`

This is not enforced as syntax
Passing a float will not raise an error

```Python
{

	def isEven(value:int):
		assert isinstance(value, int)
		print(value)
		if(value % 2 == 0):
			return True
		else:
			return False

}
```

Python does not allow for overloading
* This means giving the same function multiple definitions based on different parameter lists
* Different languages have different rules for it, but generally all of them require param list changes

_This allows for the ability for Default Parameters_
* these params can also be known as Optional Parameters

When a param is defined we use the '=' operator

```Python
{

	def addNumbers(first, second, third = 0, fourth = 0):
		return first + second + third + fourth
	
	addNumbers(1,2)
	addNumbers(1,2,3)
	addNumbers(1,2,3,4)

}
```
* This is similar to how the `range` function worked earlier and details how we don't have to always use all parameters

### What are the rules here?
Python has a lot of ways to get around its own rules
We can use "Keyword Arguments"
Parameters are filled from left to right- How can we skip to the fourth? 
Default params must go from left to right as well

We can change the order of calling parameters if we know the names

```Python
{

	def printinfo( name, age ):
		print "Name: ", name
		print "Age: ", age
		return

	printinfo( age = 52, name = "Billy")

}
```
### Unknown/Arbitrary/Variable-Length Param
* Sometimes we want to make a function that doesn't know how many params are going to come in?
* We can accomplish this with an ' * ' as a prefix to a parameter name
	* The param will now contain a Tuple that contains those values
* The variable-length param should generally be the last in the parameter list
	* Except when we are using Default parameters and Keyword use only

```Python
{

	def addThemAl(*numbers):
		total = 0

		for value in nums:
			total += value
		return total

	print(addThemAll(1,2,3))
	print(addThemAll(1,2,3,4,5,6,7,8,9))

}
```

### Revisiting Print()
print() is actually more versatile than earlier
* full syntax = `print(*objects, sep= ' ', end='\n', file=sys.stdout, flush=False)`

sep, file and flush can be set via keyword args
* sep; allows us to change the separator between objects, defaults to ' '
* end; allows us to change what is outputted at the end of the print, defaults to a newline char "\n"
* file; allow to change the target of the output
	* must have write(string) method
	* can be used for basic File output
* flush; True or False, specifies if the output is flushed or buffered (False)




## Assert
The assert command is essentially sanity check
 * `assert <condition>`
 * `assert <condition>,<error message>`

Basically a way to force an error in your code if a condition is not met
* This is an ALL STOP and gives an AssertionError

## Exception Handling - Raising an Exception
* Instead of using assert, we can Raise an exception
	* Known as throwing an exception
* isinstance can still be used

```Python
{

	def isEven(value:int):
		if not isinstance(value, int):
			raise TypeError("value expects integer")
		
		print(value)
		if(value % 2 == 0):
			return True
		else:
			return False

}
```

* Python has a large list of built in exceptions
* Very built and largely accessible

## Array Like Structures
Python comes with a handful of data structures built into the language
* Unlike Java and others, these are generally default language feature and require no imports or libraries

**Containers**

## Lists
Refers to a list collection type.
Often called an array because it is similar, however... the list is NOT an array as we might be used to
* It is actually, depending on the interpreter you are using, structurally different
The python list Variable Length Array is similar to Arraylist in Java
* But not in the bad C way
* Allows for an open ended array. No set length value

Java ArrayList is underpinned by an Array, so it isn't a Python list 
* An array is of fixed size with a chunk of memory that stores multiple variables through the same name
	* The index of each variable is achieved via pointer arithmetic
* The ArrayList is a managed array class
	* Each ArrayList is an object


Array | ArrayList/PythonList
------|----------------------
Fixed in Size | Managed Array
Managed by programmer | object will replace underpinning array
Can't shrinkand grow, can only be replaced | Programmer has no say in size after creation
Memory is managed by the programmer | Automatically grows
 | Can waste memory


Why is this so important?
1. Like using ArrayLists in Java there is an inherent give and take to using lists
2. We're going to give up control and possibly effeciency
3. Gain a dynamic feeling data structure that guarantees O(1) runtimes
4. Since we often don’t care about memory efficiency as much in Python – we’re ok with this trade-off


### Creating Lists
To create a list we simply assign a [] to the variable
This [] can contain init values if we like:
* `myList = []`
	* creates an empty list
* `myList = [1,2,3,4]`
	* list containing 1, 2, 3, 4

Construct a list with
```Python
{

	myList = list(< iterable >)

}
```

_Lists are Objects_
* append(x)
	* adds item to end of list
* extend(<iterable>)
	* adds all items from an iterable structure to end of list
* remove(x)
	* find and remove x from list
	* change the size
* pop( [index] )
	* remove last item of the list and return
	* index provided does the same at the index
* reverse()
	* reverse the list without return
* sort()
	* sorts the data if it can be sorted

With these methods lists can be used as a Stack or a Queue
* Append and Pop give it a stack like behavior automatically
* However, you can pop(0) to get a queue like behavior


## Tuples and Strings
Tuples are **immutable** collection.
Once built, they cannot change
* They don’t shrink or grow
* You can’t change the data contained within them
Tuple syntax is pretty much identical to List syntax.
The difference is that tuples use () for declaration syntax.
* myTuple = (1,2,3,4)
* But uses [] for indexing–print(myTuple[1])

Tuples have a key feature - they are HETEROGENEOUS
* We can mix data types within them
* Generally get used to represent "records"
* Can also be used to return multiple values from a function

Strings are what you expect them to be
* Strings are a mutable collection of characters that represent text
* Like Java, they are Objects

### String Operators
* [index] - Gets a specific character
* [start:finish] - Gets a substring
* [start:] - Substring from start to end
* + - concat operator
* * - allows us to 'multiply' a string

```Python
{

	print("Hello"*2)

}
```

### Common Methods
* count(value, start, end)
	* returns number of times a substring appears within string
	* pattern analysis
* find (value, start end)
	* returns the index of a substring found in a string
* swapcase()
	* returns a string with all the ltter cases flipped
* split(sep, maxsplit)
	* returns a list of substrings delimeted by the separator (space by default)
* upper()/lower()/title()
	* changes cases of string
* strip(char)
	* removes a set of characters from the string


## _Credit & License_
