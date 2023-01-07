#Idea 1: Rotate the string (move first char to end) until both strings are ==
# if no match found then return False, else True.
def isSubstring(s1,s2):
  if s1 in s2 or s2 in s1:
    return True
  else:
    return False
def isRotation1(s1,s2):
  if len(s1) != len(s2):
    return False
  for c in s1:
    first = s1[0]
    s1 = s1[1:len(s1)] + first
    if s1 == s2:
      return True
  return False

#Idea 2: Concatenate s1 to s1 and check if s2 is a substring of s1+s1
def isRotation2(s1,s2):
  if len(s1) != len(s2) or (s1 == "" or s2 == ""):
    return False
  s1s1 = s1 + s1
  return isSubstring(s1s1,s2)


test1a = "waterbottle"
test1b = "erbottlewat"
print(isRotation2(test1a, test1b))
      
