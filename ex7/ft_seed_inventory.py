def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.upper()

    if unit == "packets" or unit == "grams" or unit == "area":
        print(f"Seed inventory: {seed}, {quantity} {unit}")
    else:
        print("Unknown unit type")

