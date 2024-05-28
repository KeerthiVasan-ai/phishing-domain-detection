import re
from src.utils.helper import split_parameters,split_domain,split_directory_and_file

def process_url(url):
    PROCESSED_URL = re.split("//",url)[1]
    PROCESSED_URL,PARAMETER = split_parameters(PROCESSED_URL)
    DOMAIN,PROCESSED_URL = split_domain(PROCESSED_URL)
    FILES,DIRECTORY = split_directory_and_file(PROCESSED_URL)
    print(f"URL : {url}")
    print(f"DOMAIN : {DOMAIN}")
    print(f"DIRECTORY : {DIRECTORY}")
    print(f"FILES : {FILES}")
    print(f"PARAMETERS : {PARAMETER}")
    return url,DOMAIN,DIRECTORY,FILES,PARAMETER