pip install -r requirements.txt
cd bacend\FastAPI\database\DOCKER
docker-compose up -d
cd ..\..\
uvicorn main:app --reload