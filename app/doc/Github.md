# Github

A good option is to use Github: it is free, reliable and devs are already familiar with it.

Store files on any of your Github private or public repositories using [PyGithub](https://github.com/PyGithub/PyGithub)

## Github Access Token

Generate a Github Access Token necessary to authenticate the API calls: go to `Account -> Settings -> Developer Settings -> Personal Access Token`

Grant the token the necessary privileges (read/write into repositories) and **NEVER** show or share your tokens.

See Github documentation if unsure: [Creating a personal access token
](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

## Code Samples

Here are some snippets to show how to read/write files

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


## Deploy to Heroku

Before deploying to Heroku make sure to define the Github Access Token as environment variable and create a corresponding Heroku Config Var
```
heroku config:set GITHUB_ACCESS_TOKEN=xyz)
```




