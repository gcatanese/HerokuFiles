# Remote files with Heroku

Heroku file system is [ephemeral](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), meaning Dyno applications can write on the file system but 
changes are discared when the Dyno restarts.

It is also important to remember that Heroku Dynos restart (at least) every 24 hrs (see [cycling](https://devcenter.heroku.com/articles/dynos#restarting)), 
dus deleting all local filesystem changes.

Applications which need to persist data should rely on an external service like a database or a remote storage.

## Free options for remote file storage 

For applications that require low IO activities (save some changes in file, upload small number of files) there are 
few remote storage cloud services which offer a free tier, some of them limiting the size and/or features available.
These are definitely good alternatives if the application is not storing a large volume of data or save confidential information.

* [Github](app/doc/Github.md)
* [S3](app/doc/S3.md)
* [Dropbox](app/doc/Dropbox.md)
* [DriveHQ (FTP)](app/doc/DriveHQ.md)


