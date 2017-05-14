#!/usr/bin/env python

from sys import argv

from pingboard import *

if __name__ == '__main__':
    if len(argv) > 1:
        load_config(argv[1])

    api = API(client_id=get_config('pingboard.id'), client_secret=get_config('pingboard.secret'))

print api.request('GET', 'users')

