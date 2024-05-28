from urllib.parse import urlparse
import re

class URLFeatures:
    def __init__(self,url)->None:
        self.url = url  

    def get_tld_count(self)->int:
        parsed_url = urlparse(self.url)
        domain = parsed_url.netloc
        return len(domain.split(".")[-1])

    def get_length(self)->int:
        return len(self.url)

    def is_email_present(self)->bool:
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        if re.search(email_pattern, self.url):
            return 1
        else:
            return 0