FROM base_php:latest

EXPOSE 80 443
WORKDIR /var/www/symfonyplay

# Can customise the base php environment for testing and local environment needs here.
RUN apt-get update

RUN apt-get install -y mysql-client iputils-ping curl vim

RUN a2enmod ssl

COPY ./vhost.conf /etc/apache2/sites-available/symfonyplay.conf
RUN a2ensite symfonyplay.conf \
    && a2enmod rewrite \
    && a2enmod headers

RUN service apache2 restart

# WIP for getting remote debugging
#RUN yes | pecl install xdebug
#RUN docker-php-ext-enable xdebug
#RUN echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini
#RUN echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini
#RUN echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini
#RUN echo "xdebug.remote_host=host.docker.internal" >> /usr/local/etc/php/conf.d/xdebug.ini
