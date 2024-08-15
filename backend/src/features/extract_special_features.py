import whois
from src.data_processing.special_features import SpecialFeatures

def get_special_features(url,domain)->list:
    
    try:
        domain_info = whois.whois(domain)
        special_features = SpecialFeatures(url,domain)
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
    except Exception:
        return [-1] * 14
    