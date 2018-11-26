def main():
    f = open("members.txt", mode="r") #データの読み込みをする

    text = f.read()

    lines = text.split("\n")

    # for line in lines:
    member = lines

    info = f"{member[0]}{member[1]}"

    print(info)




if __name__ == "__main__":
    main()