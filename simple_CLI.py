choice_of_operator= input('''
please select the type of operation you will like to perform
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus
''')

num_1 = float(input('Enter your first number: '))
num_2 = float(input('Enter your second number: '))

if choice_of_operator == '+':
  print(f'{num_1} + {num_2} = ')
  print(num_1 + num_2)

elif choice_of_operator == '-':
  print(f'{num_1} - {num_2} = ')
  print(num_1 - num_2)

elif choice_of_operator == '*':
  print(f'{num_1} * {num_2} = ')
  print(num_1 * num_2)

elif choice_of_operator == '/':
  print(f'{num_1} / {num_2} = ')
  print(num_1 / num_2)

elif choice_of_operator == '%':
  print(f'{num_1} % {num_2} = ')
  print(num_1 % num_2)

else:
  print('Please enter a valid operator')