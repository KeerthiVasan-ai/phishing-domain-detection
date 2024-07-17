import re

def split_parameters(url):
    url = url.split("?")
    if(len(url) == 2):
        return url[0],url[1]
    else:
        return url[0],None

def split_domain(url):
    url = re.split("/",url,maxsplit=1)
    if len(url) != 1:
        return url[0],f"/{url[1]}"
    else:
        return url[0],None

def split_directory_and_file(url):
    files = ""
    directory = ""
    if url is not None:
        url = re.split("/",url)
        for file in url:
            if file.find(".") != -1:
                files = file
            else:
                files = None
                directory += f"/{file}"
        else:
            directory = None

        if files == "":
            files = url[-1]
            if directory is not None:
                directory = directory.replace(files,"")
        else:
            files = None
        return files,directory
    else:
        return None,None