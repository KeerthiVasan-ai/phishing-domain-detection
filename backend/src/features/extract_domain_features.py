from src.data_processing.features import Features
from src.data_processing.domain_features import DomainFeatures

def get_domian_property(domain)->list:
    feature = Features(domain)
    domain_feature = DomainFeatures(domain)
    return [
        feature.get_dot_count(),
        feature.get_hypen_count(),
        feature.get_underline_count(),
        feature.get_slash_count(),
        feature.get_question_mark_count(),
        feature.get_equal_count(),
        feature.get_at_count(),
        feature.get_and_count(),
        feature.get_exclamation_count(),
        feature.get_space_count(),
        feature.get_tilde_count(),
        feature.get_comma_count(),
        feature.get_plus_count(),
        feature.get_asterisk_count(),
        feature.get_hashtag_count(),
        feature.get_dollar_count(),
        feature.get_percent_count(),
        domain_feature.get_vowels_count(),
        domain_feature.get_domain_length(),
        domain_feature.is_domain_in_ip(),
        domain_feature.is_server_or_client_domain()
    ]