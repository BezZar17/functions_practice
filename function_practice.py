def hello():
    print("What it do?")

def pack(cookies, juice, chips):
    return [cookies, juice, chips]

def eat_lunch(pack):
    if len(pack) == 0:
        print("My lunchbox is empty!! SAD DAYS! :/")
    else:
        for i in range(len(pack)):
            if i == 0:
                print(f"First I eat {pack[0]}")
            else:
                print(f"Next I eat {pack[i]}")

hello()
print(pack("cookies", "juice", "chips"))
eat_lunch(["cookie", "juice", "chips"])
eat_lunch([])