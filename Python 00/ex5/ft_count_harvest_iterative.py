def ft_count_harvest_recursive():
    a = int(input("Days until harvest: "))
    y = 1
    for i in range(a):
        print("Day ", y)
        y += 1
    print("Harvest time!")