from sys import exit
from collections import deque

def f_add(cmnd):
    if not cmnd:
        print('NO')
    else:
        f2_save_contact()
        print(f'Adding the: {cmnd[0]} phone: {cmnd[1]}')    


def f_change(cmnd):
    print('wtf change')


def f_exit(cmnd):
    print('Good bye!')
    exit()


def f_hello (cmnd):
    print('How can I help you?')


def f_phone(cmnd):
    print('wtf phone')


def f_show_all(cmnd):
    print('wtf show all')


def f_talking(cmnd):
    cmnd = cmnd.split()
    cmnd = deque(cmnd)
    voc_func = cmnd.popleft()
    return voc_cmnd[voc_func], cmnd

def f_unknown(cmnd):
    print('Please, repeat... Don`t understand you.(')


def f2_save_contact():
    pass


voc_contacts = {}
voc_cmnd = {'hello' : f_hello,
            'add' : f_add,
            'change' : f_change,
            'phone' : f_phone,
            'show all' : f_show_all,
            'good bye' : f_exit,
            'close' : f_exit,
            'exit' : f_exit
}

input_command = ''

while True:
    cmnd = []
    input_command = input('What can I do for you? >>> ')
    input_command = input_command.lower()
    
    res, cmnd = f_talking(input_command)
    print(res)
    # try:
    res(cmnd)
    # except KeyError:
    #     res = f_unknown(cmnd)
    #     res()

    # if res in voc_cmnd:
    #     res(cmnd)
    # else:
    #     res = f_unknown(cmnd)
    #     # res()


