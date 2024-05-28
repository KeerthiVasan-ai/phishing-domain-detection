class Features:
    def __init__(self,url_part):
        self.url_part = url_part
    
    def get_dot_count(self)->int:
        return self.url_part.count(".")
    
    def get_hypen_count(self)->int:
        return self.url_part.count("-")


    def get_underline_count(self)->int:
        return self.url_part.count("_")
        

    def get_slash_count(self)->int:
        return self.url_part.count("/")
        

    def get_question_mark_count(self)->int:
        return self.url_part.count("?")
        

    def get_equal_count(self)->int:
        return self.url_part.count("=")

    def get_at_count(self)->int:
        return self.url_part.count("@")
        

    def get_and_count(self)->int:
        return self.url_part.count("&")
        

    def get_exclamation_count(self)->int:
        return self.url_part.count("!")
        

    def get_space_count(self)->int:
        return self.url_part.count(" ")
        

    def get_tilde_count(self)->int:
        return self.url_part.count("~")
        

    def get_comma_count(self)->int:
        return self.url_part.count(",")
        

    def get_plus_count(self)->int:
        return self.url_part.count("+")
        

    def get_asterisk_count(self)->int:
        return self.url_part.count("*")
        

    def get_hashtag_count(self)->int:
        return self.url_part.count("#")
        

    def get_dollar_count(self)->int:
        return self.url_part.count("$")
        

    def get_percent_count(self)->int:
        return self.url_part.count("%")