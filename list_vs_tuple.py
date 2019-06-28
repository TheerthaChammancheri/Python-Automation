import sys
import timeit

print(sys.getsizeof([1,2,3,4,5]))
print(sys.getsizeof((1,2,3,4,5)))

print(timeit.timeit(stmt='[1,2,3,4,5]', number=1000000))
print(timeit.timeit(stmt='(1,2,3,4,5)', number=1000000))

lst = [1,2,3,4,5]
for x in lst:
    print(x)