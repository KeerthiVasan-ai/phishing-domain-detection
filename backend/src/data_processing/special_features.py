import time
import whois
from ipwhois import IPWhois
import socket
from datetime import datetime
import requests

class SpecialFeatures:
    def __init__(self,url,domain):
        self.url = url
        self.domain = domain
        self.domain_info = whois.whois(domain)
    
    def time_response(self):
        try:
            start_time = time.time()
            ip = socket.gethostbyname(self.domain)
            return (datetime.now() - start_time).total_seconds()
        except Exception as e:
            return 0

    def domain_spf(self):
        return None

    def asn_ip(self):
        try:
            ip = socket.gethostbyname(self.domain)
            obj = IPWhois(ip)
            results = obj.lookup_rdap(asn_methods=["whois","http"])
            return results["asn"]
        except Exception as e:
            return 0

    def time_domain_activation(self):
        try:
            if isinstance(self.domain_info.creation_date, list):
                self.domain_info.creation_date = self.domain_info.creation_date[0]
            return (datetime.now() - self.domain_info.creation_date).days if self.domain_info.creation_date else None
        except Exception as e:
            return 0

    def time_domain_expiration(self):
        try:
            if isinstance(self.domain_info.expiration_date, list):
                self.domain_info.expiration_date = self.domain_info.expiration_date[0]
            return (self.domain_info.expiration_date - datetime.now()).days if self.domain_info.expiration_date else None
        except Exception as e:
            return 0

    def qty_ip_resolved(self):
        try:
            return len(socket.gethostbyname_ex(self.domain)[2])
        except Exception as e:
            return 0

    def qty_nameservers(self):
        try:
            return len(self.domain_info.name_servers)
        except Exception as e:
            return 0

    def qty_mx_servers(self):
        try:
           return len(self.domain_info.mx) if self.domain_info.mx else None
        except Exception as e:
            return 0

    def ttl_hostname(self):
        return None

    def tls_ssl_certificate(self):
        try:
            return requests.get(self.url).url.startswith('https://')
        except Exception as e:
            return 0

    def qty_redirects(self):
        try:
            response = requests.get(f'http://{self.domain}', timeout=5)
            return len(response.history)
        except Exception as e:
            return 0

    def url_google_index(self):
        try:
            return int("http://www.google.com/search?q=site:" + self.url in requests.get("http://www.google.com/search?q=site:" + self.url).text)
        except Exception as e:
            return 0

    def domain_google_index(self):
        return int("http://www.google.com/search?q=site:" + self.domain in requests.get("http://www.google.com/search?q=site:" + self.domain).text)

    def url_shortened(self):
        try:
            return int(len(self.url) < len(requests.get(self.url).url))
        except Exception as e:
            return 0