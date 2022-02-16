import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse


def shorten_link(headers, long_url):

    body = {
        "long_url": long_url
    }

    response = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks",
        headers=headers,
        json=body)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def count_clicks(headers, bitlink):

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
        headers=headers)

    response.raise_for_status()
    clicks_count = response.json()["total_clicks"]
    return clicks_count


def is_bitlink(url, headers):

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{url}",
        headers=headers)
    return response.ok


def main():
    load_dotenv()

    token = os.environ['BITLY_TOKEN']

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Ссылка будет сокращена")
    args = parser.parse_args()

    full_url = args.url
    url_parse = urlparse(full_url)
    url = url_parse.netloc + url_parse.path

    headers = {
        "Authorization": token
    }

    if is_bitlink(url, headers):
        try:
            print("Количество кликов = ", count_clicks(headers, url))
        except requests.exceptions.HTTPError:
            print("Невозможно посчитать количество кликов")

    else:
        try:
            print("Битлинк: ", shorten_link(headers, full_url))
        except requests.exceptions.HTTPError:
            print("Ссылка введена неверно")


if __name__ == '__main__':

    main()
