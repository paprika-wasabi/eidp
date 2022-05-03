from datetime import datetime
result = []
i = int(input())
assert(i) >= 1
assert(i) <= 100000
for k in range(i):
    emt = input()
    d = datetime.strptime(input(), "%d %m %Y")
    wd = datetime.strptime(input(), "%d %m %Y")
    age = d.year - wd.year - \
        ((d.month, d.day) < (wd.month, wd.day))
    if d < wd: result.append("Person #" + str(k + 1) + ": Ungueltiges Geburtsdatum")
    elif age > 130: result.append("Person #" + str(k + 1) + ": Zu alt")
    else: result.append("Person #" + str(k + 1) + ": " + str(age))
    # j = d.year - wd.year
    # dif = d - wd
    # dif_year = dif.days / 365
    # if dif.days == 366 or dif.days == 365:
    #     age = 1
    # else:
    #     age = j - ((d.month, d.day) <= (wd.month, wd.day))
    # if wd.date() <= d.date():
    #     if wd.date() == d.date():
    #         result.append("Person #" + str(k + 1) + ": " + str(0))
    #     elif j > 130:
    #         result.append("Person #" + str(k + 1) + ": Zu alt")
    #     elif dif.days <= 365:
    #         result.append("Person #" + str(k + 1) + ": " + str(0))
    #     else:
    #         result.append("Person #" + str(k + 1) + ": " + str(age))
    # else:
    #     result.append("Person #" + str(k + 1) + ": Ungueltiges Geburtsdatum")
for x in result:
    print(x)