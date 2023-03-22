docker compose up -d
docker ps
docker compose down

changes in model: makemigrations recruitment_app

recreate db: python manage.py migrate --fake myappname zero