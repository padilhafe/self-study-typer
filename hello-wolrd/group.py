import typer

repo_app = typer.Typer()
star_app = typer.Typer()

@repo_app.command(name='list')
def repo_list():
    print("repo list")

@repo_app.command(name='delete')
def repo_delete():
    print("repo delete")

@star_app.command(name='list')
def star_list():
    print("star list")

@star_app.command(name='delete')
def star_delete():
    print("star delete")

app = typer.Typer()
app.add_typer(repo_app, name='repo')
app.add_typer(star_app, name='star')

if __name__ == "__main__":
    app()