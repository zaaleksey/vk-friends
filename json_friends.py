from os import remove
from os.path import exists

import requests

from secret import TOKEN_SERVICE


def get_json_friends_by_id(user_id):
    url = (
        f"https://api.vk.com/method/friends.get?user_id={user_id}&fields=nickname, domain, sex, bdate, city, "
        f"country, timezone, has_mobile, contacts, education, online, relation, last_seen, status, "
        f"can_write_private_message, can_see_all_posts, can_post, universities&access_token={TOKEN_SERVICE}&v=5.131 "
    )
    return requests.get(url).json()


def check_exists_file_and_deleted(path_file):
    if exists(path_file):
        remove(path_file)
