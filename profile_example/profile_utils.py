import cProfile


def profile_this(f):
    def profiled_f(*args, **kwargs):
        prof = cProfile.Profile()
        result = prof.runcall(f, *args, **kwargs)
        f_path = f.__name__ + '.profile'
        prof.dump_stats(f_path)
        return result
    return profiled_f
