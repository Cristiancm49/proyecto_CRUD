from http import client
from unicodedata import name
import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manejo de clientes"""
    pass


@clients.command()
@click.option('-n', '--name',
             type=str,
             prompt=True,
             help='El nombre del cliente')
@click.option('-c', '--company',
             type=str,
             prompt=True,
             help='La compania del cliente')
@click.option('-e', '--email',
             type=str,
             prompt=True,
             help='El email del cliente')
@click.option('-p', '--position',
             type=str,
             prompt=True,
             help='La position del cliente')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create crea un nuevo cliente"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """Lista de clientes"""
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    click.echo('  ID  |  NAME  | COMANY  | EMAIL  | POSITION  ')
    click.echo('*' * 100)

    for client in clients_list:
        print('{uid} | {name} | {company}| {email} | {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'],))


@clients.command()
@click.pass_context
def update(ctx, clients_iud):
    """Cargar clientes"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_iud):
    """Eliminar clientes"""
    pass


all = clients
