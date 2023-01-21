import requests
import TOKENS
import time
import progress.bar


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_foto(self, owner_id, count=5):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': owner_id, 'album_id': 'profile', 'rev': 1, 'count': count, 'extended': 1}
        response = requests.get(url, params={**self.params, **params}).json()
        sizes = ['w', 'z', 'y', 'x', 'm', 's']
        result = {}
        for items in response['response']['items']:
            size_dict = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
            file_url = max(items['sizes'], key=lambda x: size_dict[x["type"]])
            if items['likes']['count'] in result:
                name_id = f'{items["likes"]["count"]},{items["date"]}'
                result.update({name_id: file_url['url']})
            else:
                result.update({items['likes']['count']: file_url['url']})
        return result


class YA:

    def __init__(self, token):
        self.token = token
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def upload_foto(self, path):
        res = vk.users_foto(owner_id)
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        requests.put(f'{url}?path={path}', headers=self.headers)
        bar = progress.bar.IncrementalBar('File upload', max=len(res))
        for foto in res:
            params = {'path': f'{path}/{foto}', 'url': res[foto]}
            status = requests.post(URL, headers=self.headers, params=params).json()
            bar.next()
            time.sleep(1)
        print("\nUpload succes!")


access_token_vk = TOKENS.token_vk
access_token_ya = TOKENS.token_disk
user_id = TOKENS.id
vk = VK(access_token_vk, user_id)
ya = YA(access_token_ya)
owner_id = 150400978
ya.upload_foto(owner_id)
