def check_connection(username, count_tries, priority):
    if priority >= 10:
        finish = 5
        for attempt in range(1, count_tries + 1):
            if attempt == finish:
                print("Connect was succesfully")
                break
            print(f"Attempt: {attempt} to connect to {username}")
    
    elif priority >= 5 and priority < 10:
        finish = 3
        for attempt in range(1, 6):
            if attempt == finish:
                print("Connect was succesfully")
            print(f"Attempt: {attempt} to connect to {username}")

    else:
        print("Your username has so low priority")

check_connection(priority=100, username="Mike", count_tries=10)