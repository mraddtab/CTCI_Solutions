#Determine if a string has all unique characters
# O(N^2) brute force
def isUnique_brute(str):
    for i in range(0, len(str)):
      for j in range(0, len(str)):
        if str[i] == str[j] and i != j:
          return False

    return True


#O(N) USING ASCII 
#ASCII has 128 characters, each ascii character 
#is associated with a unique integer value.

def isUnique(str):
  charTable = []
  for i in range(0, 128):
    charTable.append(False)

  for i in range(0, len(str)):
    ascii_value = ord(str[i])
    if(charTable[ascii_value] == True):
      return False
    charTable[ascii_value] = True
  return True
    

print(isUnique("abcdefa"))
