import os
if os.path.isfile("E:/project/insta_rally/config/marrharuta_uuid_and_cookie.json"):
    os.remove("E:/project/insta_rally/config/marrharuta_uuid_and_cookie.json")

from instabot import Bot

from datetime import datetime, timezone


# def utc_to_local(utc_dt):
#     return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


bot = Bot()
# help(bot)
bot.login(username = 'marrharuta',  password = 'rRiTosHa99')
#
# # user_followers = bot.get_user_followers('marrharuta') # Список подписчиков
# # user_following = bot.get_user_following('marrharuta') # Список подписок
#
# # print(user_followers)
# # print(user_following)
#
# # users = []
# # for user_id in user_followers:
# #     users.append(bot.get_username_from_user_id(user_id))
#
media_link = 'https://www.instagram.com/p/CMxnxp5Hv6l/'
media_pk = bot.get_media_id_from_link(media_link)
# # users_liked = bot.get_media_likers(media_pk)
# # print(len(users_liked))
#
res = bot.get_media_comments_all(media_pk)
# text = []
# date = []
# for line in res:
#     text.append()
print(res)


