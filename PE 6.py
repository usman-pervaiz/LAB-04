print("Muhammad Usman Pervaiz - 18B-006-CS - SEC-A")
print("LAB NO: 04")

X = [[1,2,3], 
    [4 ,5,6], 
    [7 ,8,9]] 
  
Y = [[9,8,7], 
    [6,5,4], 
    [3,2,1]] 
  
  
result = [[0,0,0], 
        [0,0,0], 
        [0,0,0]] 
  
# iterate through rows 
for i in range(len(X)):    
# iterate through columns 
    for j in range(len(X[0])): 
        result[i][j] = X[i][j] + Y[i][j] 
  
for r in result: 
    print("\n",r)
