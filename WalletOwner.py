#!/usr/bin/env python
# @aberkman

import requests
from bs4 import BeautifulSoup
from maltego_trx.overlays import OverlayPosition, OverlayType
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import BTCAddress
from maltego_trx.maltego import UIM_PARTIAL

DEF_LABEL = 'Private Wallet'


class WalletOwner(DiscoverableTransform):
    """
    checks the potential ownership of a btc wallet
    via www.vivigle.com
    """

    @classmethod
    def create_entities(cls, request, response):
        addr = request.Value
        label = cls.get_label(addr)
        if label == DEF_LABEL:
            ent = response.addEntity(BTCAddress, addr)
            ent.setBookmark('2')
            return

        ent = response.addEntity(BTCAddress, addr)
        ent.setBookmark('3')
        ent.setNote(label)


    @staticmethod
    def get_label(addr):
        url = f'https://vivigle.com/BitWallet/wallet?address={addr}'
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        titles = soup.find_all('p', class_='wallet-holder')
        return titles[0].text.split('\n')[2]
