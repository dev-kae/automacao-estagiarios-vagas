import requests
from model import Vaga
from typing import List


def search_in_gupy(job_title: str, limit: int):
    opportunities: List[Vaga] = []
    try:
        url = f"https://employability-portal.gupy.io/api/v1/jobs?jobName={job_title}&limit={limit}&offset=0&state=São%20Paulo"

        payload = {}
        headers = {
            "sec-ch-ua-platform": '"Linux"',
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "host": "employability-portal.gupy.io",
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.json()

        for i in response["data"]:
            name = i["name"]
            workplaceType = i["workplaceType"]
            url = i["jobUrl"]
            opportunities.append(
                Vaga(name=name, workplaceType=workplaceType, url=url, plataform="Gupy")
            )
    except Exception as e:
        print(e)
    finally:
        return opportunities


for _ in search_in_gupy("Java JR", limit=10):
    print(f"{_}\n")
