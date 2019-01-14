import time

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

def rle_encoder(txt):

    if not txt:
        return ''
    c = txt[0]
    i = 1
    res = []
    for x in txt[1:]:
        if x == c:
            i += 1
        else:
            res.append((c,i))
            i = 1
            c = x
    res.append((c,i))
    return res

def rle_decoder(inp):
    res = []
    i = 0
    while i<len(inp):
        c = inp[i]
        i += 1
        count = 0
        while i<len(inp) and inp[i].isdigit():
            count = count*10 + int(inp[i])
            i += 1
        res.append(c*count)

    return ''.join(res)

if __name__ == "__main__":
    import sys
    args = sys.argv
    print(args)
    if len(args)==3:
        dat = args[2]
    elif len(args)==2:
        dat = sys.stdin.read()
    else:
        print("Error")
        exit(0)
    if args[1]=='-d':
        print(rle_decoder(dat))
    else:
        print(rle_encoder(dat))
