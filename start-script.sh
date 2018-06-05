docker-compose build
docker-compose run web django-admin.py startproject mysite .
sudo chown -R $USER:$USER .
docker-compose up