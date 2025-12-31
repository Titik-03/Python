def ft_count_harvest_recursive(nowday=1, a=None):
    if a is None:
        a = int(input("Days until harvest: "))
    if nowday <= a:
        print(f"day {nowday}")
        ft_count_harvest_recursive(nowday + 1, a)
    if nowday == a:
        print("Harvest time!")
