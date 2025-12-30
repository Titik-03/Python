def ft_count_harvest_recursive():
    a = int(input("Days until harvest: "))
    
    def count(nowday):
        if nowday > a:
            print("Harvest time!")
            return
        print("Day", nowday)
        count(nowday + 1)
    
    count(1)

ft_count_harvest_recursive()