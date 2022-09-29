def compress(str):
  if str == "":
    return str
  curr = str[0]
  ret = ""
  n = 0
  i = 0
  while(i < len(str)):
    if str[i] == curr: 
      n += 1
    else:
      ret += curr + f'{n}'
      n = 1
      curr = str[i]
    i += 1
  ret += curr + f'{n}'
  if len(str) < len(ret):
    return str
  return ret

print(compress("aabbcc"))
