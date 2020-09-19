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
