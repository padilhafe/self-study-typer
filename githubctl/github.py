import requests
from dotenv import dotenv_values

config = dotenv_values()
def get_all_user_repositories(username):
    base_url = f"https://api.github.com/users/{username}/repos"
    repos = []
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {config['GITHUB_TOKEN']}"
    }

    try:
        page = 1
        while True:
            params = {"page": page, "per_page": 100}
            response = requests.request("GET", base_url, headers=headers, params=params)
            response.raise_for_status()

            repositories = response.json()
            if not repositories:
                break

            for repo in repositories:
                repos.append({
                    "id": repo['id'],
                    "name": repo['name'],
                    "html_url": repo['html_url'],
                    "description": repo['description'],
                    "language": repo['language'],
                    "stargazers_count": repo['stargazers_count'],
                    "forks_count": repo['forks_count'],
                    "fork": repo['fork'],
                    "created_at": repo['created_at'],
                })

            page += 1

        return repos

    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories for user {username}: {e}")
        return None
