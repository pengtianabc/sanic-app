# file: api/handler/demo.py
from sanic import Blueprint
from sanic import response

blueprint = Blueprint('api_handler_demo', url_prefix='/demo')

@blueprint.route('/')
async def getTestInfo(request):
    return response.json({"message": "HelloWorld"})

