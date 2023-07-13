import requests
from bs4 import BeautifulSoup


def connect_to_account():
    session = requests.Session()
    login_url = 'https://twitter.com/i/flow/login'
    request_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    proxies = {'https': '127.0.0.1:2080'}
    response = session.get(login_url, headers=request_header, proxies=proxies)
    soup = BeautifulSoup(response.text, "lxml")
    token = soup.select_one("[name='authenticity_token']")['value']
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
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://twitter.com',
        'referer': 'https://twitter.com/login',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    res = session.post("https://twitter.com/sessions",
                       data=payload, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    for item in soup.select(".tweet-text"):
        print(item.text)

# Account Data :
# username : @josog43667


{"flow_token": "g;168926380412289740:-1689263916859:LfHzi8PDth1bx9MC1I0o6uBr:1", "subtask_inputs": [{"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
    "setting_responses": [{"key": "user_identifier", "response_data": {"text_data": {"result": "josog43667"}}}], "link": "next_link"}}]}
{"flow_token": "g;168926380412289740:-1689263916859:LfHzi8PDth1bx9MC1I0o6uBr:6", "subtask_inputs": [
    {"subtask_id": "LoginEnterPassword", "enter_password": {"password": "ps4plus14", "link": "next_link"}}]}

password = 'ps4plus14'
email = 'josog43667@msback.com'
connect_to_account()
