def get_input():
    print("Please enter data:")
    rows = []
    while True:
        line = input()
        if line:
            rows.append(line)
        else:
            break
    return rows
