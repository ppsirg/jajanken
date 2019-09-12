# -*- coding: utf-8 -*-

import os
from subprocess import call
from concurrent.futures import ProcessPoolExecutor as PE
from time import sleep

base_dir = os.path.join(os.getcwd())


def send(filename, destiny):
    filepath = os.path.join(base_dir, filename)
    call('cp -rfv {} {}'.format(filepath, destiny).split(' '))
    print('moved {}, i will wait for a while...'.format(filepath))
    sleep(300)


def run(destiny):
    dir_list = os.listdir(os.getcwd())
    with PE(max_workers=2) as t:
        for _dir in dir_list:
            t.submit(
                send, _dir, destiny
            )
