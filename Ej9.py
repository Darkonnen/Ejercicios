def max_divisor(n):
    maximo_actual = 0
    i = 1
    while i < n:
        if n % i == 0:
            maximo_actual = 1
        i += 1
    return maximo_actual
