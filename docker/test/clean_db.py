#!/usr/bin/env python3
import subprocess

working_dir = "/var/www/xturf-api"

drop_db = ["php", "bin/console", "doctrine:database:drop", "--force"]
create_db = ["php", "bin/console", "doctrine:database:create"]
create_schema = ["php", "bin/console", "doctrine:schema:create"]
emulate_migrations = ["php", "bin/console", "doctrine:migrations:version", "--add", "--all"]
check_migrations = ["php", "bin/console", "doctrine:migrations:status"]
yes = ["yes"]


def check(status_code):
    if status_code != 0:
        exit(status_code)


def main():
    print("Cleaning DB")
    check(subprocess.call(drop_db, cwd=working_dir))
    check(subprocess.call(create_db, cwd=working_dir))
    check(subprocess.call(create_schema, cwd=working_dir))

    p1 = subprocess.Popen(yes, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p2 = subprocess.Popen(emulate_migrations, cwd=working_dir, stdin=p1.stdout, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    p1.stdout.close()
    p2.wait()
    p2.stdout.close()
    check(subprocess.call(check_migrations, cwd=working_dir))


if __name__ == '__main__':
    main()
