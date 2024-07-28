def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            print('Составное')
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print('Составное')
                    break
            else:
                print('Простое')

        return result
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_


result = sum_three(0, 9, 5)
print(result)
