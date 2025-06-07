from src.github_apis import get_repo_metadata


repo_url = "kubernetes/kubernetes"


def main():
    repo_metadata = get_repo_metadata(repo_url)
    
    stars = repo_metadata.get('stargazers_count', "N/A")
    open_issues = repo_metadata.get('open_issues_count', "N/A")

    languages_url = repo_metadata.get('languages_url', None)

    print(stars)
    print(open_issues)
    print(languages_url)

    # print()
    # print(get_repo_issue_count(repo_url))


if __name__ == "__main__":
    main()
