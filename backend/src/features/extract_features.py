from src.features.extract_url_features import get_url_property
from src.features.extract_domain_features import get_domian_property
from src.features.extract_directory_features import get_directory_property
from src.features.extract_files_features import get_file_property
from src.features.extract_params_features import get_paramater_property
from src.features.extract_special_features import get_special_features

def obtain_features(url,domain,directory,file,params)->list:
    url_features = get_url_property(url)
    domain_features = get_domian_property(domain)
    directory_features = get_directory_property(directory)
    file_features = get_file_property(file)
    params_features = get_paramater_property(params,url)
    special_features = get_special_features(url,domain)
    features = url_features+domain_features+directory_features+file_features+params_features+special_features
    return features
    