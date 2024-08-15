from src.data_processing.features import Features
from src.data_processing.files_features import FileFeatures

def get_file_property(file)->list:
    feature = Features(file)
    file_feature = FileFeatures(file)
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
        file_feature.get_file_length()
    ]