#!/bin/bash
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart

#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#sudo gunicorn -c /home/box/web/etc/hello.py hello:app

sudo ln -sf /home/akellavolk/dev/stepik/web_mailru/server/etc/local.conf /etc/nginx/external.conf
sudo /etc/init.d/nginx restart

sudo gunicorn -c /home/akellavolk/dev/stepik/web_mailru/server/etc/hello.py hello:app
