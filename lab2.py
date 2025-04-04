#Дано натуральное число n. Выведите все числа от 1 до n.

def recursion(number,k=1):
    if k <= n:
        print(k)
        recursion(n,k+1)
n = int(input())
recursion(n)


#Даны два целых числа. Выведите числа от A до B, в порядке возрастания(A < B), или в порядке убывания(A > B).
def rec(a,b):
    if a < b:
        print(a)
        if a!=b:
            rec(a+1,b)
    elif a > b:
        print(a)
        if a!=b:
            rec(a-1,b)
    else:
        print(a)

a = int(input())
b = int(input())
rec(a,b)


#Вычислите сумму цифр N. При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).
def summ_of_digital(n):
    if n == 0:
        return 0
    else:
        return (n%10) + summ_of_digital(n//10)

n = int(input())
result = summ_of_digital(n)
print(result)


#Дано натуральное число n>1. Выведите все простые делители этого числа в порядке возрастания.
import math
def print_prime_factors(n, i=2):
    # Базовое условие: если i больше sqrt(n), и n больше 1, выводим n
    if i > math.isqrt(n):
        if n > 1:
            print(n)
        return
    # Если i - делитель числа n, выводим i и рекурсивно вызываем для n // i
    if n % i == 0:
        print(i)
        print_prime_factors(n // i, i)
    else:
        # Иначе проверяем следующий возможный делитель
        print_prime_factors(n, i + 1)

n = int(input())
print_prime_factors(n)
