f = open("tree.txt", "r")
lines = f.readlines()


def xmas_tree():
    for line in lines:
        for px in line:
            print(" " if px == " " else "|" if px == "|" else "/" if px == "/" else "\\" if px == "\\" else "" if px == "\n" else "_", end='')
        print("")
    print("Merry Christmas Code Institute")


xmas_tree()