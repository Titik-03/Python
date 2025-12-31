def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "area":
        print(seed_type, "seeds: covers", quantity, "square meters")
    elif unit == "grams":
        print(seed_type, "seeds:", quantity, unit, "total")
    elif unit == "packets":
        print(seed_type, "seeds:", quantity, unit, "available")
    else:
        print("Unknown unit type")
