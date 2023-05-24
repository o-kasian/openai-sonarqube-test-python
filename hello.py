import sys

def _BadMethod(WrongName):
  WrongName2 = WrongName
  print 'Out: ', WrongName2
  
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
