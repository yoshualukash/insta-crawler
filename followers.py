# Get instance
import instaloader
import json
L = instaloader.Instaloader(max_connection_attempts=0)

# Login or load session
username = ''
password = ''
L.login(username, password)        # (login)


# Obtain profile metadata
instagram_target = ''
profile = instaloader.Profile.from_username(L.context, instagram_target)

follow_list = []
count=1
for follower in profile.get_followers():
    username = follower.username
    follow_list.append(username)
    print(str(count) + ". " + username)
    count = count + 1
follow_list_json = json.dumps(follow_list)
open("list_followers_" + instagram_target +".json","w").write(follow_list_json)
print("selesai")
print("cek file json di file : list_followers_" + instagram_target +".json")
