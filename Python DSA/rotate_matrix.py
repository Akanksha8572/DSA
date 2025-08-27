# Rotate a matrix by 90 degrees in place
# optimal way
# TC = O(n^2), SC = O(1)
matrix = [[7,9,5,3],[10,20,0,1],[29,0,8,5],[4,14,6,7]]
n = len(matrix)
for i in range (0,n-1):
    for j in range (i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for i in range(0,n):
    matrix[i].reverse()
for row in matrix:
    print(row)
    