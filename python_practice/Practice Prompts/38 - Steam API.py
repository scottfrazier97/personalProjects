def steam_api_lookup(appid):

    import requests

    #Return a string with all our information
    response = requests.get(f"https://steamspy.com/api.php?request=appdetails&appid={appid}")

    #Use JSON to convert string above to dictionary, and then print all KEY:VALUE pairs
    for k,v in response.json().items():
        print(k,v)

steam_api_lookup("2807960")