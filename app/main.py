from flask import Flask, request, Response
from flask import send_file
import logging
import requests
import os
from github_api import *

try:
    app = Flask(__name__)

    print(check_file_exist('files/file.json'))

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


@app.route('/get')
def get():
    """
    Ping the endpoint
    :return:
    """
    logging.info('/get')

    g = get_file()

    return g.decoded_content.decode()


@app.route('/put')
def put():
    """
    Ping the endpoint
    :return:
    """
    logging.info('/get')

    put_file()

    return "Ok"

def get_port():
    """
    Retrieves port
    :return:
    """
    return int(os.environ.get("PORT", 5000))


if __name__ == '__main__':

    logging.info('Starting up')

    app.run(debug=True, port=get_port(), host='0.0.0.0')
