#Inserts c at index i and returns a new string

#Determines if two strings are either one removal or one insert away.
def oneInsRemAway(str1, str2):
  shorter = list(min([str1, str2], key = len))
  longer = list(max([str1,str2], key = len))
  for i in range(0, len(shorter) + 1):
    for c in longer:
      shorter.insert(i, c)
      if shorter == longer:
        return True
      del shorter[i]
  return False

def oneAway(str1, str2):
  n_diff = 0 #records # differences in strings 
  if abs(len(str1) - len(str2)) > 1:
    return False
  if str1 == str2:
    return True
  if len(str1) == len(str2):
    for i in range(0, len(str1)):
      if str1[i] != str2[i]:
        n_diff += 1
    if n_diff > 1:
      return False
    else: 
      return True
  else:
    return oneInsRemAway(str1,str2)

# True
print(" ***** True test Cases ******")
print(oneAway("cat", "dat"))
print(oneAway("abc", "abd"))
print(oneAway("abc", "abcd"))
print(oneAway("abcd", "acd"))
print(oneAway("pale", "bale"))
print(oneAway("", "a"))
print(oneAway("", ""))
print("")
#False
print(" ***** False test Cases ******")
print(oneAway("abc", "def"))
print(oneAway("abc", "abcdde"))
print(oneAway("pal", "bale"))
print(oneAway("paler", "railer"))
print(oneAway("tetete", "hehe"))
print(oneAway("", "aa"))
print(oneAway("ccc", "bbb"))
