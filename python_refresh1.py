# age number
age= 33
# name string
name= "grachel"
name1 = """
Mickey
Mouse 
Hello
"""
# multiple lines " per line
print(age)
print(name)

sentence = """
hello  yo ho ho. the quick brown fox jumped over the lazy dog. 
hello there.
"""
print(sentence)

sentence2 = "hey there nice to meet you"
long_string= sentence + sentence2
print(long_string)

#print as is- ('my name is {},'grachel')
new_string = "my name is {}", format(name)
print(new_string)

#print - my name is grachel
new_string2 = "my name is {}". format(name)
print(new_string2)