unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

print("Verifying user:")
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print("\nRemove user:")
deleted_users = ['alice', 'brian']
for del_user in deleted_users:
    if del_user in confirmed_users:
        confirmed_users.remove(del_user)
        print(del_user.title())

