import requests
import time
import progress.bar


class YA:

    def __init__(self, token):
        self.token = token
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        requests.put(f'{url}?path={path}', headers=self.headers)

    def upload_foto(self, path, res):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        bar = progress.bar.IncrementalBar('File upload', max=len(res))
        for foto in res:
            params = {'path': f'{path}/{foto}', 'url': res[foto]}
            status = requests.post(url, headers=self.headers, params=params).json()
            bar.next()
            time.sleep(1)
        print("\nUpload succes!")

