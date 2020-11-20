def row_weights(array):

    t1 = 0
    t2 = 0
    num = 0

    for n in array:
        if num % 2 == 0:
            t1 += n
            num += 1
        else:
            t2 += n
            num += 1
    result = [t1, t2]

    return result
