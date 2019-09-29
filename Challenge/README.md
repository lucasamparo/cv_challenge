# Senai CIMATEC - Atos Bull Computer Vision Formation Challenge
 </br>
<h3>This is an API to find out where the black hole is, given the coordinates of 2 stars at different times.</h3>
 </br>

## HOW TO USE

* Run ```docker-compose up --build``` command in the Challenge folder
* Acess <a href="http://localhost:5000" title="Localhost">Localhost:5000</a> (swagger)
 or use </br>
```curl -X POST "http://0.0.0.0:5000/findBlackHole" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"numberOfTeste\": 3, \"coordenates\": [ [ 12, 2 ], [ 5, 6 ], [ 10, 8 ], [ 2, 7 ], [ 0.5, -0.5 ], [ -1, 0 ], [ -0.5, -0.5 ], [ 0, 1 ], [ 0.5, 6.5 ], [ -10.5, -3.5 ], [ -1.5, 6.5 ], [ -5.5, -8.5 ] ]}"```
