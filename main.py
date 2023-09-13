import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(bitly_key, link):
    url_bitlink = "https://api-ssl.bitly.com/v4/shorten"
    payload = {"long_url": link}
    headers = {"Authorization": bitly_key}
    response = requests.post(url_bitlink, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["id"]


def count_clicks(bitly_key, bitlink):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    payload = {"units": -1, "unit": "month"}
    headers = {"Authorization": bitly_key}
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(bitly_key, bitlink):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    headers = {"Authorization": bitly_key}
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    parser = argparse.ArgumentParser(
        description="Программа помогает сокрашать ссылки а так же получать количество переходов по сокращенной ссылке"
    )
    parser.add_argument("--url", help="Введите ссылку:")
    args = parser.parse_args()
    parsed_url = urlparse(args.url)
    url_without_protocol = f"{parsed_url.netloc}{parsed_url.path}"
    load_dotenv()
    bitly_key = os.environ["BITLY_KEY"]
    try:
        if is_bitlink(bitly_key, url_without_protocol):
            print(count_clicks(bitly_key, url_without_protocol))
        else:
            print(shorten_link(bitly_key, args.url))
    except requests.exceptions.HTTPError as ex:
        print(ex)


if __name__ == "__main__":
    main()
