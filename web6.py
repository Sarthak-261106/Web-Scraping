import requests
user = input('Enter the image name:')

user_agent={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
}

url=f'https://www.google.com/search?q={user}&sca_esv=abca9301b52d9f7f&udm=2&biw=767&bih=730&sxsrf=APpeQns7jwBSxcP1SYmmeTDcw96ejDSDYA%3A1788607691538&ei=y_ybaqO2IJiZseMPlMDP0QI&ved=2ahUKEwjjx-LwqteWAxWYTGwGHRTgMyoQ4dUDegQIBhAN&uact=5&oq=moon&gs_lp=Egtnd3Mtd2l6LWltZyIEbW9vbjIQEAAYgAQYigUYQxixAxiDATIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHkj4CVAAWABwAXgAkAEAmAEAoAEAqgEAuAEDyAEAmAIBoAIHmAMAiAYBkgcBMaAHALIHALgHAMIHAzItMcgHBYAIAQ&sclient=gws-wiz-img'

response = requests.get(url=url , headers=user_agent).content

print(response)