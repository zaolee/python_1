from requests import get

websites = [
    "google.com",
    "https://httpstat.us/502",
    "https://httpstat.us/404",
    "https://httpstat.us/300",
    "https://httpstat.us/200",
    "https://httpstat.us/101"
    ]

result = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
        code = get(website).status_code
    if code >=500:
        result[website] = "5## / sever error"    
    elif code >=400:
        result[website] = "4## / client error"
    elif code >=300:
        result[website] = "3## / rediretion"
    elif code >=200:
        result[website] = "2## / successful"    
    elif code >=100:
        result[website] = "1## / informational response"
print(result)




# from requests import get

# websites=[
# "google.com",
# "https://httpstat.us/502",
# "https://httpstat.us/404",
# "https://httpstat.us/300",
# "https://httpstat.us/200",
# "https://httpstat.us/101"
# ]

# results={}

# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#         code = get(website).status_code
#     if code >= 500:
#         results[website] = "5xx / server error"
#     elif code >= 400:
#         results[website] = "4xx / client error"
#     elif code >= 300:
#         results[website] = "3xx / redirection "
#     elif code >= 200:
#         results[website] = "2xx / successful"
#     elif code >= 100:
#         results[website] = "1xx / informational response"

# print(results)



    

