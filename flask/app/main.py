# импорт модулей приложения
from flask import Flask, render_template, url_for
from minio import Minio
from minio.error import InvalidResponseError

# Объявление экземпляра объекта "Клиент MinIO"
# Это место можно улучшить, убрав т.н. хардкод - прямое указание адреса и ключей
# доступа. В продакш среде никогда не стоит так делать. А секреты лучше получать из
# предназначеных для этого систем типа Hashicorp Vault, GitLab Secret Variables и т.п.
# так же в этом месте не предусмотрена обработка исключений. если база будет недоступна то
# приложение завершится с ошибкой
#To do - remove hardcode
client = Minio("192.168.99.10:9000",
               access_key="minioadmin",
               secret_key="minioadmin",
               secure=False)
# Скачиваем с MinIO файл
# Get a full object
try:
    data = client.get_object('testbucket', 'Dratuti.jpg')
    with open('static/image.jpg', 'wb') as file_data:
         for d in data.stream(32*1024):
             file_data.write(d)
except InvalidResponseError as err:
    print(err)


# Объявляем экземпляр приложения Flask, указываем в параметре template_folder
# что файлы веб страниц будут содержаться в папке template
app = Flask(__name__,template_folder='template')
@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template("./index.html")

# запускаем приложение функцией run, которая запустит веб-сервер с нашим приложением на всез интерфейсах и порту 80
# В продакшен среде не рекомендуется использовать run. Более подробно в документации к Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)