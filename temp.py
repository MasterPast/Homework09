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


q = {
    '1': 'qwe',
    '2': '23ew',
    '3': 'cxvc'
}

w = ['q', 'wer']
e = deque(w)

# w = ['q', 'wer']
if '2' in q:
    print('Yeah')
e.popleft()
print(e)
print(e[0])
pr1()
pr2()
# deco()
