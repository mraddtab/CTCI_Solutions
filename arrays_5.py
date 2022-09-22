#O(N) Given two strings check if they are 0 or 1 edits away from another
# Insert Character (inplace), Remove, Insert
# Algorithim
#1. If the two strings are equal just return True
#2. If the difference in lengths of strings is greater than 1, then more
# than one insert/removal occured return False
#3. If the lengths are the same, check for # of replaced characters, if
# its greater than 1 return True, else return false.
def one_away(str1, str2):
  edit_counter = 0
  if str1 == str2:
    return True
  if abs(len(str1) - len(str2)) > 1:
    return False
  if abs(len(str1) - len(str2)) == 1:
    edit_counter +=1
  if len(str1) == len(str2):
    for i in range(0, len(str1)):
      if str1[i] != str2[i]:
        edit_counter +=1
  return edit_counter <= 1

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
