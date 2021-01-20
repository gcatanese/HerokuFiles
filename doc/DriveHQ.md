# DriveHQ

[DriveHQ](https://www.drivehq.com/) is a file server provider supporting FTP and WebDAV. It offers a 5 Free GB Basic Service.
 
Using the Python `ftplib` module it is pretty simple to store and fetch files via FTP.

Notes:
* signup for a DriveHQ Basic Account
* login with the same credentials using the Python api


**Example**

Checkout [sample code](https://github.com/gcatanese/HerokuFiles/tree/main/app/ftp_api.py) in ftp_api.py

## Deploy to Heroku

Before deploying to Heroku make sure to define the AWS credentials as environment variables and create the corresponding Heroku Config Vars
```
heroku config:set FTP_HOST=ftp.drivehq.com
heroku config:set FTP_USER=username
heroku config:set FTP_PWD=password
```




