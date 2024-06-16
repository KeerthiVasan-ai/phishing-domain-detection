from src.data_processing.features import Features
from src.data_processing.url_features import URLFeatures
import src.utils.constants as constants

def get_url_property(url)->list:
    if url is not None:
        feature = Features(url)
        url_feature = URLFeatures(url)
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
            url_feature.get_tld_count(),
            url_feature.get_length(),
            url_feature.is_email_present()
        ]
    else:
        return constants.NOT_FOUND_CONSTANT * constants.URL_FEATURES