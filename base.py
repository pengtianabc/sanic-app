from functools import wraps
from sanic import response
from sanic.log import logger
import asyncio
from api.dao.cookie import checkcookie
from api.utils.common_util import GenRequestId
import err
def authorized(*args):
    def decorator(f):
        if asyncio.iscoroutinefunction(f):
            @wraps(f)
            async def decorated_function(request, *args, **kwargs):
                # run some method that checks the request
                # for the client's authorization status
                logger.debug("autorize args:%s"%str(args))
                is_authorized = checkcookie(request)
                if is_authorized:
                    # the user is authorized.
                    # run the handler method and return the response
                    r = await f(request, *args, **kwargs)
                    return r
                else:
                    # the user is not authorized. 
                    return response.json(err.BuildRepJson(err.CODE_NO_LOGIN), status=401)
            return decorated_function
        else:
            @wraps(f)
            def decorated_function_sync(request, *args, **kwargs):
                # run some method that checks the request
                # for the client's authorization status
                logger.debug("autorize args:%s"%str(args))
                is_authorized = checkcookie(request)
                if is_authorized:
                    # the user is authorized.
                    # run the handler method and return the response
                    r = f(request, *args, **kwargs)
                    return r
                else:
                    # the user is not authorized. 
                    return response.json(err.BuildRepJson(err.CODE_NO_LOGIN), status=401)
            return decorated_function_sync
    return decorator

async def filter_request(request):
    request.ctx.request_id = GenRequestId()

async def filter_response(request, response):
    response.headers["Server"] = "CapsheafAPIServer"
    response.headers["RequestId"] = request.ctx.request_id

request_middlewares = [
    filter_request
]
response_middlewares = [
    filter_response
]