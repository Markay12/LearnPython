 Learning Python CSE220 Notes

![Python3 Image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fc%2Fc3%2FPython-logo-notext.svg%2F1200px-Python-logo-notext.svg.png&f=1&nofb=1)


# Table of Contents
1. [Python](https://github.com/Markay12/LearnPython/blob/master/lecture_notes.md#python)
2. [History](https://github.com/Markay12/LearnPython/blob/master/lecture_notes.md#history)
3. [Python Structure](https://github.com/Markay12/LearnPython/blob/master/lecture_notes.md#python-structure)
4. [Main?](https://github.com/Markay12/LearnPython/blob/master/lecture_notes.md#building-main)
5. [Print](https://github.com/Markay12/LearnPython/blob/master/lecture_notes.md#print)
6. [Easy Commands](https://github.com/Markay12/LearnPython/blob/master/lecture_notes.md#easy-commands)
7. [Operators](https://github.com/Markay12/LearnPython/blob/master/lecture_notes.md#operators)
8. [Truthiness and Falsiness]()
9. [Conditionals and Loops]()
10. [Missing Operators]()
11. [Functions]()


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


