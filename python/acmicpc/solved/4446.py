ja = ['a', 'i', 'y', 'e', 'o', 'u']
l_ja = len(ja)
mo = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
l_mo = len(mo)

while True:
    try:
        s = input()
            
        res = ""
        for c in s:
            tmp = c.lower()
            if tmp in ja:
                tmp = ja[(ja.index(tmp)+3)%l_ja]
            elif tmp in mo:
                tmp = mo[(mo.index(tmp)+10)%l_mo]
            if c.isupper():
                tmp = tmp.upper()
            res += tmp
        print(res)
    except:
        break


