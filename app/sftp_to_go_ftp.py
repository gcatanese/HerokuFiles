import ftplib

from config import *

# Store files on SFTP To Go server


def download_file(filename, tmpfile):
    """
    Get file from FTP server
    :param filename: full path of the file
    :return:
    """
    print(f"filename {filename}")

    session = ftplib.FTP_TLS(get_ftp_host(), get_ftp_username(), get_ftp_password())
    session.prot_p() # data-channel protected by TLS

    f = open(tmpfile, 'wb')
    session.retrbinary('RETR ' + filename, f.write, 1024)

    session.quit()
    f.close()

    f = open(tmpfile, 'rb')
    content = f.read()

    return content


def upload_file(filename, localfile):
    """
        Save file to SFTP server
        :param filename: path where to save the file
        :param localfile: path of local file to upload
        :return:
        """
    print(f"filename {filename}")

    session = ftplib.FTP_TLS(get_ftp_host(), get_ftp_username(), get_ftp_password())
    session.prot_p() # data-channel protected by TLS

    file = open(localfile, 'rb')  # file to send
    session.storbinary('STOR '+filename, file)  # send the file
    file.close()  # close file and FTP
    session.quit()

