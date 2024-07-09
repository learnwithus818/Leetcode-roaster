web: gunicorn assistantApp.wsgi --log-file -
worker: celery -A assistantApp worker --loglevel=info