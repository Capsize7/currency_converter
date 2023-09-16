# DRF Test task about currencies converter

This is a simple currencies converter based on Django Rest Framework. It is using a open service to get correct data of rates and update it every 1 hour via celery beat.

## Features
- Python
- Django
- PostgreSQL
- Docker
- Celery
- Celery-beat
- Redis

## How to install
```
1)Clone the project:
- git clone https://github.com/Capsize7/currency_converter      

2)Run the dockers images
- docker-compose up -d --build

3)Apply migrations for db
- docker-compose exec app python manage.py migrate --noinput

4)Check all tests
- python manage.py tests converter_api.tests (run this command in terminal of app container)

5)Example of request:
http://127.0.0.1:8000/api/rates/usd/rub/1/ (from - usd, to - rub, ammount - 1)

```

## License

The MIT License (MIT)
