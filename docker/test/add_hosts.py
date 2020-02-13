#!/usr/bin/env python3
import os
import subprocess


def check(status_code):
    if status_code != 0:
        exit(status_code)


def setup_hosts():
    local_hosts = "127.0.0.1    api.xturf.intra test-api.xturf.intra"
    with open("/etc/hosts", "r+") as file:
        for line in file:
            if local_hosts in line:
                break
        else:  # not found, we are at the eof
            file.write(local_hosts)  # append missing data


def main():
    print("Setting up /etc/hosts")
    setup_hosts()


if __name__ == '__main__':
    main()
