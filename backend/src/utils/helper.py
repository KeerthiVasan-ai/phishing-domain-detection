import re

def split_parameters(url):
    url = url.split("?")
    if(len(url) == 2):
        return url[0],url[1]
    else:
        return url[0],None

def split_domain(url):
    url = re.split("/",url,maxsplit=1)
    return url[0],f"/{url[1]}"

def split_directory_and_file(url):
    files = ""
    directory = ""
    append_factor = "/"
    url = re.split("/",url)
    for file in url:
        if file.find(".") != -1:
            files = file
        else:
            directory += f"/{file}"
    if files == "":
        files = url[-1]
        append_factor = ""
        directory = directory.replace(files,"")
    return files,directory[1:]+append_factor