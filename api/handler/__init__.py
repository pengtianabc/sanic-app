# file: api/handler/__init__.py
from sanic import Blueprint
from .demo import blueprint as bp_demo
from .demo2 import blueprint as bp_demo2
# register your blueprint here
bps = [bp_demo, bp_demo2]

# export for parent
blueprint = Blueprint.group(*bps, url_prefix='/handler')