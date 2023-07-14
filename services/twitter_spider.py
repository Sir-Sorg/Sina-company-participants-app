from .core import Twitter_Conecction
from .core import config

USERNAME = 'josog43667'
EMAIL = 'josog43667@msback.com'
PASSWORD = 'ps4plus14'
config.PROXY = {"http": "26.26.26.1:10809", }
ACCOUNT = Twitter_Conecction()


def main():
    ACCOUNT.login(USERNAME, PASSWORD)
    print(ACCOUNT.me)
    # print(twitter.get_user_id('elonmusk'))
    # print(twitter.get_user_info('elonmusk'))
    # print(twitter.get_user_data('elonmusk'))
    # print(twitter.get_user_tweets('elonmusk', total=200))
    # print(twitter.get_user_media('elonmusk', total=100))


if __name__ == "__main__":
    main()
