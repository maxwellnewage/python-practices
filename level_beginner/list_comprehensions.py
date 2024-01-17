"""
List Comprehension examples
"""

# dictionary comprehension
sentence = "Hello World"  # input("Words:")

result = {word: len(word) for word in sentence.split()}

print(result)

# list comprehension
list_quad_nums = [num ** 2 for num in range(10)]
print(list_quad_nums)

list_odd_nums = [num for num in range(10) if num % 2 == 0]
print(list_odd_nums)
