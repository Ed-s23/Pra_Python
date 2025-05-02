a=3
# variable with float value.
b=3.17
# variable with complex value.
c=50+7j
#CARACTERES

# Single quotes
str1 = 'Hello World!'
# Double quotes
str2 = "This is a string."
# Triple quotes for multi-line strings
str3 = '''This is a multi-line string.'''

#SECUENCIALES

my_list = [1, 2, 3, 'Hello', 'World']
my_tuple = (4, 5, 6, 'Python')
# Range from 0 to 4
my_range = range(4)
for i in my_range:
    print(i)
# Output: 0, 1, 2, 3

#BINARIOS
my_bytes = b'Hello'
my_bytearray = bytearray(b'Python')

#DICCIONARIOS

my_dict = {
    "name": "Max",
    "age": 25,
    "city": "Berlin"
}

#BOLEANOS
a = True
b = False
result_1 = (a and b) # returns False
result_2 = (a or b) # returns True
result_3 = (not a) # returns False

#CONJUNTOS
my_set = {1, 2, 3, 4, 5}
my_set = {1, 2, 3, 4, 5}
frozen_set = frozenset(my_set)

