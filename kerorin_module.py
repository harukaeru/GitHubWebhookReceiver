def kerorin_app(_, start_response):
    data = b'<h1>Hello, World! :)</h1>'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
