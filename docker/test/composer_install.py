#!/usr/bin/env python3
import os
import subprocess

install = ["composer", "install"]


def check(status_code):
    if status_code != 0:
        exit(status_code)


def main():
    print("Running composer install")

    my_env = os.environ.copy()
    my_env["COMPOSER_PROCESS_TIMEOUT"] = "600"
    my_env["SYMFONY_ENV"] = "test"

    check(subprocess.call(
        install,
        cwd="/var/www/symfonyplay",
        env=my_env
    ))


if __name__ == '__main__':
    main()
