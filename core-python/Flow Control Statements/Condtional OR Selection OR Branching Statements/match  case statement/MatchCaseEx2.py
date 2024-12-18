#MatchCaseEx2.py
wkd=input("Enter Week Name:")
match(wkd.upper()):
    case "MONDAY":
        print('{} is Working Day'.format(wkd))
    case "TUESDAY":
        print('{} is Working Day'.format(wkd))
    case "WEDNESDAY":
        print('{} is Working Day'.format(wkd))
    case "THURSDAY":
        print('{} is Working Day'.format(wkd))
    case "FRIDAY":
        print('{} is Working Day'.format(wkd))
    case "SATURDAY":
        print('{} is Week End'.format(wkd))
    case "SUNDAY":
        print('{} is Holiday'.format(wkd))
    case _:
        print("{} is not week day".format(wkd))

