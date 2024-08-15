from urllib.parse import urlparse

class ParameterFeatures:
    def __init__(self,params,url):
        self.params = params
        self.url = url

    def get_params_length(self):
        return len(self.params)
    
    def is_tld_present(self):
        return int(any(tld in self.params for tld in ['.com', '.net', '.org', '.gov', '.edu', '.mil', '.int']))
    
    def params_count(self):
        return len(self.params.split('&')) if self.params else 0