from flask_restx import fields

header = {
            'Content-Type'  : 'application/json'
}

campos_base = {
            'datahora': fields.DateTime,
}

campos = {
    'id': fields.Integer,
    'texto': fields.String,
    'float': fields.Float
}