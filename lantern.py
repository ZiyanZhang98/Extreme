def is_composite(n):
    if n <= 1:
        return False
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i = i + 6
    return False


def is_comp_div(n):
    comp = []
    for i in range(2, n+1):
        if n%i == 0:
            if is_composite(i) is True:
                comp.append(i)
    return comp


return_list = is_comp_div(5)
print(return_list)