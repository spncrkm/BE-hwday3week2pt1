party_guests = [("Chris", "Top Hat"), ("Victor", "Suit"), ("Kayla", "Bandana"), ("Winter", "Suspenders")]
def add_party_guests(guest):
    
    for person, item in party_guests:
        if guest[1] == item:
            print("Sorry, somebody is already wearing that, please come back with something more unique!")
            return party_guests
    party_guests.append(guest)
    return party_guests

print(add_party_guests(("Ryan", "Onesie")))
print(add_party_guests(("Da'Von", "Birks and Chubbies")))
print(add_party_guests(("Kayla again but cooler", "J's")))
print(add_party_guests(("Caleb", "Lipstick")))
print(add_party_guests(("Brad", "Just a trench coat ༼ つ ◕_◕ ༽つ")))
print(add_party_guests(("Tim", "Top Hat")))