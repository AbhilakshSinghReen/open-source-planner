from src.github_apis import get_repo_star_count, get_repo_issue_count


repo_url = "https://github.com/kubernetes/kubernetes"


def main():
    print(get_repo_star_count(repo_url))
    print(get_repo_issue_count(repo_url))


if __name__ == "__main__":
    main()
