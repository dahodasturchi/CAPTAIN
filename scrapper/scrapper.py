import requests as r




def paster(putting):
    str(putting)
    data = {"content": putting, "syntax": "python", "expiry_days": 1}
    headers = {"User-Agent": "My Python Project"}
    result = r.post("https://dpaste.com/api/", data=data, headers=headers)
    #print(f"URL: {r.text}")
    return result.text


def screen(url):
    BASE = f'https://render-tron.appspot.com/screenshot/https://{url}'

    response = r.get(BASE, stream=True)
    #print(f'{response.status_code}')
    if response.status_code == 200:
        with open('screen.jpg','wb') as file:
            for result in response:
                file.write(result)
            file.close()

        return True
    else:
        return False






















