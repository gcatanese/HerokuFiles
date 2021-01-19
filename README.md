# Remote files with Heroku

Heroku file system is [ephemeral](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), meaning Dyno applications can write on the file system but 
changes are discared when the Dyno restarts.

It is also important to remember that Heroku Dynos restart (at least) every 24 hrs (see [cycling](https://devcenter.heroku.com/articles/dynos#restarting)), 
dus deleting all local filesystem changes.

Applications which need to persist data should rely on an external service like a database or a remote storage.

## Free options for remote file storage 

For applications that require limited IO activities (save some changes in file, upload small number of files) there are 
few remote storage cloud services offering a **free tier**, some of them limiting the size and/or the features available.  
These are definitely good alternatives if the application does need to deal with a large volume of data or saving confidential information.

* [Github](doc/Github.md)
* [S3](doc/S3.md)
* [Dropbox](doc/Dropbox.md)
* [DriveHQ (FTP)](doc/DriveHQ.md)


