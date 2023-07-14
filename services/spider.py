import requests
from bs4 import BeautifulSoup


def connect_to_account():

    # Initial session and other parametrs
    session = requests.Session()
    login_url = 'https://twitter.com/i/flow/login'
    request_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    proxies = {'https': '127.0.0.1:2080'}

    # Request Get to find Token
    response = session.get(login_url, headers=request_header, proxies=proxies)
    soup = BeautifulSoup(response.text, "lxml")
    token = soup.select_one("[name='authenticity_token']")['value']

    # Creating Post Request
    payload = {
        'session[username_or_email]': email,
        'session[password]': password,
        'authenticity_token': token,
        'ui_metrics': '{"rf":{"c6fc1daac14ef08ff96ef7aa26f8642a197bfaad9c65746a6592d55075ef01af":3,"a77e6e7ab2880be27e81075edd6cac9c0b749cc266e1cea17ffc9670a9698252":-1,"ad3dbab6c68043a1127defab5b7d37e45d17f56a6997186b3a08a27544b606e8":252,"ac2624a3b325d64286579b4a61dd242539a755a5a7fa508c44eb1c373257d569":-125},"s":"fTQyo6c8mP7d6L8Og_iS8ulzPObBOzl3Jxa2jRwmtbOBJSk4v8ClmBbF9njbZHRLZx0mTAUPsImZ4OnbZV95f-2gD6-03SZZ8buYdTDkwV-xItDu5lBVCQ_EAiv3F5EuTpVl7F52FTIykWowpNIzowvh_bhCM0_6ReTGj6990294mIKUFM_mPHCyZxkIUAtC3dVeYPXff92alrVFdrncrO8VnJHOlm9gnSwTLcbHvvpvC0rvtwapSbTja-cGxhxBdekFhcoFo8edCBiMB9pip-VoquZ-ddbQEbpuzE7xBhyk759yQyN4NmRFwdIjjedWYtFyOiy_XtGLp6zKvMjF8QAAAWE468LY"}',
        'scribe_log': '',
        'redirect_after_login': '',
        'authenticity_token': token,
        'remember_me': 1
    }
    res = session.post(login_url, data=payload, headers=request_header)
    soup = BeautifulSoup(res.text, "lxml")
    for item in soup.select(".tweet-text"):
        print(item.text)


def get_flow_token():
    params = {'flow_name': 'login'}
    payload = {'input_flow_data': {
        'flow_context': {'debug_overrides': {}, 'start_location': {'location': 'manual_link'}, }, },
        'subtask_versions': {'action_list': 2, 'alert_dialog': 1, 'app_download_cta': 1, 'check_logged_in_account': 1,
                             'choice_selection': 3, 'contacts_live_sync_permission_prompt': 0, 'cta': 7, 'email_verification': 2, 'end_flow': 1,
                             'enter_date': 1, 'enter_email': 2, 'enter_password': 5, 'enter_phone': 2, 'enter_recaptcha': 1, 'enter_text': 5,
                             'enter_username': 2, 'generic_urt': 3, 'in_app_notification': 1, 'interest_picker': 3, 'js_instrumentation': 1,
                             'menu_dialog': 1, 'notifications_permission_prompt': 2, 'open_account': 2, 'open_home_timeline': 1, 'open_link': 1,
                             'phone_verification': 4, 'privacy_options': 1, 'security_key': 3, 'select_avatar': 4, 'select_banner': 2,
                             'settings_list': 7, 'show_code': 1, 'sign_up': 2, 'sign_up_review': 4, 'tweet_selection_urt': 1, 'update_users': 1,
                             'upload_media': 1, 'user_recommendations_list': 4, 'user_recommendations_urt': 1, 'wait_spinner': 3, 'web_modal': 1}}
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    proxies = {'https': '127.0.0.1:2080'}
    response = session.post("https://api.twitter.com/1.1/onboarding/task.json",
                            proxies=proxies, headers=headers, params=params, json=payload)
    print(response.text)


get_flow_token()
