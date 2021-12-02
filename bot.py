import os
if os.path.isfile("E:/project/insta_rally/config/marrharuta_uuid_and_cookie.json"):
    os.remove("E:/project/insta_rally/config/marrharuta_uuid_and_cookie.json")

from instabot import Bot

class InstaHandler:

    def __init__(self, login, password, link):
        self.login = login
        self.password = password

        self.bot = Bot()
        self.log_in()
        self.link = self.bot.get_media_id_from_link(link)

    def delete_cookie(self):
        """
        from inspect import getsourcefile
        from os.path import abspath
        p = abspath(getsourcefile(lambda:0))
        this code returns E:\project\insta_rally\main.py
        :return:
        """
        pass

    def log_in(self):
        self.bot.login(username=self.login, password=self.password)

    def get_my_followers_list(self):
        return self.bot.get_user_followers(self.login) # Список подписчиков

    def get_like(self):
        return self.bot.get_media_likers(self.link)

    def get_comments(self):
        comments = self.bot.get_media_comments_all(self.link)



#
# # def utc_to_local(utc_dt):
# #     return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
#
#
#
# #
# # # user_followers = bot.get_user_followers('marrharuta') # Список подписчиков
# # # user_following = bot.get_user_following('marrharuta') # Список подписок
# #
# # # print(user_followers)
# # # print(user_following)
# #
# # # users = []
# # # for user_id in user_followers:
# # #     users.append(bot.get_username_from_user_id(user_id))
# #
# media_link = 'https://www.instagram.com/p/CMxnxp5Hv6l/'
# media_pk = bot.get_media_id_from_link(media_link)
# # # users_liked = bot.get_media_likers(media_pk)
# # # print(len(users_liked))
# #
# res = bot.get_media_comments_all(media_pk)
# # text = []
# # date = []
# # for line in res:
# #     text.append()
# print(res)


