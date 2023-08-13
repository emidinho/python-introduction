# Prof: I have a good usecase.
# Create a list of names and friends, and then iterate and get them all greeted


friends = ["ewane", "samba", "confy", "marian", "ansible", "paul", "eman", "ralph", "chanelle", "mariia"]

def greetings_for_friends():
    for friend in friends:
        if friend == "marian":
            continue
        elif friend == "chanelle":
            break
        print("hello dearest", friend,"how's the life so far?")
        print("it's been ages since we last talked")
        print("hopefully we meet this summer in paris for some catching up")
        print("i'll be in france during the summer for a conference.")
        print()


greetings_for_friends()