def fizzbuzz(numero):
    num = numero
    if num % 5 == 0 and num % 3 ==0:
        return 'fizzbuzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0:
        return 'fizz' 
    return num

assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'fizz'
assert fizzbuzz(6) == 'fizz'
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == 'buzz'
assert fizzbuzz(10) == 'buzz'
assert fizzbuzz(15) == 'fizzbuzz'


for numero in range(1,100):
    print(fizzbuzz(numero))