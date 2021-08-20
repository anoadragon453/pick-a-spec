import random
from github import Github
from github.Issue import Issue


def main():
    github_repo = "matrix-org/matrix-doc"

    with open("token") as f:
        github_token = f.read().strip()

    g = Github(github_token)
    r = g.get_repo(github_repo)

    # Get MSC Issues
    mscs = r.get_issues(
        state="open",
        labels=["proposal"],
    )

    pick: Issue = random.choice([msc for msc in mscs])

    print(f"Your random MSC is {pick.title} - {pick.html_url}")


if __name__ == '__main__':
    main()
