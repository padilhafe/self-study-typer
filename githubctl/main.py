import typer
from rich import print
from github import get_all_user_repositories

app = typer.Typer()
repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")

@repo_app.command(name="list", help="list user repository")
def list_repos(user: str = typer.Option(..., "--user", "-u", help="github username")):
    repo = get_all_user_repositories(username=user)
    print(repo)

if __name__ == "__main__":
    app()