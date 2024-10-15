import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

os.system("title WebCloner Revenant Leakers")

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_website(url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for img in soup.find_all('img'):
        img_url = img['src']
        if not img_url.startswith('http'):
            img_url = urljoin(url, img_url)
        response = requests.get(img_url)
        img_filename = sanitize_filename(img_url.split('/')[-1])
        with open(os.path.join(output_dir, img_filename), 'wb') as f:
            f.write(response.content)

    for link in soup.find_all('link'):
        if 'stylesheet' in link.get('rel', []):
            css_url = link['href']
            if not css_url.startswith('http'):
                css_url = urljoin(url, css_url)
            response = requests.get(css_url)
            css_filename = sanitize_filename(css_url.split('/')[-1])
            with open(os.path.join(output_dir, css_filename), 'wb') as f:
                f.write(response.content)

    for script in soup.find_all('script'):
        if script.get('src'):
            js_url = script['src']
            if not js_url.startswith('http'):
                js_url = urljoin(url, js_url)
            response = requests.get(js_url)
            js_filename = sanitize_filename(js_url.split('/')[-1])
            with open(os.path.join(output_dir, js_filename), 'wb') as f:
                f.write(response.content)

    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        for img in soup.find_all('img'):
            img_url = img['src']
            if not img_url.startswith('http'):
                img_url = sanitize_filename(img_url.split('/')[-1])
            img['src'] = img_url

        for link in soup.find_all('link'):
            if 'stylesheet' in link.get('rel', []):
                css_url = link['href']
                if not css_url.startswith('http'):
                    css_url = sanitize_filename(css_url.split('/')[-1])
                link['href'] = css_url

        for script in soup.find_all('script'):
            if script.get('src'):
                js_url = script['src']
                if not js_url.startswith('http'):
                    js_url = sanitize_filename(js_url.split('/')[-1])
                script['src'] = js_url

        f.write(soup.prettify())

print("""\033[32m ▄█     █▄     ▄████████ ▀█████████▄   ▄████████  ▄█        ▄██████▄  ███▄▄▄▄      ▄████████    ▄████████ 
███     ███   ███    ███   ███    ███ ███    ███ ███       ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ 
███     ███   ███    █▀    ███    ███ ███    █▀  ███       ███    ███ ███   ███   ███    █▀    ███    ███ 
███     ███  ▄███▄▄▄      ▄███▄▄▄██▀  ███        ███       ███    ███ ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ███        ███       ███    ███ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███     ███   ███    █▄    ███    ██▄ ███    █▄  ███       ███    ███ ███   ███   ███    █▄  ▀███████████ 
███ ▄█▄ ███   ███    ███   ███    ███ ███    ███ ███▌    ▄ ███    ███ ███   ███   ███    ███   ███    ███ 
 ▀███▀███▀    ██████████ ▄█████████▀  ████████▀  █████▄▄██  ▀██████▀   ▀█   █▀    ██████████   ███    ███ 
                                                 ▀                                             ███    ███\033[92m
                      
                      
                                                                             \033[90mMade by TheDemon
                                                                             https://discord.gg/2Kt68GceF9\033[90m
                       """)


url = input("""\033[91m --> Enter the site URL: \033[0m""")

output_dir = input("""
\033[91m --> Enter the output directory: \033[0m""")

download_website(url, output_dir)

print("""
\033[0m\033[92mSite cloned successfully\033[0m""")

input("\n\033[91mPress any key to exit...\033[0m")
