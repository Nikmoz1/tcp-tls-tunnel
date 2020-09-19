def normalize_headers(headers: dict) -> dict:
    normalized_headers = {}
    for header in headers:
        if "-" in header:
            key_list = [x.capitalize() for x in header.split("-")]
            key = "-".join(key_list)
            normalized_headers[key] = headers[header]
        else:
            normalized_headers[header.capitalize()] = headers[header]
    return normalized_headers


g = {
    "ACCEPT": "*/*",
    "Upgrade-insecure-Requests": "1",
    "accept-encoding": "gzip, deflate, br",
    "Extra-Header-1": "test",
    "Cookie": "foo=bar",
    "Host": "www.example.com",
    "referer": "https://www.google.com/",
    "Extra-Header-2": "test",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "<USER_AGENT>",
    "Connection": "keep-alive",
}

print(normalize_headers(g))