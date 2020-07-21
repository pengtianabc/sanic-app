# file: api/handler/demo.py
from sanic import Blueprint
from sanic import response
from sanic.log import logger
from api.utils import redis_util
import asyncio
import json
blueprint = Blueprint('api_handler_demo', url_prefix='/demo')

# 文档: https://sanic.readthedocs.io/en/latest/sanic/request_data.html

# method 可以分开一起注册, 也可以分开注册
@blueprint.route('/', methods=['GET', 'POST'])
async def getTestInfo(request):
    logger.debug("request body: %s"%request.body)
    return response.json({"message": "HelloWorld, method:%s request_id:%s body:%s"%(request.method, request.ctx.request_id, request.body.decode('utf8'))})

@blueprint.route('/split_method', methods=['GET'])
async def getTestInfoSplitGet(request):
    return response.json({"message": "Hello GET"})

@blueprint.route('/split_method', methods=['POST'])
async def getTestInfoSplitPost(request):
    return response.json({"message": "Hello POST"})

# WebSocket Demo
@blueprint.websocket('/ws_redis_test')
async def get_live_data(request, ws):
    red = redis_util.GetRedisConn()
    sub = red.pubsub()
    sub.subscribe("test_channel")
    logger.info("Client in %s"%(request.remote_addr or request.ip))
    while True:
        msgs = redis_util.fetch_channel_msg(sub, sz=100)
        if not msgs:
            await asyncio.sleep(0.5)
        else:
            msg = json.dumps(msgs)
            logger.info("sending data to client:%s"%msg)
            # TODO: 将msg处理下
            # 发送数据给客户端
            await ws.send(msg)
            # TODO: 接收对方的ack, 暂时不处理命令
            # ack = await ws.recv()
            # logger.info("client ack:%s"%ack)
    sub.close()

