class OopsException(Exception):
    print Exception

def doSomething(input):
    try:
        result = 100 / input
        print "result = ", result
    # except ZeroDivisionError as err:
        # result = "----- Come from ZeroDivisionError -----"
        # raise OopsException(result)
    except Exception as other:
        other = "------ Come from Exception -------"
        raise OopsException(other)
    else:  # If no exception happens
        print "this is else.............."

doSomething(1)
doSomething(3)
doSomething(5.0)
doSomething(0)
