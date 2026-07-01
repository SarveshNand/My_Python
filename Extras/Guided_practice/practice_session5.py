# Write three functions:
# is_big(num) → returns True if num > 100, else False
# get_parity(num) → returns 'Even' or 'Odd'
# run_program() → contains the while True loop, calls the above two functions, handles the 'quit' logic
# Then call run_program() at the bottom.

def is_big(num:int):
  if num > 100:
    return 'Big number!'
  else:
    return 'Small number!'
  
def get_parity(num:int):
  if num % 2 == 0:
    return 'Even'
  else:
    return 'Odd'
  
def run_program():
  while True:
    number = input('Enter a number: ')
    if number == 'quit':
      break
    print(is_big(int(number)))
    print(get_parity(int(number)))

run_program()