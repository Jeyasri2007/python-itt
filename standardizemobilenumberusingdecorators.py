def wrapper(f):
    def fun(l):
        formatted_list = ["+91 " + n[-10:-5] + " " + n[-5:] for n in l]
        return f(formatted_list)
    return fun

