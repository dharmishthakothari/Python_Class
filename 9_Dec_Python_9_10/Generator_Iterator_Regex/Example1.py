def my_generator():
    for i in range(1,10):

        yield i

gen=my_generator()
print(gen)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

# for i in gen:
#     print(i)
