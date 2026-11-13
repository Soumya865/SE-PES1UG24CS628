
from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label


# Test 1: Fuzz testing nights_stayed()
@given(st.one_of(st.text(), st.none()))
def test_nights_stayed_no_crash(s):
    nights_stayed(s)


# Test 2: Fuzz testing room_floor()
@given(st.one_of(st.text(), st.none()))
def test_room_floor_no_crash(s):
    room_floor(s)


# Test 3: Fuzz testing booking_label()
@given(st.one_of(st.text(), st.none()))
def test_booking_label_no_crash(s):
    booking_label(s)
