import click


@click.group()
def clients():
    """Manejo de clientes"""
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Create crea un nuevo cliente"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """Lista de clientes"""
    pass


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
