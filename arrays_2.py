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

#O(n!) Calculate all the permutations of a string, and check if the other string
#is one of them.
def check_permutation_brute (str1, str2):
  if str2 in permutations(str1, 0, len(str1) - 1):
    return True
  else:
    return False


#O(nlog(n)) More intuitive way is to just turn the two strings into a lists, sort them and check if they're equal. list.sort() is nlog(n) 
def check_permutation_sort(str1, str2):
  str1_arr = list(str1)
  str2_arr = list(str2)
  str1_arr.sort()
  str2_arr.sort()
  if str1_arr != str2_arr:
    return False
  return True

print(list("abc").sort())

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
