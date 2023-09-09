from collections import deque
import re

def deco(fn):
    def inner():
        print(7)
        z = fn()
        print(8)
        return z
    return inner

@deco
def pr1():
    print(1)

@deco
def pr2():
    print(2)


def read_file():    
    with open('contacts.txt', 'r') as fr:
        voc_contacts = {}
        frc = fr.readlines()
        for dics in frc:
            s = dics.split()
            voc_contacts.update(name=s[0])
            voc_contacts.update(phone=s[1])
            voc1 = voc_contacts.copy()
            list_voc_contacts.append(voc1)


def f2_print(fn):
    def inner(cmnd):
        msg = fn(cmnd)
        print(msg)
        return
    return inner

q = {'hello' : 'f_hello',
            'add' : 'f_add',
            'change' : 'f_change',
            'phone' : 'f_phone',
            'show all' : 'f_show_all',
            'good bye' : 'f_exit',
            'close' : 'f_exit',
            'exit' : 'f_exit'
}

q2 = {'hello' : '2121f_hello',
            'add' : '121f_add',
            'change' : '1212f_change',
            'phone' : '121f_phone',
            'show all' : '121f_show_all',
            'good bye' : '1212f_exit',
            'close' : '1212f_exit',
            'exit' : '1212f_exit'
}

list_voc_contacts = []
w = ['q', 'wer', 'cxvxc', 'qweqw']
n = ['sd2', '345678']
e = deque(w)
read_file()
msg = 'show all'
# f2_print(print(msg))
for z1,z2 in zip(q, q2.items()):
    print(z1 + ' ' + z2[1])
