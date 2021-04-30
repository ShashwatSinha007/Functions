a= input('Please enter a string ')
def most_frequent(str):
    d = dict()
    for b in str:
        if b not in d:
            d[b] = 1
        else:
            d[b] += 1
    return d

print (most_frequent(a))
