
import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position' ]
clients = []


def _initilize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        write = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        write.writerows(clients)

        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)




def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        _client_was_found()


def list_clients():
    print(clients)


def update_client (client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        _client_not_found()


def delete_client(client_name):
    global clients
    for client in clients:
        if client_name == client['name']:
           command = input('Estas seguro de borrar este cliente? Y/N ')
           command = command.upper()
           if command == 'Y':
                clients.remove(client)
           else:
               print('Se cancelo el proceso de borrar un usuario')
               sys.exit()
        else:
            _client_not_found()


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('BIENVENIDOS A PLATZI VENTAS')
    print('*'*50)
    print('Que quieres hacer hoy?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('Cual es el {}?  '.format(field_name))
    return field

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('Cual es el nombre del cliente? ')

        if client_name == 'exit':
            break
        if not client_name:
            sys.exit()

    return client_name


def _client_not_found():
    return print('El cliente no esta registrado en la lista')


def _client_was_found():
    print('El cliente ya esta registrado en la lista')


if __name__ == '__main__':
    _initilize_clients_from_storage()
    
    _print_welcome()
    command = input("Escribe un comando: ")
    command = command.upper()
    if command == 'C':
        client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('comapany'),
        'email' : _get_client_field('email'),
        'position' : _get_client_field('position'),
        }

        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name) 
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('Inglrese la actualizacion en el nombre: ')
        update_client(client_name, updated_client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('Se encontro el cliente en la lista')
        else:
            _client_not_found()
    else:
        print('Comando invalido')


    _save_clients_to_storage()    