from requests_html import HTMLSession
import re

BCOLOURS = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
}


def main():
    session = HTMLSession()
    request = session.get('http://restaurant-gioia.sv-restaurant.ch/de/menuplan/')
    menu_elements = request.html.find('#menu-plan-tab1 .item-content')

    menus = []
    for element in menu_elements:
        price = element.find('.menu-prices .price .val')
        description = element.find('.menu-description', first=True).text
        description = (
            map(lambda item: item.strip(),
                filter(lambda item: item not in ['', ',', '\n', 'und'],
                       re.split('(,|\n|und)',
                                description))))

        menus.append({
            'type': element.find('.menuline', first=True).text,
            'title': element.find('.menu-title', first=True).text,
            'description': description,
            'price': {
                'intern': price[0].text,
                'extern': price[1].text,
            }
        })

    texts = []
    for menu in menus:
        delimiter = '\n- '
        description = delimiter + delimiter.join(menu['description'])
        texts.append(
            '{HEADER}{menu[title]}{ENDC}\n'
            '{BOLD}Type:{ENDC} {menu[type]}\n'
            '{BOLD}Description:{ENDC} {description}\n'
            '\n'
            '{OKGREEN}Int: {menu[price][intern]} CHF{ENDC} | '
            'Ext: {menu[price][extern]} CHF'.format(menu=menu, description=description, **BCOLOURS))
    print(('\n\n%s\n\n' % ('-' * 50)).join(texts))
