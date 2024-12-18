#MatchCaseEx4.py
wkd=input("Enter Week Name:")
if wkd.upper() in ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MON","TUE","WED","THU","FRI","SAT","SUN"]:
    match(wkd[0:3].upper()):
        case "MON" | "TUE" | "WED" | "THU" | "FRI":
            print('{} is Working Day'.format(wkd))
        case "SAT":
            print('{} is Week End'.format(wkd))
        case "SUN":
            print('{} is Holiday'.format(wkd))
else:
    print("{} is not a week day".format(wkd))




