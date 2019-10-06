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

following_list = []
count=1
for followee in profile.get_followees():
    username = followee.username
    following_list.append(username)
    print(str(count) + ". " + username)
    count = count + 1
following_list_json = json.dumps(following_list)
open("list_following_" + instagram_target +".json","w").write(following_list_json)
print("selesai")
print("cek file json di file : list_following_" + instagram_target +".json")