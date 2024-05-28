from urllib.parse import urlparse

class ParameterFeatures:
    def __init__(self,params,url):
        self.params = params
        self.url = url

    def get_params_length(self):
        return len(self.params)
    
    def is_tld_present(self):
        parsed_url = urlparse(self.url)
        domain = parsed_url.netloc.split(".")[-1]
        parameters = self.params.split("&")
        for params in parameters:
            tdl = params.split("=")[1]
            if(tdl == domain):
                return 1
        return 0
    
    def params_count(self):
        parameters = self.params.split("&")
        print(parameters)
        return len(parameters)