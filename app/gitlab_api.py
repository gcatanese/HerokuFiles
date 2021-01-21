import gitlab

from config import get_gitlab_access_token

# Store files on Gitlab

REPO_ID = '23804786'

gl = gitlab.Gitlab('https://gitlab.com', private_token=get_gitlab_access_token())


def get_file(filename):

    project = gl.projects.get(REPO_ID)

    f = project.files.get(file_path=filename, ref='master')

    return f


def check_file_exist(filename):
    try:
        file = get_file(filename)
    except:
        return False

    return True


def put_file(filename, content):

    project = gl.projects.get(REPO_ID)

    action = 'create'

    if check_file_exist(filename):
        action = 'update'

    data = {
        'branch': 'master',
        'commit_message': 'Push file',
        'actions': [
            {
                'action': action,
                'file_path': filename,
                'content': content,
            }
        ]
    }

    commit = project.commits.create(data)

    print(commit)

