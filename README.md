# TS-Django-Seller-Marketplace

*****

Para iniciar o projeto:

  poetry shell
  poetry install
  python manage.py migrations 
  python manage.py runserver

*****
Para iniciar o container docker Postgres

docker run -d -e POSTGRES_USER=olist -e POSTGRES_PASSWORD=olist123 --name=projectApp -p 5433:5432 postgres
