import requests


BaseURL = "https://api.github.com/user/repos"
# # resourceEndPoint = '/user/repos'


sessionManager = requests.Session()
sessionManager.headers = { 'Authorization': 'Bearer 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' }

git_response = sessionManager.get("https://api.github.com/user",)

git_response2 = sessionManager.get(BaseURL)
print(git_response.status_code)

print(git_response2.status_code)

