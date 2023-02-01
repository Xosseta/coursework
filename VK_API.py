import requests
import json


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
        with open("data.json", "w") as write_file:
            json.dump(response, write_file)
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
