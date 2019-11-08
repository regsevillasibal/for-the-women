# Functions
#    how to create a function
#    to give the function parameters
#    default values for the parameters
#    hot to return information back from a function

#age = 12
#name = "Matt"

def hello():
	print("Hello World")
	print("Hello Isaac")
	print("Hello Primary")
#line must be indented to be part of the function, otherwise it is not part

hello()
hello()
hello()

# print(hello())
#figure out why none

def hello1(name,age):
	print(("Hello {} you are {} years old").format(name,age))

#hello1("Mark",12)

hello1(age=20, name="Mark")
#positional declaration of value


def hello2(name="Isaac", age=0):
	return "Hello {} you are {} years old".format(name, age)

sentence = hello2(name="Oscar")
print(sentence)
