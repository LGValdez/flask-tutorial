from . import user
USER_LIST = user.USER_LIST

def search_user(username, password):
    uid = 0
    for user in USER_LIST:
        if user.USERNAME == username and user.PASSWORD == password:
            uid = user.ID
            break
    return uid

def get_userdata(user_id):
    user_data = {"name": "Unknown", "mobile": 0}
    for user in USER_LIST:
        if user.ID == int(user_id):
            user_data = {
                "name": user.name,
                "mobile": user.mobile
            }
    return user_data
