from flask import Blueprint, Response, make_response, jsonify
from flask_restx import Resource, Namespace, Api, fields, inputs
from datetime import datetime
from . import model

my_personal_authorization = {
    "Authorization": {
        "description": "Inputs: Bearer \\<jwtToken\\>",
        "name": "token",
        "type": "apiKey",
        "in": "header",
    }
}

swagger_bp = Blueprint('swagger_bp', __name__, url_prefix='/swagger')
swagger_ns = Namespace(
    path='/',name='',
    description='Exemplos Swagger'
    )
swagger_api = Api(
    app=swagger_bp,
    version='1.0',
    title='Exemplo',
    description='Métodos da API',
    authorizations=my_personal_authorization,
    security='apikey'
    )

swagger_api.add_namespace(swagger_ns)
parser =  swagger_ns.parser()

def monta_model():
    model_obj = swagger_ns.model(name='Tabela', model=model.campos_base)
    model_obj['rows'] = fields.List(fields.Nested(swagger_ns.model(name='Detalhes', model=model.campos)))

    return model_obj

@swagger_ns.route('/metodo_exemplo_simples')
@swagger_ns.doc(security=None)
class metodo_exemplo_simples(Resource):
    @swagger_ns.response(100, 'Continue')
    @swagger_ns.response(101, 'Switching Protocols')
    @swagger_ns.response(102, 'Processing (WebDAV; RFC 2518)')
    @swagger_ns.response(103, 'Early Hints (RFC 8297)')
    @swagger_ns.response(200, 'OK')
    @swagger_ns.response(201, 'Created')
    @swagger_ns.response(202, 'Accepted')
    @swagger_ns.response(203, 'Non-Authoritative Information')
    @swagger_ns.response(204, 'No Content')
    @swagger_ns.response(205, 'Reset Content')
    @swagger_ns.response(206, 'Partial Content')
    @swagger_ns.response(207, 'Multi-Status')
    @swagger_ns.response(208, 'Already Reported')
    @swagger_ns.response(226, 'IM Used')
    @swagger_ns.response(300, 'Multiple Choices')
    @swagger_ns.response(301, 'Moved Permanently')
    @swagger_ns.response(302, 'Found (Previously "Moved temporarily")')
    @swagger_ns.response(303, 'See Other')
    @swagger_ns.response(304, 'Not Modified')
    @swagger_ns.response(305, 'Use Proxy')
    @swagger_ns.response(306, 'Switch Proxy')
    @swagger_ns.response(307, 'Temporary Redirect')
    @swagger_ns.response(308, 'Permanent Redirect')
    @swagger_ns.response(400, 'Bad Request')
    @swagger_ns.response(401, 'Unauthorized')
    @swagger_ns.response(402, 'Payment Required')
    @swagger_ns.response(403, 'Forbidden')
    @swagger_ns.response(404, 'Not Found')
    @swagger_ns.response(405, 'Method Not Allowed')
    @swagger_ns.response(406, 'Not Acceptable')
    @swagger_ns.response(407, 'Proxy Authentication Required')
    @swagger_ns.response(408, 'Request Timeout')
    @swagger_ns.response(409, 'Conflict')
    @swagger_ns.response(410, 'Gone')
    @swagger_ns.response(411, 'Length Required')
    @swagger_ns.response(412, 'Precondition Failed')
    @swagger_ns.response(413, 'Payload Too Large')
    @swagger_ns.response(414, 'URI Too Long')
    @swagger_ns.response(415, 'Unsupported Media Type')
    @swagger_ns.response(416, 'Range Not Satisfiable')
    @swagger_ns.response(417, 'Expectation Failed')
    @swagger_ns.response(418, 'I\'m a teapot (RFC 2324, RFC 7168)')
    @swagger_ns.response(421, 'Misdirected Request')
    @swagger_ns.response(422, 'Unprocessable Content')
    @swagger_ns.response(423, 'Locked (WebDAV; RFC 4918)')
    @swagger_ns.response(424, 'Failed Dependency (WebDAV; RFC 4918)')
    @swagger_ns.response(425, 'Too Early (RFC 8470)')
    @swagger_ns.response(426, 'Upgrade Required')
    @swagger_ns.response(428, 'Precondition Required (RFC 6585)')
    @swagger_ns.response(429, 'Too Many Requests (RFC 6585)')
    @swagger_ns.response(431, 'Request Header Fields Too Large (RFC 6585)')
    @swagger_ns.response(451, 'Unavailable For Legal Reasons (RFC 7725)')
    @swagger_ns.response(500, 'Internal Server Error')
    @swagger_ns.response(501, 'Not Implemented')
    @swagger_ns.response(502, 'Bad Gateway')
    @swagger_ns.response(503, 'Service Unavailable')
    @swagger_ns.response(504, 'Gateway Timeout')
    @swagger_ns.response(505, 'HTTP Version Not Supported')
    @swagger_ns.response(506, 'Variant Also Negotiates (RFC 2295)')
    @swagger_ns.response(507, 'Insufficient Storage (WebDAV; RFC 4918)')
    @swagger_ns.response(508, 'Loop Detected (WebDAV; RFC 5842)')
    @swagger_ns.response(510, 'Not Extended (RFC 2774)')
    @swagger_ns.response(511, 'Network Authentication Required (RFC 6585)')
    def get(self):
        'Exemplo simples sem autenticação e retornando a descrição dos principais Status Code:\n<b>1xx</b> informational response\n<b>2xx</b> success\n<b>3xx</b> redirection\n<b>4xx</b> client errors\n<b>5xx</b> server errors\n\nPara maiores detalhes consultar: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes'
        return "OK"


@swagger_ns.route('/metodo_exemplo_parametros')
class metodo_exemplo_parametros(Resource):
    parser.args.clear()
    parser.add_argument(name='data', location='query', help='parametro data', required=True, type=inputs.date)
    parser.add_argument(name='numero', location='query', help='parametro numero', required=True, type=inputs.natural)   
    parser.add_argument(name='texto', location='query', help='parametro texto', required=False)
    @swagger_ns.expect(parser)
    @swagger_ns.response(200, 'OK')
    @swagger_ns.response(500, 'Internal Server Error')
    def get(self):
        'Exemplo parâmetros via GET'
        return "OK"
    

@swagger_ns.route('/metodo_exemplo_model')
class metodo_exemplo_model(Resource):
    @swagger_ns.response(200, 'OK', model=swagger_ns.model(name='Basic', model=monta_model()), headers=model.header)
    @swagger_ns.response(500, 'Internal Server Error')
    def get(self):
        'Exemplo parâmetros via GET'
        dados_retorno = {
              "datahora":  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
              "rows": [
                     {
                        'id': 123,
                        'texto': 'ABC',
                        'float': '1.234'
                     }
              ]
        }
                            
        return dados_retorno, 200, model.header


@swagger_ns.route('/metodo_exemplo_post')
@swagger_ns.doc(security=None)
class metodo_exemplo_post(Resource):
    @swagger_ns.response(200, 'OK')
    @swagger_ns.response(500, 'Internal Server Error')
    def post(self):
        'Exemplo post'
        dados_retorno = {
            'status':'ok'
        }

        return dados_retorno, 200, model.header
