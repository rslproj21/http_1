import requests


def heroes_requests():
    heroes_intelligence = {}
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    all_heroes = response.json()
    for hero in all_heroes:
        if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
            heroes_intelligence[hero['name']] = hero['powerstats']['intelligence']
    print(max(heroes_intelligence, key=heroes_intelligence.get))


if __name__ == '__main__':
    heroes_requests()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Content-type": 'application/json', 'Authorization': f'OAuth {self.token}'}



    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': file_path, 'overwrite': 'true'}
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params=params)
        response = response.json()

        href = response.get("href", "")
        response.put(href, data=open('yandex_disk_task.txt', 'rb'))



if __name__ == '__main__':
    path_to_file = "Yandex_disk_task/hometask_to_yadisk.txt"
    token = input('Введите токен доступа : ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
