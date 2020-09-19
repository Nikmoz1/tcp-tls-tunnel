def normalize_headers(headers: dict) -> dict:
    result = {}
    for header in headers:
        if "-" in header:
            key_list = [x.capitalize() for x in header.split("-")]
            key = "-".join(key_list)
            result[key] = headers[header]
        else:
            result[header.capitalize()] = headers[header]
    return result
