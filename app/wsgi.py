import os
from twitfix import app
from waitress import serve
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

FRONTEND_URL = os.getenv('FRONTEND_URL')

if __name__ == "__main__":
    # listen on 0.0.0.0 to facilitate testing with real services
    serve(
        app,
        url_scheme='https',
        host='0.0.0.0',
        port=8888,
        server_name=FRONTEND_URL,
        trusted_proxy='172.28.0.3',
        log_untrusted_proxy_headers=True,
        trusted_proxy_headers = "forwarded",
        threads=5,
    )
