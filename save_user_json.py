import json
from os.path import exists
from time import sleep

import requests

from secret import TOKEN_SERVICE, MY_ID


def get_json_friends_by_id(user_id):
    url = f"https://api.vk.com/method/friends.get?user_id={user_id}&fields=nickname, domain, sex, bdate, city, " \
          f"country, timezone, has_mobile, contacts, education, online, relation, last_seen, status, " \
          f"can_write_private_message, can_see_all_posts, can_post, universities&access_token={TOKEN_SERVICE}&v=5.131 "
    return requests.get(url).json()


def save_users_json():
    count = 0
    friends = get_json_friends_by_id(MY_ID)
    for friend in friends["response"]["items"]:
        friend_file = open(f"users/{friend['id']}.json", "w+")
        json.dump(friend, friend_file, ensure_ascii=True, indent=4)
        if not friend["is_closed"]:
            users = get_json_friends_by_id(friend["id"])
            for user in users["response"]["items"]:
                if not exists(f"users/{user['id']}.json"):
                    user_file = open(f"users/{user['id']}.json", "w+")
                    json.dump(user, user_file, ensure_ascii=True, indent=4)
            sleep(.5)
        count += 1
        print(f"{count}/{friends['response']['count']}")


if __name__ == '__main__':
    # save_users_json()
    pass
