
docker build . --target bakery-frontend -t bakery-frontend
docker build . --target bakery-backend -t bakery-backend
docker-compose up
