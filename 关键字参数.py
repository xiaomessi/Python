def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
    print(x)
    print(y)
    print(args)

my_func(2, 3, 4, 5, 6, a=7, b=8)
