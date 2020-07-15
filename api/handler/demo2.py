# file: api/handler/demo2.py
from sanic import Blueprint
from sanic import response

blueprint = Blueprint('api_handler_demo2', url_prefix='/demo2')

@blueprint.route('/')
async def getTestInfo(request):
    return response.json({"message": "HelloWorld bp_demo2"})

