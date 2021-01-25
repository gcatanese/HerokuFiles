# Gmail

Send a file by email using your Gmail account and the [yagmail](https://github.com/kootenpv/yagmail) Python library.

This is a very basic approach but it might be useful if there is the need to save a file somewhere for backup or 
for performing a quick analysis

## Gmail

You will need to use your Gmail credentials as well as enabling `Allow less secure apps` in the Gmail settings, see 
[here](https://www.google.com/settings/security/lesssecureapps) 

## Code Samples

**Example**

Checkout [sample code](https://github.com/gcatanese/HerokuFiles/tree/main/app/gmail_api.py) in gmail_api.py

## Deploy to Heroku

Before deploying to Heroku make sure to define the credentials as environment variables and create the corresponding Heroku Config Vars
```
heroku config:set GMAIL_USERNAME=xyz)
heroku config:set GMAIL_PASSWORD=abc)
```




