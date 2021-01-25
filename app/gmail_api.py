import yagmail

from config import *

# Send file by email

yag = yagmail.SMTP(get_gmail_username(), get_gmail_password())


def upload_file(recipient, attachment):
    """
        Send email with file
        :param recipient: recipient of the email
        :param attachment: path of local file to upload
        :return:
        """
    print(f"attachment {attachment}")

    contents = ['Body of email', attachment]

    yag.send(recipient, 'subject', contents)
