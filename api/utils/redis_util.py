import redis
def GetRedisConn():
    # TODO: use custom redis configuration
    return redis.Redis()

def fetch_channel_msg(sub, sz=100):
    '''
    sub: redis channel subscriber
    sz: max message size
    '''
    cnt = 0
    lst = []
    while cnt <= sz:
        data = sub.get_message()
        if data == None:
            break
        if data['type'] != 'message':
            continue
        msg = data['data'].decode('utf8')
        lst.append(msg)
        cnt += 1
    return lst