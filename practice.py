prices ={}
while True:
    cmd =input("command(add/show/quit)")
    if cmd == "quit":
        break
    elif cmd =="add":
        name=input("enter fruit name: ")
        price = input("fruit price: ")
        prices[name]=price
        print("added.")
    elif cmd == "show":
        for i in prices:
            print(f"{i}: {prices[i]}")
    else:
        print("unknown command")
