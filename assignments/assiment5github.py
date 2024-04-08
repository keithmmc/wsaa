from github import Github # module to interact with Github API
from config import config # credentials
import requests # HTTP client library



apikey = config
g = Github(apikey)

#get repo URL
repo = g.get_repo("keithmmc/A-Private_Repo") 

file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url 

ile_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url


response = requests.get(url_of_file)
content_of_file = response.text
#print (contentOfFile)

new_contents = content_of_file.replace("Andrew", "Keith")
#print(new_contents)

github_response=repo.update_file(file_info.path,"file has been updated",
new_contents,file_info.sha)
print (github_response)
