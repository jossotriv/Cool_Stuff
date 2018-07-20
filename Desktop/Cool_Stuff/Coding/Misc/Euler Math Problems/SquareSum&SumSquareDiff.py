def find_sum_square_difference(n):
    sum_of_squares = n*(n+1)*(2*n+1)/6
    square_of_sum = ((n**4)+(2*n**3)+(n**2))/4
    return abs(square_of_sum - sum_of_squares)
