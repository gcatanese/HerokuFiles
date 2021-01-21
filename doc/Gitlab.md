# Gitlab

Store files on any of your Gitlab private or public repositories using [Python-Gitlab](https://python-gitlab.readthedocs.io/en/stable/index.html)

## Gitlab Personal Access Token

Generate a Github Personal Access Token: go to `Account -> Settings -> Access Tokens -> Add Personal Access Token`

Grant the token the necessary privileges (read/write into repositories) and **NEVER** show or share your tokens.


## Code Samples


**Example**

Checkout [sample code](https://github.com/gcatanese/HerokuFiles/tree/main/app/gitlab_api.py) in gitlab_api.py

## Deploy to Heroku

Before deploying to Heroku make sure to define the Access Token as environment variable and create a corresponding Heroku Config Var
```
heroku config:set GITLAB_ACCESS_TOKEN=xyz)
```




