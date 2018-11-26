import random


def main():
    with open("members.txt", "r") as f:
        members_text = f.read()
        members_lists = members_text.split("\n")  # 縦に名前が表示されるので改行した｡

    for members_list in members_lists:
        members_shuffle = random.choices(members_list)

        print(members_shuffle)


if __name__ == "__main__":
    main()
