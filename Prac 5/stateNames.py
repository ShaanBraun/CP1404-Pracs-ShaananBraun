"""
CP1404/CP5632 Practical
State names in a dictionary
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

short_state = input("Enter short state: ")
while short_state != "":
    short_state = short_state.upper()
    if short_state in STATE_NAMES:
        print(short_state, "is", STATE_NAMES[short_state])
    else:
        print("Invalid short state")
    short_state = input("Enter short state: ")

for state_name in STATE_NAMES:
    print("{:<4} is {}".format(state_name, STATE_NAMES[state_name]))