CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/akellavolk/stepik/web_mailru/ask',
   
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=4',     
        '--timeout=60',
        '--log-level=debug'
        'ask.wsgicd :application',
    ),
}