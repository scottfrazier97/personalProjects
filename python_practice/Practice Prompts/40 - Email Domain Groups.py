# Given a list of emails, group them by domain name:

def email_domain_grouping(email_list):

    cleaned_list = [str(email).strip() for email in email_list]

    tracker = {}

    for email in cleaned_list:

        domain = email.split("@")[1]

        if domain not in tracker:
            tracker[domain] = []
            tracker[domain].append(email)
        else:
            tracker[domain].append(email)
        
    sorted_tracker = dict(sorted(tracker.items(), key=lambda item: item[0]))

    return sorted_tracker

result = email_domain_grouping(['fake.name@yahoo.com', 'scott.frazier@emailcorp.com', 'luka@mavs.com', 'lebron@yahoo.com'])
{print(f"{k}: {v}") for k,v in result.items()}
