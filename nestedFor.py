x = [ ['0,0', '0,1'], ['1,0', '1,1'], ['2,0', '2,1'] ]
for i in range(len(x)):
  for j in range(len(x[i])):
        x[i][j] = i+j

print(i+j)