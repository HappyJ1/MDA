# Function to perform 3x3 matrix multiplication
def matrix_multiplication(A, B):
    # Initialize the result matrix with zeros
    result = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    
    # Perform multiplication using nested loops
    for i in range(len(A[1])):
        for j in range(len(A)):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Multiply the matrices
result = matrix_multiplication(A, B)

# Print the result
print(result[0])
print(result[1])
print(result[2])