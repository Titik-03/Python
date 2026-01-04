def check_temperature(temp_str):
    print("=== Garden Temperature Checker ===")
    try:
        a = int(temp_str)
        if a > 40:
            print(f"Error: {a}°C is too hot for plants (max 40°C)")
        elif a < 0:
            print(f"Error: {a}°C is too cold for plants (min 0°C")
        else:
            print(f"Temperature {a}°C is perfect for plants!")
    except:
        print(f"Error: '{temp_str}' is not a valid number")
    # print("All tests completed - program didn't crash!")

# Testing the function
check_temperature("25")
check_temperature("abc")
check_temperature("100")
check_temperature("-50")
print("All tests completed - program didn't crash!")


