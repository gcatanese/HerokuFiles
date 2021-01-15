# Remote files with Heroku

Heroku file system is [ephemeral](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), meaning Dyno applications can write on the file system but 
changes are discared when the Dyno restarts.

It is important to remember that Heroku Dynos restart (at least) every 24 hrs (see [cycling](https://devcenter.heroku.com/articles/dynos#restarting)), 
dus deleting all local filesystem changes.

Applications which need to persist data should rely on an external service like a database or a remote storage.

## Free options for remote file storage 

### Github

Use a Github repository and put/get files using [PyGithub](https://github.com/PyGithub/PyGithub)

**Create a file**
```
github = Github('access_token)
repository = github.get_user().get_repo('my_repo')

content = '{\"name\":\"beppe\",\"city\":\"amsterdam\"}'
f = repository.create_file('data.json', "create_file via PyGithub", content)
```

**Get a file**
```
github = Github('access_token)
repository = github.get_user().get_repo('my_repo')

file = repository.get_contents(filename)
print(file.decoded_content.decode())
```

**Example**

Checkout [Python app sample code](https://github.com/gcatanese/HerokuFiles/tree/main/app) which provides few Flask 
endpoints demonstrating the access to `Github`

```
curl http://localhost:5000/check?filename=files/file.json

curl http://localhost:5000/get?filename=files/file.json

curl -i -X POST -H "Content-Type: application/json" -d "{\"name\":\"beppe\",\"city\":\"amsterdam\"}" http://localhost:5000/put?filename=files/file.json
```