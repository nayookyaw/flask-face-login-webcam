/*

Nay Oo Kyaw
nayookyaw.nok@gmail.com

*/

The main purpose is to login with face using webcam

/*
Using Programming
 Flask api, Face-recognition, face comparison
 webcam , image taking 
 ajax, template, html, javascript
*/

## run
go to 'flask-face-login-webcam' folder

find server.py

$ python server.py

go to browser and enter

http://localhost:7000/

Take image from webcam and check result

If login is successful, page background will be green

If login fails, page background will be red

## Requirment

python version 3.6

```
pip install face_recognition
pip install flask
pip install scipy