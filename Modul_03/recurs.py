# 2 ** 3
# 2 * 2 ** 2
#     2 * 2 ** 1
#         2 * 2 * 0
#             1

# 8
# 2 * 4
#     2 * 2
#         2 * 1
#             1

def power(x, n):

    if n == 0:
        return 1

    return x * power(x, n - 1)

result = power(2,  3)
print(result)

def func(x, y):
    """
    My function is function.
    :param x: x is a value of .,m.,zcv
    :param y: y is a value of .,m.,zcv
    :type x: int
    :type y: int
    :return: returns sum of it's args
    :rtype: int
    """
    pass
