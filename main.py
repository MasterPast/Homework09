from sys import exit
from collections import deque

def f2_input_error(fn):
    def inner(cmnd):
        try:
            # print(cmnd)
            msg = fn(cmnd)
            # print(msg)
        except KeyError:
            msg = 'WTF'
        except IndexError:
            print('Give me name and phone please...')
        except UnboundLocalError:
            print('Give me name and phone please...')
        return msg
    return inner


def f2_save_contact(cmnd):
    pass    


def f2_print(fn):
    def inner(cmnd):
        msg = fn(cmnd)
        print(msg)
        return
    return inner


@f2_print
@f2_input_error
def f_add(cmnd):
    voc_contacts = {}
    voc_contacts['name'] = cmnd[0]
    voc_contacts['phone'] = cmnd[1]
    list_voc_contacts.append(voc_contacts)
    msg = f'\nIt was added: {voc_contacts["name"]} with phone number: {voc_contacts["phone"]} in your contacts.\n'
    return msg

@f2_print
@f2_input_error
def f_change(cmnd):
    for voc in filter(lambda voc: voc['name']==cmnd[0], list_voc_contacts):
        voc.update([('phone', cmnd[1])])
        msg = f'\nIt was changed the phone number of: {voc["name"]} on: {voc["phone"]}.\n'
    return msg


def f_exit(cmnd):
    msg = '\nGood bye!'
    f2_print(print(msg))
    exit()


@f2_print
def f_hello (cmnd):
    msg = '\nHow can I help you?\n'
    return msg


@f2_print
def f_phone(cmnd):
    for voc in filter(lambda voc: voc['name']==cmnd[0], list_voc_contacts):
        msg = f'\nFor contact: {voc.get("name")} I found this phone number: {voc["phone"]}.\n'
    return msg


@f2_print
def f_show_all(cmnd):
    msg = '\nI found next information in your contacts: \n'
    msg += (('-' * 46) + '\n')
    for contacts in list_voc_contacts:
        cont_string = '| {a1:{align}{width}} | {a2:{width}}|\n'.format(
                            a1=contacts['name'], a2=contacts['phone'], align='>', width=20)
        msg += cont_string
    msg += (('-' * 46) + '\n')
    return msg


@f2_print
@f2_input_error
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


@f2_print
def f_unknown(cmnd):
    msg = '\nPlease, repeat... Don`t understand you.('
    return msg

def read_file():
    with open('contacts.txt', 'r') as fr:
        voc_contacts = {}
        frc = fr.readlines()
        for dics in frc:
            s=dics.split()
            voc_contacts.update(name = s[0])
            voc_contacts.update(phone = s[1])
            voc1 = voc_contacts.copy()
            list_voc_contacts.append(voc1)
        # print(list_voc_contacts)


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
        input_command = input('\nWhat can I do for you? >>> ')
        input_command = input_command.lower()
        # print(input_command)
        res, cmnd = f_talking(input_command)
        # print(res)
        res(cmnd)

main()