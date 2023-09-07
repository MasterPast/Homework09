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
            s=dics.split()
            print(s[0])
            voc_contacts['name'] = s[0]
            voc_contacts['phone'] = s[1]
            list_voc_contacts.append(voc_contacts)
        print(list_voc_contacts)
    #Copying the links of content!!!! Correct this!

q = {
    '1': 'qwe',
    '2': '23ew',
    '3': 'cxvc'
}
list_voc_contacts = []
w = ['q', 'wer', 'cxvxc', 'qweqw']
e = deque(w)

# w = ['q', 'wer']
# if '2' in q:
#     print('Yeah')
# e.popleft()
# print(e)
# print(e[0])
# pr1()
# pr2()
# deco()
read_file()

