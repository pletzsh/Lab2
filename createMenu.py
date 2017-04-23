#
def createMenu(optionList):
  tmp = ''; ct = 0
  for option in optionList:
    tmp += str(ct) + '.' + option + '\n'
    ct +=1
  return tmp
