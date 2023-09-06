from sys import exit

def f_add(contact):
    contact = contact.split()
    print(f'Adding the {contact[0]} phone: {contact[1]}')    


def f_hello ():
    print('How can I help you?')


def f_change():
    print('wtf change')


def f_phone():
    print('wtf phone')


def f_talking(cmnd):
    cmnd = cmnd.split()
    print(cmnd)
    return voc_cmnd[cmnd]


def f_show_all():
    print('wtf show all')


def f_exit():
    print('Good bye!')
    exit()


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

while input_command != 'quit':
    input_command = input('What can I do for you? >>> ')
    input_command = input_command.lower()
    res = f_talking(input_command)
    res()


