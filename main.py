# Copyright 2021 BFDestroyeer

import os
from argparse import ArgumentParser
from flask import Flask, send_from_directory


def __get_argument_parser() -> ArgumentParser:
    """
    Returns argument parser
    :return: argument parser
    """
    parser = ArgumentParser()
    parser.add_argument("port", type=int, action="store", choices=range(0, 65535), help="Server port number")
    return parser


def main(arguments):
    os.makedirs('shared', exist_ok=True)
    app = Flask(__name__, static_url_path='')

    @app.route('/download/<path:path>')
    def download_file(path):
        return send_from_directory('shared', path)

    app.run(host='0.0.0.0', port=arguments.port)


if __name__ == "__main__":
    main(__get_argument_parser().parse_args())
