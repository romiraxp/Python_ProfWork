def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return b ** 2 - 4 * a * c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        result = "корней нет"
    elif discriminant(a, b, c) == 0:
        x = -b / (2 * a)
        result = x
    elif discriminant(a, b, c) > 0:
        x1 = (- b + discriminant(a, b, c) ** 0.5) / (2 * a)
        x2 = (- b - discriminant(a, b, c) ** 0.5) / (2 * a)
        result = str(x1) + " " + str(x2)
    return result

if __name__ == '__main__':
    discriminant(1, 8, 15)
    print(solution(1, 8, 15))
    discriminant(1, -13, 12)
    print(solution(1, -13, 12))
    discriminant(-4, 28, -49)
    print(solution(-4, 28, -49))
    discriminant(1, 1, 1)
    print(solution(1, 1, 1))