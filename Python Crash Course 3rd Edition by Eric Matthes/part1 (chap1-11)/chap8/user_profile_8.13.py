def make_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_info = {}
user_profile = make_profile('john', 'suralta', hobby='coding', grade='college freshman')
print(user_profile)