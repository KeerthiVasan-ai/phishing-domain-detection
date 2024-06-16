from src.data_processing.special_features import SpecialFeatures
import src.utils.constants as constants

def get_special_features(domain)->list:
    if domain is not None:
        print(domain)
        special_features = SpecialFeatures(domain)
        return [
            special_features.time_response(),
            special_features.domain_spf(),
            special_features.asn_ip(),
            special_features.time_domain_activation(),
            special_features.time_domain_expiration(),
            special_features.qty_ip_resolved(),
            special_features.qty_nameservers(),
            special_features.qty_mx_servers(),
            special_features.ttl_hostname(),
            special_features.tls_ssl_certificate(),
            special_features.qty_redirects(),
            special_features.url_google_index(),
            special_features.domain_google_index(),
            special_features.url_shortened(),
        ]
    else:
        return constants.NOT_FOUND_CONSTANT * constants.SPECIAL_FEATURES