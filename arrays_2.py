#Check_permutations, Check if two strings are a permutation of another
def swap(a,b, str):
  ret = list(str)
  ret[a], ret[b] = ret[b], ret[a]
  return ''.join(ret)
def permutations(str, L, R):
  ret = []
  if len(str) <= 1:
    return [str]
  if L == R:
    return [str]
    
  for i in range(L, R+1):
    swapped = swap(L,i,str)
    ret += permutations(swapped, L + 1, R)
  return ret
  
def check_permutation(str1, str2):
  if str2 in permutations(str1, 0, len(str1) - 1):
    return True
  else:
    return False


test1 = ("", "abc")  #fail
test2 = ("a", "abc") #fail
test3 = ("bbbb", "a") #fail
test4 = ("a", "bbbb") #fail
test5 = ("abc", "cba") #pass
test6 = ("cba", "abc") #pass
test7 = ("abcdefg", "gfedcba") #pass

print(check_permutation("", "abc"))
print(check_permutation("a", "abc"))
print(check_permutation("bbbb", "a"))
print(check_permutation("a", "bbbb"))
print(check_permutation("abc", "cba"))
print(check_permutation("cba", "abc"))
print(check_permutation("abcdefg", "gfedcba"))
