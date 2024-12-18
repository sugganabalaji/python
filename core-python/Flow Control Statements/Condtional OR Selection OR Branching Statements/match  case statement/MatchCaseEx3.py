#MatchCaseEx3.py
wkd=input("Enter Week Name:")
match(wkd.upper()):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print('{} is Working Day'.format(wkd))
    case "SATURDAY":
        print('{} is Week End'.format(wkd))
    case "SUNDAY":
        print('{} is Holiday'.format(wkd))
    case _:
        print("{} is not week day".format(wkd))

