

#
# def get_fibonacci_number_from_index(index):
#    if index <= 1:
#        return index
#    else:
#        return(get_fibonacci_number_from_index(index-1) + get_fibonacci_number_from_index(index-2))

#https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
#https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
def get_fibonacci_number_from_order(order):
    if order < 0:
        print("Input must be a positive integer.")
        return
    if order <=1:
        return 0
    else:
        index = order - 1
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for record in bin(index)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if record=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2


