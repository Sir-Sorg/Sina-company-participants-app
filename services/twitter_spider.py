from core import Twitter_Conecction
from core import config

USERNAME = 'josog43667'
EMAIL = 'josog43667@msback.com'
PASSWORD = 'ps4plus14'
config.PROXY = {"http": "127.0.0.1:2080", "https": "127.0.0.1:2080"}

def main():
    user_account = Twitter_Conecction()
    user_account.login(USERNAME, PASSWORD)
    print(user_account.me)
    # print(twitter.get_user_id('elonmusk'))
    # print(twitter.get_user_info('elonmusk'))
    # print(twitter.get_user_data('elonmusk'))
    # print(twitter.get_user_tweets('elonmusk', total=200))
    # print(twitter.get_user_media('elonmusk', total=100))


if __name__ == "__main__":
    main()
