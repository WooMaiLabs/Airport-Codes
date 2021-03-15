wikipedia_urls = {
    'de': 'https://de.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'Liste_der_IATA-Codes%2F{}',
    'el': 'https://el.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          '%CE%9A%CE%B1%CF%84%CE%AC%CE%BB%CE%BF%CE%B3%CE%BF%CF%82_%CE%B1%CE%B5%CF%81%CE%BF%CE%B4%CF%81%CE%BF%CE%BC%CE'
          '%AF%CF%89%CE%BD_%CE%BC%CE%B5_%CE%B2%CE%AC%CF%83%CE%B7_%CF%84%CE%BF%CE%BD_%CE%BA%CF%89%CE%B4%CE%B9%CE%BA%CF'
          '%8C_IATA:_{}',
    'en': 'https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'List_of_airports_by_IATA_airport_code%3A_{}',
    'fa': 'https://fa.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          '%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%81%D8%B1%D9%88%D8%AF%DA%AF%D8%A7%D9%87%E2%80%8C%D9%87%D8%A7_%D8%A8%D8'
          '%B1_%D9%BE%D8%A7%DB%8C%D9%87_%DA%A9%D8%AF_%DB%8C%D8%A7%D8%AA%D8%A7:_{}',
    'fr': 'https://fr.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'Liste_des_codes_AITA_des_a%C3%A9roports%2F{}',
    'hi': 'https://hi.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          '%E0%A4%B5%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4'
          '%B0%E0%A5%8B%E0%A4%82_%E0%A4%95%E0%A5%80_%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A5%80_IATA_%E0%A4%95%E0%A5%8B%E0'
          '%A4%A1_%E0%A4%85%E0%A4%A8%E0%A5%81%E0%A4%B8%E0%A4%BE%E0%A4%B0:_{}',
    'hr': 'https://hr.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'Dodatak:Popis_zra%C4%8Dnih_luka_po_IATA_kodu:_{}',
    'it': 'https://it.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'Codici_aeroportuali_IATA_-_{}',
    'ja': 'https://ja.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'IATA%E7%A9%BA%E6%B8%AF%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E4%B8%80%E8%A6%A7%2F{}',
    'lb': 'https://lb.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'IATA_FluchhafenIndex-{}',
    'nl': 'https://nl.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'Vliegvelden_gesorteerd_naar_IATA-code_{}',
    'pl': 'https://pl.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          'Porty_lotnicze_%C5%9Bwiata:_{}',
    'zh': 'https://zh.wikipedia.org/w/api.php?action=parse&format=json&prop=text&page='
          '%E5%9B%BD%E9%99%85%E8%88%AA%E7%A9%BA%E8%BF%90%E8%BE%93%E5%8D%8F%E4%BC%9A%E6%9C%BA%E5%9C%BA%E4%BB%A3%E7%A0'
          '%81_({})'
}


def get(lang, variant=None):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    urls = []
    for alphabet in alphabets:
        base_url = wikipedia_urls.get(lang, '').strip()
        if variant is not None:
            base_url += '&uselang={}'.format(variant)
        if base_url == '':
            raise ValueError('Invalid Language')
        urls.append(base_url.format(alphabet))
    return urls
