class FileFeatures:
    def __init__(self,file):
        self.file = file

    def get_file_length(self):
        return len(self.file)