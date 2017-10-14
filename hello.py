from cgi import parse_qs

def app(environ, start_response):
    """Simplest possible application object"""
    data = parse_qs(environ['QUERY_STRING'])
    print data
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
