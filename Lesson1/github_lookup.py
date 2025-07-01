import requests

def fetch_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        print("User not found or error occurred.")
        return

    data = response.json()
    print(f"\n👤 Name: {data.get('name')}")
    print(f"📦 Public Repos: {data.get('public_repos')}")
    print(f"📍 Location: {data.get('location')}")
    print(f"👥 Followers: {data.get('followers')}")


if __name__ == "__main__":
    user = input("Enter GitHub username: ")
    fetch_user_data(user)
