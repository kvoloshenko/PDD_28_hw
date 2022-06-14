sudo apt install net-tools

ifconfig -a
192.168.0.109

https://www.cyberciti.biz/faq/ubuntu-linux-install-openssh-server/
Type command:
sudo apt-get install openssh-server
Enable the ssh service by typing:
sudo systemctl enable ssh
Start the ssh service by typing:
sudo systemctl start ssh

sudo systemctl status ssh

Configure firewall and open port 22
sudo ufw allow ssh
sudo ufw enable
sudo ufw status



Username: osboxes
Password: osboxes.org

Установка Python 3 и создание среды программирования в Ubuntu 18.04. [Краткое руководство]
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart-ru
Шаг 1 — Обновление и модернизация
sudo apt update
sudo apt -y upgrade

Шаг 2 — Проверьте версию Python
python3 -V
Шаг 3 — Установка pip
sudo apt install -y python3-pip

Шаг 5 — Установка venv
# sudo apt install -y python3-venv
sudo apt install python3-venv

Шаг 6 — Создание виртуальной среды
#python3.6 -m venv my_env
python3 -m venv django2 

Шаг 7 — Активизация виртуальной среды
# source my_env/bin/activate
source django2/bin/activate


- установка пакетов в окружение
pip freeze > requirements.txt
pip install -r requirements.txt

Enable Port In Ubuntu
# sudo ufw allow <port_nr>
sudo ufw allow 8000

4. Провека что запускается проекта
python manage.py runsever


---
5. Настройка базы данных (postgresql)

- Создание базы

sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql

CREATE DATABASE sitedb;
CREATE USER django with NOSUPERUSER PASSWORD 'nu123456';
GRANT ALL PRIVILEGES ON DATABASE sitedb TO django;

ALTER ROLE django SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE django SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE django SET TIME ZONE 'Asia/Yekaterinburg';

\q

- ПОдключение
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },

    'default': {
        'NAME': 'sitedb',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'django',
        'PASSWORD': 'nu123456',
        'HOST': 'localhost'
    }
}
---
- установка psycopg2
обновим pip
pip install --upgrade pip

Установка дополнительных пакетов
В окружении
sudo apt-get install libpq-dev python3.8-dev
pip install psycopg2

Проверка:
python manage.py migrate


6. gunicorn (uwsgi)
- установить
pip install gunicorn
- Тестовый запуск проекта
gunicorn kvblog.wsgi (из папки проекта)
- Регистрация gunicorn как сервиса (сеть, сокет)
sudo nano /etc/systemd/system/gunicorn.service

- текст файла
--------------------------------------
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/home/ubuntu/kvblog
ExecStart=/home/osboxes/django2/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/kvblog/kvblog.sock kvblog.wsgi

[Install]
WantedBy=multi-user.target
-----------------------------------------

WorkingDirectory - папка с проектом (где лежит manage.py)
/home/ubuntu/kvblog/django2/bin/gunicorn - путь до гуникорна в окружении
/home/osboxes/django2/lib/python3.10/site-packages 
/home/osboxes/django2/bin/gunicorn

# sudo usermod -a -G groupName userName

sudo usermod -a -G www-data osboxes

- Регистрация и запуск сервиса
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn (service gunicorn status) - должен быть active

7. nginx
- установка
sudo apt install nginx
service nginx status

- насройка nginx
cd /etc/nginx/sites-available/
- перенаправление запросов на сокет гуникорна
nano default
текст фала
---------------------------------------------
server {
    listen 80;
    server_name 192.168.0.109;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/kvblog;
    }

    location /media/ {
        root /home/ubuntu/kvblogg;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/kvblog/kvblog.sock;
    }
}
-------------------------------------------------
service nginx restart
