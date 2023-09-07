from sys import exit
from collections import deque

def f2_input_error(fn):
    def inner(cmnd):
        try:
            print(cmnd)
            fn(cmnd)
        except IndexError:
            print('Give me name and phone please...')
        return 
    return inner

def f2_save_contact(cmnd):
    pass    


@f2_input_error
def f_add(cmnd):
    voc_contacts = {}
    voc_contacts['name'] = cmnd[0]
    voc_contacts['phone'] = cmnd[1]
    list_voc_contacts.append(voc_contacts)
    
@f2_input_error
def f_change(cmnd):
    for voc in filter(lambda voc: voc['name']==cmnd[0], list_voc_contacts):
        print(voc)
    # voc_contacts['name'] = cmnd[0]
    # voc_contacts['phone'] = cmnd[1]
    

def f_exit(cmnd):
    print('Good bye!')
    exit()


def f_hello (cmnd):
    print('How can I help you?')


def f_phone(cmnd):
    print('wtf phone')


def f_show_all(cmnd):
    print(list_voc_contacts)


def f_talking(cmnd):
    cmnd = cmnd.split()
    cmnd = deque(cmnd)
    if cmnd[0] == 'good' or cmnd[0] == 'show':
        cmnd[0] += ' ' + cmnd[1]    
        voc_func = cmnd.popleft()
        cmnd.popleft()
    else:
        voc_func = cmnd.popleft()
    # print(voc_func)
    return voc_cmnd[voc_func], cmnd

def f_unknown(cmnd):
    print('Please, repeat... Don`t understand you.(')


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

list_voc_contacts = []
# voc_contacts = {}
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

def main():
    read_file()
    while True:
        cmnd = []
        
        input_command = input('What can I do for you? >>> ')
        input_command = input_command.lower()
        # print(input_command)
        res, cmnd = f_talking(input_command)
        # print(res)
        res(cmnd)

main()