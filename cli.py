# # Wriiten by Nishant Mittal aka nishantwrp
# import click
# import os
# import configparser
# import getpass
# import requests
# import platform

# import shutil
# from appdirs import *


# @click.command()

# @click.option('--info', 'action', flag_value='info',default = True,help="Displays Instructions For Using sublime-backup")
# @click.option('--update', 'action', flag_value='update',help="Update The Sublime Snippets Connected With Your Account With Those In Your Computer")
# @click.option('--get', 'action', flag_value='get',help="Downloads The Sublime Snippets In A Directory Snippets In The Present Working Directory")
# @click.option('--logout', 'action', flag_value='logout',help="Logs Out The Current User")
import argparse


def cli():
    parser = argparse.ArgumentParser(
        prog='mylibrary', description='Builds a file for deployment to server')

    parser.add_argument('--build', type=str, help='Builds the project')
    parser.add_argument('--deploy', action='store_true')

    args = parser.parse_args();

    if args.build:
        print(args.build)

    if args.deploy:
        print('deploy')


if __name__ == "__main__":
    cli()
