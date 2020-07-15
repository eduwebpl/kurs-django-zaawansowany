import grequests

urls = ["http://127.0.0.1:8000/withdraw/" for _ in range(5)]

requests_set = (grequests.post(url, data={"value": 1}) for url in urls)

responses = grequests.map(requests_set)
for response in responses:
    print(f"{response.text} [{response.status_code}]")
