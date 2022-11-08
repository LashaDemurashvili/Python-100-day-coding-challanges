
def fun(a, *args, **kwargs):
    print(a, args, kwargs)

fun(1,2,3,4, x=10, y=15)
# 1 (2, 3, 4) {'x': 10, 'y': 15}
