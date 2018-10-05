'''
Logger class

Instantiates all methods required to log processes from a python application
Communicates with a web server where the logs are stored
'''
import requests


class Logger:

    def __init__(self):
        self