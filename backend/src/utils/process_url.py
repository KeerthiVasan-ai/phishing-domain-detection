from urllib.parse import urlparse

def process_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    directory = parsed_url.path
    file = parsed_url.path.split('/')[-1]
    parameter = parsed_url.query
    return url,domain,directory,file,parameter