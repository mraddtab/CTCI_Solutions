def urlify(str, trueLen):
  ret = list(str)
  for i in range(0, trueLen):
    if ret[i] == ' ':
      for j in range(len(str)-1, i,-1):
        ret[j] = ret[j-2]
      ret[i],ret[i+1], ret[i+2] = '%', '2', '0'
  print(ret)

urlify("Mr John Smith    ", 13)
urlify("Hey Man  ", 7)
urlify("         ",3)
urlify("h e  ", 5)
