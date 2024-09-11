from flask import Flask
from . import swagger

app = Flask(__name__)

app.register_blueprint(swagger.swagger_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
