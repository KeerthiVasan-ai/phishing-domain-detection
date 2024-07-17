import time
import dns.resolver 
import whois
import datetime
import requests

class SpecialFeatures:
    def __init__(self,url):
        self.domain = url
    
    def time_response(self):
        try:
            start_time = time.time()
            dns.resolver.resolve(self.domain, 'A')
            end_time = time.time()
            response_time = (end_time - start_time) * 10
            return response_time
        except Exception as e:
            return -1

    def domain_spf(self):
        try:
            answers = dns.resolver.resolve(self.domain, 'TXT')
            for record in answers:
                if 'v=spf1' in str(record):
                    return 1
            return 0
        except Exception as e:
            return -1

    def asn_ip(self):
        try:
            answers = dns.resolver.resolve(self.domain, 'A')
            ip = answers[0].address
            response = requests.get(f'https://api.iptoasn.com/v1/as/ip/{ip}')
            if response.status_code == 200:
                data = response.json()
                return data['as_number']
            return 0
        except Exception as e:
            return -1

    def time_domain_activation(self):
        try:
            domain_info = whois.whois(self.domain)
            if domain_info.creation_date:
                creation_date = domain_info.creation_date
                if isinstance(creation_date, list):
                    creation_date = creation_date[0]
                current_date = datetime.date.today()
                return (current_date - creation_date.date()).days
            return 0
        except Exception as e:
            return -1

    def time_domain_expiration(self):
        try:
            domain_info = whois.whois(self.domain)
            if domain_info.expiration_date:
                expiration_date = domain_info.expiration_date
                if isinstance(expiration_date, list):
                    expiration_date = expiration_date[0]
                current_date = datetime.date.today()
                return (expiration_date.date() - current_date).days
            return 0
        except Exception as e:
            return -1

    def qty_ip_resolved(self):
        try:
            answers = dns.resolver.resolve(self.domain, 'A')
            return len(answers)
        except Exception as e:
            return -1

    def qty_nameservers(self):
        try:
            answers = dns.resolver.resolve(self.domain, 'NS')
            return len(answers)
        except dns.resolver.NoAnswer:
            return 0
        except Exception as e:
            return -1

    def qty_mx_servers(self):
        try:
            answers = dns.resolver.resolve(self.domain, 'MX')
            return len(answers)
        except dns.resolver.NoAnswer:
            return 0
        except Exception as e:
            return -1

    def ttl_hostname(self):
        try:
            answers = dns.resolver.resolve(self.domain, 'A')
            return answers.rrset.ttl
        except Exception as e:
            return -1

    def tls_ssl_certificate(self):
        try:
            response = requests.get(f'https://{self.domain}', timeout=5)
            return 1 if response.status_code == 200 and response.url.startswith('https') else 0
        except Exception as e:
            return -1

    def qty_redirects(self):
        try:
            response = requests.get(f'http://{self.domain}', timeout=5)
            return len(response.history)
        except Exception as e:
            return -1

    def url_google_index(self):
        try:
            response = requests.get(f'https://www.google.com/search?q=site:{self.domain}')
            return 1 if "did not match any documents" not in response.text else 0
        except Exception as e:
            return -1

    def domain_google_index(self):
        return self.url_google_index()

    def url_shortened(self):
        shortened_domains = ['bit.ly', 'goo.gl', 'tinyurl.com', 't.co', 'ow.ly', 'bit.do', 'shorte.st', 'adf.ly']
        try:
            response = requests.head(f'http://{self.domain}', allow_redirects=True, timeout=5)
            final_url = response.url
            for sd in shortened_domains:
                if sd in final_url:
                    return 1
            return 0
        except Exception as e:
            return -1