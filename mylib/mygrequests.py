# coding=utf8

import grequests
import logging as L

L.basicConfig(level=L.INFO, format='[%(asctime)s] %(levelname)-8s %(message)s')

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]

def callback(r, *args, **kw):
    L.info('FETCH_SUC: %s\t%s' % (r.url, r.status_code))

def exception_handler(request, exception):
    L.info('FETCH_ERR: %s\t%s' % (request.url, exception))

def fetch_urls():
    request_l = [grequests.get(url, verify=False, timeout=3, callback=callback)for url in urls]
    response_l = grequests.map(request_l, size=20, exception_handler=exception_handler)


if __name__ == '__main__':
    fetch_urls()
