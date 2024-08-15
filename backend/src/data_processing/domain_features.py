import re

class DomainFeatures:
    def __init__(self,domain)->None:
        self.domain = domain

    def get_vowels_count(self):
        return sum([self.domain.lower().count(v) for v in 'aeiou'])

    def get_domain_length(self):
        return len(self.domain)

    def is_domain_in_ip(self):
        return int(bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', self.domain)))

    def is_server_or_client_domain(self):
        return int('server' in self.domain or 'client' in self.domain)