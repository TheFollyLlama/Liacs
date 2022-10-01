To build application:
  Install Docker, and Docker-Compose

  On Mac/Linux:
  Run on command line: "bash ru n.sh"
  This builds frontend and backend (so it will include any changes you make), and starts all the images (including DB)

  On Windows:
  - TODO, but I'm know there is a windows equivalent to building the 2 docker images, and docker-compose up.
          you may even just be able to rename run.sh to run.bat


Once the application is up:
  To interact with the frontend: "localhost:3000"
  To interact with the backend: "localhost:5000"

  To access the containers: "docker exec -it backend /bin/bash" or "docker exec -it frontend /bin/bash"

  Backend endpoints:
  - GET /welcome
  - GET /products
  - GET /order
  - POST /order {"product_name":""  , "quantity":""}
  - DELETE /order

  To send a POST request from commandline
  curl -d @test.json  -H "Content-Type: application/json" -v  -X POST localhost:5000/order
  (where test.json is a file including the required json. i.e.: {"product_name": "Poffertjes","quantity": 121})
