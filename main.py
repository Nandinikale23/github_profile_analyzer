
import requests
import matplotlib.pyplot as plt

#enter github username
username = input("Enter GitHub username: ")

#GitHub user profile API
profile_url = f"https://api.github.com/users/{username}"
profile_response = requests.get(profile_url)

#check user exists
if profile_response.status_code != 200:
    print("❌ GitHub user not found")
    exit()

profile_data = profile_response.json()

#basic profile info print 
print("\n📌 GitHub Profile Info")
print("Name:", profile_data.get("name"))
print("Public Repositories:", profile_data.get("public_repos"))
print("Followers:", profile_data.get("followers"))
print("Following:", profile_data.get("following"))

#repositories API
repos_url = f"https://api.github.com/users/{username}/repos"
repos_response = requests.get(repos_url)
repos_data = repos_response.json()

#language count dictionary
language_count = {}

for repo in repos_data:
    lang = repo["language"]
    if lang:
        if lang in language_count:
            language_count[lang] += 1
        else:
            language_count[lang] = 1

print("\n📊 Languages Used:")
for lang, count in language_count.items():
    print(lang, ":", count)

#graph draw करणे
if language_count:
    languages = list(language_count.keys())
    counts = list(language_count.values())

    plt.bar(languages, counts)
    plt.xlabel("Programming Languages")
    plt.ylabel("Number of Repositories")
    plt.title("GitHub Language Usage")
    plt.show()
else:
    print("No language data found")
