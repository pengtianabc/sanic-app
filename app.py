#!/usr/bin/env python3
#coding:utf8
from sanic.log import logger

# 全局debug开关 如果通过sanic命令行开启会自动忽略该字段
# 通过命令行运行
# https://sanic.readthedocs.io/en/latest/sanic/deploying.html
# python3 -m sanic app.app --host=0.0.0.0 --port=9000 --worker=1 --debug
DEBUG_MODE=True

def create_app():
    global DEBUG_MODE
    import os
    import logging
    from sanic import Sanic
    from sanic.response import json
    from sanic.response import text
    from api import blueprint as api
    from api import views as api_views_base
    app = Sanic()
    app.blueprint(api)
    if __name__ == "__main__":
        loglevel = logging.DEBUG if DEBUG_MODE else logging.INFO
        logger.setLevel(loglevel)
    logger.debug("\tSTARTING DUMMY DEBUG MSG")
    logger.info("\tSTARTING DUMMY INFO MSG")
    logger.warn("\tSTARTING DUMMY WARN MSG")
    logger.error("\tSTARTING DUMMY ERROR MSG")
    logger.critical("STARTING DUMMY CRITICAL MSG")
    for vclass in api_views_base:
        v = vclass.as_view()
        url = "/api/%s"%vclass.__url__.lstrip("/")
        app.add_route(v, url)
    for handler, (rule, router) in app.router.routes_names.items():
        logger.info("Route: %s methods: %s name: %s"%(rule, '/'.join(list(router.methods)), router.name))
    from base import request_middlewares, response_middlewares
    logger.info("Resigtering request middlewares")
    for ware in request_middlewares:
        app.register_middleware(ware, attach_to="request")
    logger.info("Resigtering response middlewares")
    for ware in response_middlewares:
        app.register_middleware(ware, attach_to="response")
    logger.info("Register static dir to %s"%(os.path.realpath("./static")))
    app.static('/static', './static')
    return app

app = create_app()
if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, host="0.0.0.0", port=9000, access_log=True)

