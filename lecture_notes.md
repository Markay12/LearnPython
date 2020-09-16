# Learning Python CSE220 Notes

# Table of Contents
1. [Python]()
2. [History]()
3. [7 Steps to Learning New Languages]()
4. [Main?]()
5. [Print]()
6. [Easy Commands]()


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

1. Use the tab key
2. Do not mix tabs and space when defining a code block
3. Python uses 4 space as indentation by default

### Syntax Structures
1. One of the really nice things about Python Structure is a more regular syntax
2. The major structures are all very similar, close to the same as english language

---

## Building Main

`
{
	def main():
		print("Hello World")

	if __name__ = "__main__":
		main()
}
`

* Now we have a main function
* However, we need to be aware of the way that python reads and understands code. Python does not read code like other
interpreters (java). The code is read from top down. Therefore this would happen

`
{
	def main():
		print("Hello World!")

	print("This is executed first\n")

	if __name__ = "__main__":
		main()
}
`

Output:
This is executed first
Hello World!

---

## Print

`print("Hello","this","is","test")`

Output:
Hello this is test

`
{
	var1 = 1
	var2 = 2
	var3 = 3
	print(var1, var2, var3)
}
`

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


### __ triggers a name mangling mechanism
- pretects a name from being accidently overriden

---

## Data Types
Python is Dynamically and Strong typed 
- Often known as duck typing
- Strong typing means that vars act as their type and not in unexpected ways
1. Less or no data coercion
2. Strings don't magically become numbers
3. Required explicit conversions

- Dynamic Typing means that vars are not fixed from one type line to line
1.  Not necissarily contradictory
2. Strong speaks to how the variable is used, not to how it is changed
3. We can change from line to line and how we change it will link it to that data type

Variables will remain strongly typed
`var1 = 1` is an integer
However we can convert this integer to a string
`print(str(var1))`

We can change a variable between different types without classifying the change. Use quotes to change from int to string
```
{
	var1 = 1
	var1 = "foo"
}
```

- This var just changed from an integer to a String

### Nuances
When declaring vars you want to create with a default value to represent this data type

```
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
```
{
	name = input("What is your name? --> ")
}
```

Be Careful!
- Everything that is put through the input command is evaluated as a String so we would need to cast this variable to something else once formatted

Example.
```
{
	num = input("Choose a number? --> ")
	
}
```

This is something different in Python3. In Python2 this wasn't and issue and python used to make the decision on the type of variable for you


---

## Operators


