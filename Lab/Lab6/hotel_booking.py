ROOM_RATE = {"standard": 2000, "deluxe": 3500, "suite": 6000}


def booking_cost(room, nights, guests, is_peak_season):
    if room not in ROOM_RATE:
        raise ValueError("unknown room")
    if nights < 1:
        raise ValueError("invalid nights")
    rate = ROOM_RATE[room]
    if is_peak_season:
        rate += rate // 4
    total = rate * nights
    if guests > 2:
        total += (guests - 2) * 500 * nights
    if nights >= 7:
        total -= total // 10
    return total


def cancellation_refund(amount, days_before, is_member):
    if days_before >= 7:
        return amount
    elif days_before >= 2:
        refund = amount // 2
    else:
        refund = 0
    if is_member:
        refund += amount // 4
    return refund


def room_upgrade(room, is_member, rooms_free):
    if rooms_free == 0:
        return room
    if room == "standard" and is_member:
        return "deluxe"
    elif room == "deluxe" and is_member:
        return "suite"
    return room
