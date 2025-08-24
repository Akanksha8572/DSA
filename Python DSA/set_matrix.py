matrix = [[7,9,5,3],[10,20,0,1],[29,0,8,5],[4,14,6,7]]
# Function to set entire row and column to zero if a zero is found in the matrix
# brute force approach
def markinfinity(matrix, row, col):
    r = len(matrix)
    c= len(matrix[0])
    for i in range(0,r):
        if matrix[i][col] != 0:
            matrix[i][col] = float('inf')
    for j in range (0,c):
        if matrix[row][j] != 0:
            matrix[row][j] = float('inf')
def setzeros(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range (0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                markinfinity(matrix,i,j)
        for i in range (0,r):
            for j in range(0,c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
setzeros(matrix)
for row in matrix:
    print(row)
#optimal way
r = len(matrix)
c = len(matrix[0])
rowtracker = [0 for _ in range(r)]
coltracker = [0 for _ in range(c)]
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j] == 0:
            rowtracker[i] = -1
            coltracker[j] = -1
for i in range(0,r):
    for j in range(0,c):
        if rowtracker == -1 or coltracker == -1:
            matrix[i][j] = 0
for row in matrix:
    print(row)
# TC = O(N*M) and SC =O(N+M)s

