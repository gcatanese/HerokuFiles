# Remote files with Heroku

Heroku file system is [ephemeral](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), meaning Dyno applications can write on the file system but 
changes are discared when the Dyno restarts.

It is also important to remember that Heroku Dynos restart (at least) every 24 hrs (see [cycling](https://devcenter.heroku.com/articles/dynos#restarting)), 
dus deleting all local filesystem changes.

Applications which need to persist data should rely on an external service like a database or a remote storage.

## Free options for remote file storage 

For applications that need to store files there are few remote storage cloud services offering a **free tier**, some of them limiting the size and/or the features available.
  
They all provide a secure (tokens, credentials) access via APIs and are suitable for both projects under development or in production (see details of each provider):

* [Github](doc/Github.md)
* [S3](doc/S3.md)
* [Dropbox](doc/Dropbox.md)
* [DriveHQ (FTP)](doc/DriveHQ.md)
* [Gitlab](doc/Gitlab.md)


