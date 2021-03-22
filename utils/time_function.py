from functools import wraps
import time


def my_timeit(my_func):
    @wraps(my_func)
    def timed(*args, **kw):
        tstart = time.time()
        output = my_func(*args, **kw)
        tend = time.time()

        print('"{}" took {:.3f} ms to execute\n'.format(
            my_func.__name__, (tend - tstart) * 1000))
        return output

    return timed
