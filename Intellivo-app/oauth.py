import requests

class Oauth(object):
    client_id = "731241371423211550"
    client_secret = "welkyUyKBlTpMltaLzlYv1Og4Ozev5F6"
    scope = "identify%20guilds"
    redirect_uri = "www.intellivo.com/login"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=()&redirect_uri=()&response_type=code&scope=()".format(client_id,redirect_uri)
    discord_token_url = "https://discord.com/api/oauth2/token"

    @staticmethod
    def get_access_token(code)
        payload = {
            'client_id':Oauth.client_id,
            'client_secret':Oauth.client_service,
            'grant_type':"authorization_code"
            'code':code,
            'redirect_uri':Oauth.redirect_uri,
            'scope':Oauth.scope
        }

        headers = {
        'Content-Type' : 'application/x-www-form-urlencoded'
        }

        acceess_token = requests.post(url = Oauth.discord_token_url,data = payload,headers = headers)
        json = acceess_token.json()
        return json.get("acceess_token")

    @staticmethod
    def get_user_json(acceess_token):
        url = Oauth.discord_api_url+"/users/@me"

        headers = {
            "Authoization": "Bearer {}".format(access_token)
        }

        user_object = requests.get(url = url, headers = headers)
        user_json = user_object.json()
        return user_json
