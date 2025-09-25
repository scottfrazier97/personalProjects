# You’re given a list of log lines, write a function that returns a dictionary of how 
# many times each user logged in.

logs = ["2025-09-20 UserA login", 
        "2025-09-20 UserB logout", 
        "2025-09-20 UserA logout", 
        "2025-09-21 UserC login"]

def login_counter(log_list):

    tracker = {}

    for item in log_list:
        
        log_status = item.split()[2]

        if log_status == "login":

            user = item.split()[1]

            if user in tracker:
                tracker[user] += 1
            else:
                tracker[user] = 1

        else:
            continue

    print(tracker)

login_counter(logs)     
      