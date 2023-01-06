def nullifyCols(matrix, zero_cols):
  for row in range(0,len(matrix)):
    for col in range(0, len(matrix[row])):
      if col in zero_cols:
        matrix[row][col] = 0
  return matrix

def zeroMatrix(matrix):
  zeroCols = set()
  zeroRows = set()
  for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
      if matrix[row][col] == 0:
        zeroRows.add(row)
        zeroCols.add(col)
  for row in zeroRows:
    zero_row = [0 for i in range(0,len(matrix))]
    matrix[row] = zero_row
  nullifyCols(matrix, zeroCols)
  return matrix


testMatrix = [[1,2,3,4], [5,6,7,0], [9,10,11,12], [13,14,15,16]]
print(zeroMatrix(testMatrix))
      
