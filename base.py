from functools import wraps
from sanic import response
from sanic.log import logger
from api.dao.cookie import checkcookie
import err
def authorized(*args):
    def decorator(f):
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
                return response.json(err.BuildRepJson(err.CODE_NO_LOGIN), 401)
        return decorated_function
    return decorator

def authorized_sync(*args):
    def decorator(f):
        @wraps(f)
        def decorated_function(request, *args, **kwargs):
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
                return response.json(err.BuildRepJson(err.CODE_NO_LOGIN), 401)
        return decorated_function
    return decorator
