# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
#
# print(list_)

# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#     print(list_[i])

# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
# print(sum_)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}')

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i in dict_:
#     print(i, dict_[i])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        primes.append(num)
    else:
        not_primes.append(num)

print('Primes', primes)
print('Not primes', not_primes)

