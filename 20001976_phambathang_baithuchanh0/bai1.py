def find_saddle_point(matrix):
    for i in range(len(matrix)):
        min_row = matrix[i][0]
        col_ind = 0
        for j in range(1, len(matrix[0])):
            if matrix[i][j] < min_row:
                min_row = matrix[i][j]
                col_ind = j

        for k in range(len(matrix)):
            if min_row < matrix[k][col_ind]:
                break
            elif k == len(matrix) - 1:
                print("Saddle Point at", (i, col_ind), "value:", min_row)
                return
    print("No Saddle Point")


if __name__ == '__main__':
    matrix_a = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]]
    find_saddle_point(matrix_a)
