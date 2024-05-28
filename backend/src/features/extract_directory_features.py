from src.data_processing.features import Features
from src.data_processing.directory_features import DirectoryFeatures

def get_directory_property(directory)->list:
    feature = Features(directory)
    directory_feature = DirectoryFeatures(directory)
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
        directory_feature.get_domian_length()
    ]