R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  

A = [] 
print("Enter the entries rowwise:") 
  

for i in range(R):          # A for loop for row entries 
    k =[] 
    for j in range(C):      # A for loop for column entries 
         k.append(int(input())) 
    A.append(k) 
  

print("Input matrix is:")
for i in range(R): 
    for j in range(C): 
        print(A[i][j], end = " ") 
    print() 
    
    
def transpose(A, B): 
  
    for i in range(C): 
        for j in range(R): 
            B[i][j] = A[j][i] 
  

  

B = [[0 for x in range(R)] for y in range(C)]  

transpose(A, B) 
  
print("Result matrix is") 
for i in range(C): 
    for j in range(R): 
        print(B[i][j], " ", end='') 
    print()     
