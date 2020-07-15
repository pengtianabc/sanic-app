test_cnt = 0
def checkcookie(cookie_str):
    global test_cnt
    test_cnt += 1
    if test_cnt%3==0:
        return False
    return True