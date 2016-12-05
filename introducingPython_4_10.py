def test(func):
    def new_func(*args, **kwargs):
        print "start"
        result = func(*args, **kwargs)
        print "end"
    return new_func

@test
def hello(name):
    print "hello", str(name), "!"

hello("Mars")
