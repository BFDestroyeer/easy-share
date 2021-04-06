# Copyright 2021 BFDestroyeer

import os
from argparse import ArgumentParser
from flask import Flask, send_from_directory, render_template


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

    @app.route('/download/')
    def show_root():
        full_path = './shared/'
        if not os.path.exists(full_path):
            return
        files = os.listdir(full_path)
        links = []
        for file in files:
            links.append({
                'name': file,
                'url': '/download/' + '/' + file
            })
        print(links)
        return render_template('index.html', links=links)

    @app.route('/download/<path:path>')
    def download_file(path):
        full_path = './shared/' + path
        if not os.path.exists(full_path):
            return
        if os.path.isfile(full_path):
            return send_from_directory('shared', path)
        files = os.listdir(full_path)
        links = []
        for file in files:
            links.append({
                'name': file,
                'url': '/download/' + path + '/' + file
            })
        print(links)
        return render_template('index.html', links=links)

    app.run(host='0.0.0.0', port=arguments.port)


if __name__ == "__main__":
    main(__get_argument_parser().parse_args())
