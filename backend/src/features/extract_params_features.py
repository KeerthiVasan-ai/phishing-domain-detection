from src.data_processing.params_features import ParameterFeatures
from src.data_processing.features import Features
import src.utils.constants as constants

def get_paramater_property(parameter,url)->list:
    if parameter is not None:
        feature = Features(parameter)
        params_feature = ParameterFeatures(parameter,url)
        return[
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
            params_feature.get_params_length(),
            params_feature.is_tld_present(),
            params_feature.params_count()
        ]
    else:
        return constants.NOT_FOUND_CONSTANT * constants.PARAMS_FEATURES