import URLify.py
#rotate NxN matrix with 4 byte inputs by 90˚ clockwise

def rotate(matrix,N):
    new_matrix = [[]]
    for i in range(N):
        for j in range(N):
            print(new_matrix[i][j])
            print(matrix[i][j])
            new_matrix[i][j].append(matrix.copy()[N-1-j][i])
            print(new_matrix[i][j])
            print(matrix[i][j])
    return new_matrix

matrix_1 =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

print(rotate(matrix_1,5))
print(URLify('hey',3))
