from github import Github

from config import get_github_access_token

REPO_NAME = 'HerokuFiles'
FOLDER_NAME = 'files'
FILE_NAME = 'files/file.json'

github = Github(get_github_access_token())


def get_repos():
    for repo in github.get_user().get_repos():
        print(repo.name)


def get_file(filename):
    repository = github.get_user().get_repo(REPO_NAME)
    file = repository.get_contents(filename)

    print(file.url)

    return file


def check_file_exist(filename):
    try:
        file = get_file(filename)
    except:
        return False

    return True


def put_file(filename, content):

    repository = github.get_user().get_repo(REPO_NAME)

    if check_file_exist(filename):
        f = get_file(filename)
        f = repository.update_file(filename, "commit test", content, f.sha)
    else:
        f = repository.create_file("test.txt", "commit test", content)

