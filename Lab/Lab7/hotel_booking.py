
def nights_stayed(days):
    if not isinstance(days, str):
        return None

    try:
        parts = days.split('-')

        if len(parts) != 2:
            return None

        check_in = int(parts[0].strip())
        check_out = int(parts[1].strip())

        if check_in < 1 or check_out < check_in:
            return None

        return check_out - check_in

    except (ValueError, TypeError):
        return None


def room_floor(room_code):
    if not isinstance(room_code, str):
        return None

    try:
        parts = room_code.split('-')

        if len(parts) != 2:
            return None

        prefix = parts[0].strip()
        number = parts[1].strip()

        if not prefix or not number.isdigit():
            return None

        return int(number[0])

    except (ValueError, TypeError):
        return None


def booking_label(names_csv):
    if not isinstance(names_csv, str):
        return "No guests"

    names = [n.strip() for n in names_csv.split(',')]
    names = [n for n in names if n]

    if not names:
        return "No guests"

    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result if result is not None else "Invalid input")

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result if result is not None else "Invalid input")

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)


if __name__ == "__main__":
    main()
