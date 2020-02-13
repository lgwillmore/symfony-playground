#!/usr/bin/env python3
import subprocess


def check(status_code):
    if status_code != 0:
        exit(status_code)


def main():
    print("Restarting Apache")
    check(subprocess.call(
        "service apache2 restart".split()
    ))


if __name__ == '__main__':
    main()
