from flask import Flask, render_template, url_for
from minio import Minio
from minio.error import InvalidResponseError


#To do - remove hardcode
client = Minio("192.168.99.10:9000",
               access_key="minioadmin",
               secret_key="minioadmin",
               secure=False)

# Get a full object
try:
    data = client.get_object('testbucket', 'Dratuti.jpg')
    with open('static/image.jpg', 'wb') as file_data:
         for d in data.stream(32*1024):
             file_data.write(d)
except InvalidResponseError as err:
    print(err)



app = Flask(__name__,template_folder='template')
@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template("./index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)