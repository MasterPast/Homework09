from collections import deque


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


q = {
    'wer': 'qwe',
    'war god': '23ew',
    'sqwer': 'cxvc'
}
list_voc_contacts = []
w = ['q', 'wer', 'cxvxc', 'qweqw']
n = ['sd2', '345678']
e = deque(w)
read_file()
msg = 'dfsfsdf'
# f2_print(print(msg))
if 'war god' in q:
    print('yep')