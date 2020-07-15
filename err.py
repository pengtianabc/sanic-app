CODE_SUCCESS = 0
CODE_NO_LOGIN = 2 #
CODE_NOT_PERMITED = 3
CODE_OPERATION_FAIL = 4
CODE_INTERNAL_ERROR = 5
CODE_USER_PWD_ERROR = 6
CODE_VCODE_ERROR = 7
CODE_GEN_TOKEN_ERROR = 8
CODE_INVALID_REQUEST_FORMAT = 9
CODE_ACTION_FAIL = 10
CODE_UNSUPPORT_TYPE = 11
CODE_UNSUPPORT_LISTTYPE = 12
CODE_DATA_EXPIRED = 13
CODE_SAME_AND_UNMODIFIED = 14
CODE_DUP_USER = 15
CODE_CONNECT_DB_FAIL = 16
CODE_ADD_USER_FAIL = 17
CODE_EXISTING_USERNAME = 18
CODE_NON_EXISTS_USER = 19
CODE_INVALID_ACTION = 20
CODE_PWD_ERROR = 21
CODE_EXISTING_NAME = 22
CODE_EXCEED_MAX_VALUE = 23

MESSAGE_JSON = {
    CODE_SUCCESS: "成功"
    , CODE_NO_LOGIN: "用户未登录"
    , CODE_NOT_PERMITED: "无操作权限"
    , CODE_OPERATION_FAIL: "操作失败"
    , CODE_INTERNAL_ERROR: "内部错误"
    , CODE_USER_PWD_ERROR: "用户名或密码错误"
    , CODE_VCODE_ERROR: "验证码错误"
    , CODE_GEN_TOKEN_ERROR: "生成token失败"
    , CODE_INVALID_REQUEST_FORMAT: "请求数据格式有误"
    , CODE_ACTION_FAIL: "操作失败"
    , CODE_UNSUPPORT_TYPE: "不支持的类型"
    , CODE_DATA_EXPIRED: "数据过期，请重试"
    , CODE_SAME_AND_UNMODIFIED: "前后数据相同，未修改"
    , CODE_DUP_USER: "操作失败，已存在的用户"
    , CODE_CONNECT_DB_FAIL: "后台忙"
    , CODE_ADD_USER_FAIL: "添加用户失败"
    , CODE_EXISTING_USERNAME: "已存在的用户名"
    , CODE_NON_EXISTS_USER: "不存在的用户"
    , CODE_INVALID_ACTION: "无效的操作"
    , CODE_PWD_ERROR: "密码错误"
    , CODE_EXISTING_NAME: "已存在的名称"
    , CODE_EXCEED_MAX_VALUE: "超过系统允许的最大值"
}

def BuildRepJson(code, message=None):
    if message == None:
        message = MESSAGE_JSON.get(code, "其他错误")
    return {
        "code": code,
        "message": message
    }