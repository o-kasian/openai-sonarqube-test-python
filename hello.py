import sys

def bad_method(wrong_name):
  correct_name = wrong_name
  print('Out: ', correct_name)

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))