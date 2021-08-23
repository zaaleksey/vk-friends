from time import sleep

from json_friends import get_json_friends_by_id, check_exists_file_and_deleted
from secret import MY_ID


def func():
    path_file = "csv_files/connections.csv"
    check_exists_file_and_deleted(path_file)

    friends = get_json_friends_by_id(MY_ID)
    counter, total_friends = 0, friends["response"]["count"]
    with open(path_file, "w") as connections:
        connections.write("source, target\n")
        for friend in friends["response"]["items"]:

            if "deactivated" in friend.keys():
                continue

            if not friend["is_closed"]:
                connections.write(f"{MY_ID}, {friend['id']}\n")
                users = get_json_friends_by_id(friend["id"])
                for user in users["response"]["items"]:
                    connections.write(f"{friend['id']}, {user['id']}\n")
                sleep(.5)
            counter += 1
            print(
                f"{counter}/{total_friends}: {friend['first_name']} {friend['last_name']}"
            )


if __name__ == "__main__":
    # run once
    func()
