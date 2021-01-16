import dropbox

from config import get_dropbox_access_token

# Store files on Dropbox

dbx = dropbox.Dropbox(get_dropbox_access_token())


def download_file(filename):
    """
    Get file from Dropbox
    :param filename: full path of the file
    :return:
    """
    print(f"filename {filename}")

    f, r = dbx.files_download(filename)

    content = r.content

    return content


def upload_file(filename, localfile):
    """
        Save file to Dropbox
        :param filename: path where to save the file
        :param localfile: path of local file to upload
        :return:
        """
    print(f"filename {filename}")

    with open(localfile, "rb") as f:
        dbx.files_upload(f.read(), filename, mute=True)




