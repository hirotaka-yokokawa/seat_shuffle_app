import random


def main():
    f = open("members.txt", mode="r")  # データの読み込みをする

    text = f.read()

    lines = text.split("\n")  # 縦に名前が表示されるので改行した｡

    for line in lines:
        print(line)






        f.close()


if __name__ == "__main__":
    main()
