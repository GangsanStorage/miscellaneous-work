def draw_christmas_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")

    trunk_spaces = " " * (height - 1)
    print(f"{trunk_spaces}| |")

if __name__ == "__main__":
    tree_height = int(input("크리스마스 트리의 높이를 입력하세요: "))
    draw_christmas_tree(tree_height)