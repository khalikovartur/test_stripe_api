From your terminal:
1) mkdir code && cd code
2) git clone https://github.com/khalikovartur/test_stripe_api.git
3) docker-compose up -d --build
4) docker-compose exec web pipenv sync
5) docker-compose exec web python manage.py migrate
6)  docker-compose exec web python manage.py createsuperuser
7) go to http://127.0.0.1:8000/admin/ create item 
8) go to http://127.0.0.1:8000/item/{item.id}/