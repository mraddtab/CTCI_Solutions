def swap(str, a, b):
  ret = list(str)
  ret[a], ret[b] = ret[b], ret[a]
  return ''.join(ret)

#O(N!) - Returns a list of all permutations of a string
def permutation(str, L):
  ret = []
  if L == len(str) - 1 or len(str) == 1:
    return [str]
  for r in range(L, len(str)):
      swapped = swap(str, L, r)
      ret += permutation(swapped, L+1)
  return ret

#O(N) - Returns a lowwercase copy of the string without nonchars,
def cleanStr(str):
  ret = []
  for i in range(0, len(str)):
    if str[i].isalpha():
      ret += str[i].lower()
  return ''.join(ret)

#O(?) - Checks if a string is the same forwards or backwards,
# bisects a string into left and right, and checks for equality
def isPalindrome(str):
  clean_str = cleanStr(str)
  lst = list(clean_str)
  mid = len(clean_str)//2
  if(len(clean_str) % 2 == 0):
    left = lst[0:mid]
    right = lst[mid: len(clean_str)]
  else:
    left = lst[0:mid]
    right = lst[mid+1:len(clean_str)]
  return left == right[::-1]

#O(NN!) - Check if a string is a permutation of a palindrome, by calculating all permutations and checking if any are palindromes.
def pp(str):
  permutations= permutation(str, 0)
  for i in range (0, len(permutations)):
    if isPalindrome(permutations[i]):
      return True
  return False

print(pp("Tact Coa"))
print(pp("a b a"))
