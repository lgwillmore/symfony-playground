#!/usr/bin/env python3
import os
import subprocess


def check(status_code):
    if status_code != 0:
        exit(status_code)


testing_xml = [
    # "app/phpunit.xml",
    # "app/phpunit-integration.xml",
    "app/phpunit-features.xml",
]


def main():
    print("Running tests")
    my_env = os.environ.copy()
    my_env["SYMFONY_ENV"] = "test"
    for test in testing_xml:
        check(subprocess.call(
            ["vendor/bin/phpunit", "-c", test],
            cwd="/var/www/xturf-api",
            env=my_env
        ))


if __name__ == '__main__':
    main()
