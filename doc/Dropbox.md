# Dropbox

[Dropbx](https://www.dropbox.com/) is a file hosting service that offer various plans at different prices.
The Dropbox Basic account is free and allows storing up to 2GB of files.

The intuitive Web User Interface can be used to create, edit and download files, there is a nice integration
with Google docs and Office Online, but what you really want to use is the [Python Dropbox SDK](https://www.dropbox.com/developers/documentation/python)

## Dropbox Setup

Sign up for a Dropbox account then register a new app in the `App Console`. After defining the permissions (ie files.content.write, files.content.read) 
generate the Access Token. 


## Code Samples

Here are some snippets to show how to read/write files

**Create a file**
```
dbx = dropbox.Dropbox('access_token')

filename = '/local_files/file.json'
dbx.files_upload(f.read(), filename, mute=True)
```

**Get a file**
```
dbx = dropbox.Dropbox('access_token')

filename = '/dropbox_root/file.json'
f, r = dbx.files_download(filename)

print(r.content)
```

**Example**

Checkout [sample code](https://github.com/gcatanese/HerokuFiles/tree/main/app/dropbox_api.py) in dropbox_api.py

## Deploy to Heroku

Before deploying to Heroku make sure to define the Access Token as environment variable and create a corresponding Heroku Config Var
```
heroku config:set DROPBOX_ACCESS_TOKEN=xyz)
```




