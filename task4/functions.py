def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    try:
        if name in contacts.keys():
            return 'There is already such contact, try command: change'
        else:
            contacts[name] = phone
            return 'Contact added'
    except ValueError:
        return 'Not enough data to add contact! Print add name phone'

def change_contact(args, contacts):
    name, phone = args
    try:
        if name in contacts.keys():
            contacts[name] = phone
            return 'Contact changed'
        else:
            return 'There is no such contact! Try command: add'
    except ValueError:
        return 'Not enough data to change contact! Print: change name phone'

def phone_number(args, contacts):
    name = args
    if name[0] in contacts.keys():
        phone = contacts.get(name[0])
        return f'Phone number of {name} is: {phone}'
    else:
        return 'There is no such contact!'
    
def all_numbers(contacts):
    if len(contacts)>0:
        return contacts
    else:
        return 'There is no any contacts!'
#EOF