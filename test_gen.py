import random
def generate_random_matrix(n, m, low, high):
    """
    Generates a random n x m matrix with elements in the specified range.

    Args:
        n (int): Number of rows.
        m (int): Number of columns.
        low (int): Lower bound of the element range (inclusive).
        high (int): Upper bound of the element range (inclusive).

    Returns:
        list: A list of lists representing the matrix.
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(low, high))
        matrix.append(row)
    return matrix

def print_matrix(file, matrix):
    """
    Prints the matrix as spaced integers, row by row.

    Args:
        matrix (list): A list of lists representing the matrix.
    """
    for row in matrix:
        file.write(" ".join(str(num) for num in row))
        file.write('\n')

with open("input.txt", "r+") as file:
    existing_content = file.read()
    file.seek(0, 0)
    # Example usage
    n = 12
    m = 10
    matrix = generate_random_matrix(n, m, -10, 10)
    b = generate_random_matrix(1,n,-10,10)
    c = generate_random_matrix(1,m,0,10)
    file.write(str(m) + ' ' + str(n)+ '\n')
    print_matrix(file, b)
    print_matrix(file, c)
    print_matrix(file, matrix)

    file.write('\n')

    file.write(existing_content)
    file.truncate()
