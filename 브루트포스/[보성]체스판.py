list1=[]
list2=[1000000000000000]
matrix1=[['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
matrix2=[['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]

col, row= map(int, input().split())

for a in range(0,col):
   list1.append(list(input()))

for x in range(0,col-7):   
   for y in range(0,row-7):
      countW=0
      countB=0
      for i in range(x,x+8):
         for j in range(y,y+8): 
            if list1[i][j]!=matrix1[i-x][j-y]:
               countW+=1
            if list1[i][j]!=matrix2[i-x][j-y]:
               countB+=1
      list2.append(min(countW, countB))
 
print(min(list2))
