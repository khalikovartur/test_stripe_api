From your terminal:
1) mkdir code && cd code
2) git clone https://github.com/khalikovartur/test_stripe_api.git
3) cd test_stripe_api
4) docker-compose up -d 
4) docker-compose exec web pipenv sync
5) docker-compose down
6) docker-compose up -d --build
7) docker-compose exec web python manage.py migrate
8)  docker-compose exec web python manage.py createsuperuser
9) go to http://127.0.0.1:8000/admin/   when create item 
10) go to http://127.0.0.1:8000/item/{item.id}/