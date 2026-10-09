# calculations
print(2+2)
print(7-3*2)
print(20/4)
print("17/3 =", 17/3)   # division
print("17//3 =", 17//3) # floor division
print("17%3 =", 17%3)   # modulo
print("2*5 =", 2*5)     # multiplication
print("2**5 =", 2**5)   # exponent

# more calcs
print()
width = 20  # variable
height = 30
print(width * height)
print(width * 2.56)
tax = 12.5/100
price = 100.50
itemTax = price * tax
total = itemTax + price
print(total)
print(round(total, 2))

# strings
print()
print('this string uses single quotes')
print("this one uses double")
print("in 1975: i was born a child! :0")
print('to use a quote in a sentence, we\'d do this')
print("this works \"like this\" too")
print("doesn't need it here")
print('like this "doesn\'t" need it')

# new lines \n \t
print()
print("first line \nsecond line")
print('folder\this\name')
print(r'folder\this\name')  # note the 'r' before the quotes
print("""triple quotes
can span multiple lines
    like this example""")

# concatinations
print()
print(3 * "tung " + "sahur")
print('Py''Thon')
print('this may be useful when typing long '
      'sentences across multiple lines.')
word = "hello"
print(word + ' world')
# print letters: 1st, 4th, 3rd, last, 5th to last
print(word[0], word[4], word[3], word[-1], word[-5])
print(word[0:4])
print(word[3:]) #01234 -> prints 34
print(word[:3]) #01234 -> prints 012

# not allowed
print()
print("strings are immutable:")
# word[1] = 'h'     this would cause an error
newWord = word[:4] + ' world'
print(newWord)
s = 'supercalifragilisticexpialidocious'
print(len(s))   # prints int of length of string

#TODO: LEFT OFF AT 3.1.3. Lists