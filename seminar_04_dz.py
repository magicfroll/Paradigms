from math import sqrt

def pearson_correlation(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)

    sum_x_square = sum(map(lambda xi: xi**2, x))
    sum_y_square = sum(map(lambda yi: yi**2, y))

    numerator = n * sum(map(lambda xi, yi: xi * yi, x, y)) - sum_x * sum_y

    denominator = sqrt((n * sum_x_square - sum_x**2) * (n * sum_y_square - sum_y**2))

    if denominator == 0:
        return 0

    return numerator / denominator

# Пример использования
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона:", correlation)