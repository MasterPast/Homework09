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

list_voc_contacts = []
w = ['q', 'wer', 'cxvxc', 'qweqw']
n = ['sd2', '345678']
e = deque(w)
read_file()
msg = 'show all'
# f2_print(print(msg))
for dics in q:
    pattern = re.compile(dics + ' ')
    txt = 'show all addd master 9879437593'
    s = pattern.match(txt)
    print(s)