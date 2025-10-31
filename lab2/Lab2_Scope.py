#!/usr/bin/env python3

# ENSF 692 Spring 2025
# May 8 Lab 2
# Exercise 2


# Trace through the execution of the following program.
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

# POINT 1
# What is the value of foo at this point?
# print("200")
# What is the type of foo at this point?
# # Answer: Int
# What is the value of bar at this point?
# Answer: 100
# What is the type of bar at this point?
# Answer: Int

# 200 = spam
# foo = 150
# egg = 250
# bar = 100
# ham = [1, 2, 3, 100]

spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)

# POINT 2
# What is the value of foo at this point?
# Answer: 150
# What is the value of bar at this point?
# Answer: 100
# What is the value of spam at this point?
# Answer: 200
# What is the value of eggs at this point?
# Answer: 250
# What is the value of ham at this point?
# Answer: [1, 2, 3, 100]
# What is the value of baz at this point?
# Answer: [1, 2, 3]

# spam = [1, 2, 3, 100]
# ham = 100
# bar = 200
# foo = python is very flexible
# eggs = 300
# [1,2,3,200]

eggs = "Python is very flexible!"
spam = ham
ham = bar
bar += bar
foo = eggs
eggs = bar + ham
baz.append(bar)

# POINT 3
# What is the value of foo at this point?
# foo = python is very flexible
# What is the value of bar at this point?
# bar = 200
# What is the value of spam at this point?
# spam = [1, 2, 3, 100]
# What is the value of eggs at this point?
# eggs = 300
# What is the value of ham at this point?
# ham = 100
# What is the value of baz at this point?
# [1,2,3,200]
# Print out the types and final values of each variable.

print(type(foo))
print("python is very flexible")
print(type(bar))
print("200")
print(type(spam))
print("[1, 2, 3, 100]")

print(type(eggs))
print("python is very flexible")
print(type(ham))
print("100")
print(type(baz))
print("[1,2,3,200]")
