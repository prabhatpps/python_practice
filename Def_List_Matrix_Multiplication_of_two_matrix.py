# Multiplication of two matrix


# taking 2 matrix as input
def matrix(Matrix_name, Matrix_number):
    print("for matrix", Matrix_number)
    rows_i = int(input("Enter the No. of rows : "))
    columns_i = int(input("Enter the No. of columns : "))
    for num_element_of_row in range(rows_i):
        list_1 = []
        for num_element_of_column in range(columns_i):
            element_of_matrix = int(input("enter no. : "))
            list_1.append(element_of_matrix)
        Matrix_name.append(list_1)
    print(("M" + str(Matrix_number)), " = ", Matrix_name)
    for Row_of_matrix in Matrix_name:
        for element_of_row in Row_of_matrix:
            print(element_of_row, end=" ")
        print()


# taking first matrix as input
matrix_number_1 = 1
Matrix_1 = []
matrix(Matrix_1, matrix_number_1)

# taking second matrix as input
matrix_number_2 = 2
Matrix_2 = []
matrix(Matrix_2, matrix_number_2)

if len(Matrix_1[0]) == len(Matrix_2):

    # result null matrix
    rows_in_result = len(Matrix_1)
    columns_in_result = len(Matrix_2[0])
    result = []
    for i in range(rows_in_result):
        L1 = []
        for j in range(columns_in_result):
            a = 0
            L1.append(a)
        result.append(L1)

    # iterate through rows of Matrix_1
    for i in range(len(Matrix_1)):
        # iterate through columns of Matrix_2
        for j in range(len(Matrix_2[0])):
            # iterate through rows of Matrix_2
            for k in range(len(Matrix_2)):
                result[i][j] += Matrix_1[i][k] * Matrix_2[k][j]

    print("Matrix product is given by---")
    for k in result:
        for s in k:
            print(s, end=" ")
        print()

else:
    print("Matrix product is not defined")

