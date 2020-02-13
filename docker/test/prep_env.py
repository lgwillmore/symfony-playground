#!/usr/bin/env python3
import subprocess


def check(status_code):
    if status_code != 0:
        exit(status_code)


prep_env_commands = [
    "composer run-script post-install-cmd --no-interaction".split(),
    "mysql -u root -proot -h maria -e ".split() + ["GRANT ALL PRIVILEGES ON *.* TO 'digitote';"],
    "php bin/console digitote:xturf:install-files -e dev".split(),
    # "composer update --with-dependencies --no-progress --optimize-autoloader".split(),
    "php bin/console doctrine:database:create --if-not-exists --no-interaction -vvv -e dev".split(),
    "php bin/console cache:clear -e dev".split(),
    "php bin/console doctrine:schema:drop --force --no-interaction -e dev".split(),
    "php bin/console doctrine:schema:create --no-interaction -e dev".split(),
    "php bin/console doctrine:fixtures:load -n -e dev".split(),
    "php bin/console digitote:capability:reload -e dev".split(),
    "php bin/console digitote:workspace:reload -e dev".split(),
    "php bin/console digitote:user:promote john -e dev".split(),
    "php bin/console digitote:unifiedodds:import-providers -e dev".split(),
    "bin/console memcache:clear default -e dev".split(),
    "bin/console cache:clear -e dev".split()
]


def main():
    print("Preparing env")
    for prep_command in prep_env_commands:
        check(subprocess.call(
            prep_command,
            cwd="/var/www/xturf-api"
        ))


if __name__ == '__main__':
    main()
