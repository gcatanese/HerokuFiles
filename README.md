Test

curl http://localhost:5000/check?filename=files/file.json

curl http://localhost:5000/get?filename=files/file.json

curl -i -X POST -H "Content-Type: application/json" -d "{\"name\":\"beppe\",\"city\":\"amsterdam\"}" http://localhost:5000/put?filename=files/file.json