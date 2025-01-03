def is_prime(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        if func_result <= 1:  # считается составным
            print('Составное')
        else:
            for i in range(2, int(result ** 5) + 1):
                if result % i == 0:
                    print('Составное')
                    break
            else:
                print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(sum_three(2, 3, 6))
print(result)
