import contacts

def exit_loop():
 global choice
 choice = '0'

def list_all_pprint():
 "Showing all contacts"
 contacts.Person.getContactsPPrint()

def list_all_json():
 "Showing all contacts"
 contacts.Person.getContactsJSON()

def add_person():
 name = ''
 num = ''
 count = 0
 while (name == '' or num == ''):
  name=input('Name: ')
  num=input('Number: ')
  if (name == '' or num == ''): print('Try again')
 person = contacts.Person(name, num)
 person.addPerson()

def list_options():
 print('[1] List all contacts\n'
  '[2] List all contacts (JSON)\n'
  '[3] Add a contact\n'
  '[4] Search\n'
  '[0] Quit')

def search():
 contacts.Person.search(input('Name to search: '))

options = {
 '0' : exit_loop,
 '1' : list_all_pprint,
 '2' : list_all_json,
 '3' : add_person,
 '4' : search,
 '9' : list_options
}

choice=''

while (choice!='0'):
 print()
 list_options()
 choice=input('Select an option: ')
 try:
  options[choice]()
 except LookupError: #hides the error when the user inputs a wrong option
  pass