#!/usr/bin/env python3
#coding:utf8

def create_app():
    from sanic import Sanic
    from sanic.response import json
    from sanic.response import text
    from sanic.log import logger
    from api import blueprint as api
    from api import views as api_views_base
    app = Sanic()
    app.blueprint(api)
    logger.debug("STARTING DUMMY DEBUG MSG")
    logger.info("STARTING DUMMY INFO MSG")
    logger.warn("STARTING DUMMY WARN MSG")
    logger.error("STARTING DUMMY ERROR MSG")
    logger.critical("STARTING DUMMY CRITICAL MSG")
    for vclass in api_views_base:
        v = vclass.as_view()
        url = "/api/%s"%vclass.__url__.lstrip("/")
        logger.info("Add views routing %s"%url)
        app.add_route(v, url)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, host="0.0.0.0", port=9000)

