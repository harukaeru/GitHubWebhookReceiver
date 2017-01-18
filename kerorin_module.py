def kerorin_app(_, __):
    data = '<h1>Hello, World! :)</h1>'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
