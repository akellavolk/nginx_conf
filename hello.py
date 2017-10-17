from cgi import parse_qs

def app(environ, start_response):
    """Simplest possible application object"""
    get_parameters = environ['QUERY_STRING'].split('&')
    body = '\n'.join(get_parameters) + '\n'
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    start_response(status, response_headers)
    return [body]
