# Learning Python CSE220 Notes

# Table of Contents
1. [Python]()
2. [History]()
3. [7 Steps to Learning New Languages]()
4. [Main?]()
5. [Print]()


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

`	def main():
		print("Hello World")

	if __name__ = "__main__":
		main()

`

* Now we have a main function
* However, we need to be aware of the way that python reads and understands code. Python does not read code like other
interpreters (java). The code is read from top down. Therefore this would happen

`	def main():
		print("Hello World!")

	print("This is executed first\n")

	if __name__ = "__main__":
		main()

`

Output:
This is executed first
Hello World!

---

## Print

`print("Hello","this","is","test")`

Output:
Hello this is test

`var1 = 1
 var2 = 2
 var3 = 3
 print(var1, var2, var3)
`

Output:
1 2 3

---

## Variables
- There is no command for creating a variable in Python
- Creating variables in Python is done through the assignment operator '='

Identifiers can start with an uppercase/lowercase letters
- cannot start with '_'

All other identifiers start with a lowercase letter
- Starting an identifier with a single leading underscore means that it is protected
- Using two leading underscores 


