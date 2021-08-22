import json
from os.path import exists
from time import sleep

import requests

from secret import TOKEN_SERVICE, MY_ID


def get_json_friends_by_id(user_id):
    url = (
        f"https://api.vk.com/method/friends.get?user_id={user_id}&fields=nickname, domain, sex, bdate, city, "
        f"country, timezone, has_mobile, contacts, education, online, relation, last_seen, status, "
        f"can_write_private_message, can_see_all_posts, can_post, universities&access_token={TOKEN_SERVICE}&v=5.131 "
    )
    return requests.get(url).json()


def writing_users_to_file(user):
    filename = f"users/{user['id']}.json"
    if exists(filename):
        return

    with open(filename, "w+") as user_file:
        json.dump(user, user_file, ensure_ascii=True, indent=4)


def save_users_json():
    friends = get_json_friends_by_id(MY_ID)
    counter, total_friends = 0, friends["response"]["count"]
    for friend in friends["response"]["items"]:

        if "deactivated" in friend.keys():
            continue

        if not friend["is_closed"]:
            writing_users_to_file(friend)
            users = get_json_friends_by_id(friend["id"])
            for user in users["response"]["items"]:
                writing_users_to_file(user)
            sleep(0.5)
        counter += 1
        print(
            f"{counter}/{total_friends}: {friend['first_name']} {friend['last_name']}"
        )


if __name__ == "__main__":
    # run once
    save_users_json()
