import random

with open("members.txt", "r") as f:
    members_text = f.read()
    members_list = members_text.split("\n")  # リスト化 & 縦に名前が表示されるので改行した｡

    table1 = []  # members_listを入れるための箱作り
    table2 = []
    table3 = []

    while True:
        members_shuffle = random.choice(members_list)  # ランダムに1人を抽出
        table1.append(members_shuffle)  # リストに上記の1人を入れる
        members_list.remove(members_shuffle)  # removeを使い上記の1人をリストから削除
        if len(table1) == 6:  # テーブルが6人で埋まったら繰り返しをやめるよう指示
            break

    while True:
        members_shuffle = random.choice(members_list)
        table2.append(members_shuffle)
        members_list.remove(members_shuffle)
        if len(table2) == 5:
            break

    while True:
        members_shuffle = random.choice(members_list)
        table3.append(members_shuffle)
        members_list.remove(members_shuffle)
        if len(table3) == 4:
            break

    table_1 = ", ".join(table1)  # join関数を使いリストを文字列に変更
    table_2 = ", ".join(table2)
    table_3 = ", ".join(table3)

    print(f"Table:1 {table_1} \nTable:2 {table_2} \nTable:3 {table_3}")  # まとめてみた｡
