import logging
import os

from flask import Flask, request

from github_api import *

try:
    app = Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
except Exception as e:
    logging.exception("Error at startup")


@app.route('/ping')
def ping():
    """
    Ping the endpoint
    :return:
    """
    logging.info('/ping')
    return "ping Ok"


@app.route('/check')
def check():
    """
    Check file exists
    :return:
    """
    logging.info('/check')

    # filename (ie files/file.json)
    filename = request.args.get('filename')

    ret = check_file_exist(filename)

    return str(ret)


@app.route('/get')
def get():
    """
    Get file
    :return:
    """
    logging.info('/get')

    # filename (ie files/file.json)
    filename = request.args.get('filename')

    file = get_file(filename)

    return file.decoded_content.decode()


@app.route('/put', methods=['POST'])
def put():
    """
    Store file
    :return:
    """
    logging.info('/put')

    # filename (ie files/file.json)
    filename = request.args.get('filename')
    content = str(request.json)

    put_file(filename, content)

    return "Ok"


def get_port():
    """
    Retrieves port
    :return:
    """
    return int(os.environ.get("PORT", 5000))


if __name__ == '__main__':
    app.run(debug=True, port=get_port(), host='0.0.0.0')
