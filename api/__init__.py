# api/__init__.py
from sanic import Blueprint
from sanic.log import logger
from .handler import blueprint as bp_handler
from .view import views as all_views
bps = [bp_handler]
# export for parent
blueprint = Blueprint.group(*bps, url_prefix='/api')
views = []

def preprocess_view(vclass_lst, prefix=''):
    global views
    logger.debug("preprocessing vclass_lst:%s"%vclass_lst)
    prefix = prefix.rstrip('/')
    for vclass in vclass_lst:
        if not hasattr(vclass, '__url__'):
            logger.error("Invalid view class %s without __url__ attr, skip"%vclass.__name__)
            continue
        if not vclass.__url__:
            logger.error("Invalid view class %s empty __url__ attr, skip"%vclass.__name__)
            continue
        vclass.__url__ = "%s/%s"%(prefix, vclass.__url__.lstrip('/'))
        views.append(vclass)

preprocess_view(all_views, prefix='view')
