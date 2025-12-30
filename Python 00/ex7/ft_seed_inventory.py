def ft_seed_inventory(a, b, c):
    a = a.capitalize()
    if (c == "area"):
        print(a, "seeds: covers", b, "square meters")
    elif c == "grams":
        print(a, "seeds:", b, c, "total")
    else :
        print(a,"seeds:",b,c,"available")
ft_seed_inventory("tomato", 15, "packets")
