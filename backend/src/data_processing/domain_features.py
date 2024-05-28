import re

class DomainFeatures:
    def __init__(self,domain)->None:
        self.domain = domain

    def get_vowels_count(self):
        return sum(1 for char in self.domain if char.lower() in 'aeiou')

    def get_domain_length(self):
        return len(self.domain)

    def is_domain_in_ip(self):
        ip_address_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        domain_in_ip = bool(re.match(ip_address_pattern, self.domain))
        if domain_in_ip:
            return 1
        else:
            return 0

    def is_server_or_client_domain(self):
        value = any(keyword in self.domain for keyword in ["server", "client"])
        if value:
            return 1
        else:
            return 0