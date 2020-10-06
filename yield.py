def a():
    sum=0
    for i in range(10):
        sum += i
        yield sum

    # return(sum)

A=a()
A.next()
