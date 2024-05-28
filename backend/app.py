from src.features.extract_features import obtain_features
from src.utils.process_url import process_url

URL = "https://www.example.com/examples/index.php?q=400&s=10000"

URL,DOMAIN,DIRECTORY,FILES,PARAMETER = process_url(URL)
features = obtain_features(URL,DOMAIN,DIRECTORY,FILES,PARAMETER)

# TODO: DEVELOP A FLASK APP