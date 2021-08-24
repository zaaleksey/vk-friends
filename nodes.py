import json
import os

from json_friends import check_exists_file_and_deleted
from secret import MY_ID


def forming_nodes_into_file():
    path_file = "csv_files/nodes.csv"
    check_exists_file_and_deleted(path_file)

    users_files = os.listdir("users")
    with open(path_file, "w") as nodes_file:
        nodes_file.write("id, label, sex\n")
        nodes_file.write(f"{MY_ID}, ME, 2\n")
        for user_file in users_files:
            with open(f"users/{user_file}", "r") as data_file:
                user = json.load(data_file)
                try:
                    line = f"{user['id']}, {user['first_name']} {user['last_name']}, {user['sex']}\n"
                    nodes_file.write(line)
                except ValueError:
                    print(line)
                    continue


if __name__ == "__main__":
    forming_nodes_into_file()
