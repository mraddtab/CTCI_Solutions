# URLIFY Replace all spaces in a string with %20, in place
# Assume the string has extra spaces at the end that will fit.
# Algorithim - O(nlogn)?
# 1. Iterate over string 0 up til trueLen
# 2. If space detected, shift all characters w/ index greater than it
# by 2
# 3.   Replace i, i +1 , i +2 = %, 2, 0
# 4.   Update i by 2 and trulen by 2 (don't check 2, 0)
# 4. Else check next character
def urlify(str, trueLen):
  ret = list(str)
  i=  0
  while i < trueLen:
    if ret[i] == ' ':
      print(i)
      for j in range(len(str)-1, i,-1):
        ret[j] = ret[j-2]
      ret[i],ret[i+1], ret[i+2] = '%', '2', '0'
      i += 2
      trueLen += 2
    else:
      i +=1
  print(ret)

#Test Cases
urlify("Mr John Smith    ", 13)
urlify("Hey Man  ", 7)
urlify("         ",3)
urlify("h e  ", 3)
