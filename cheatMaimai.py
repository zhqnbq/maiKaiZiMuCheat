import json
ft=open("2.json","r")
_list=json.load(ft)
__reso=[]
length=int(input())
___reso=[]
for i in _list:
    if len(i) == length:
        __reso.append(i)
while True:
    for i in __reso:
        ___reso.append(i)
    __reso.clear()
    if len(___reso) >=20 :
        print(len(___reso) , 'left')
    else:
        for i in ___reso:
            print(i)
    pos=int(input())
    pos = pos - 1
    _c=input()
    for i in ___reso:
        if i[pos] == _c:
            __reso.append(i)
    ___reso.clear()
