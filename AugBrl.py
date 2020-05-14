import requests
import csv
from lxml import html

head = {
    'Host':'br.investing.com',
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'Accept':'text/plain, */*; q=0.01',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'Content-Type':'application/x-www-form-urlencoded',
    'X-Requested-With':'XMLHttpRequest',
    'Content-Length':'181',
    'Origin':'https://br.investing.com',
    'Connection':'keep-alive',
    'Referer':'https://br.investing.com/currencies/ars-brl-historical-data',
    'Cookie': 'adBlockerNewUserDomains=1582923819; _ga=GA1.2.1795690164.1582923826; _fbp=fb.1.1582923827495.1767339498; __gads=ID=f62725cafedfb60d:T=1582923827:S=ALNI_MaTcA43REeyV_onmiNAmD_ymXRFTg; G_ENABLED_IDPS=google; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A6%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%222103%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A32%3A%22D%C3%B3lar+Americano+Real+Brasileiro%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fusd-brl%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A2%3A%2247%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A35%3A%22D%C3%B3lar+Australiano+D%C3%B3lar+Canadense%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Faud-cad%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A21%3A%22Euro+D%C3%B3lar+Americano%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Feur-usd%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2217920%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A16%3A%22%2Findices%2Fbovespa%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%221617%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A20%3A%22Euro+Real+Brasileiro%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Feur-brl%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%221473%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A30%3A%22Peso+Argentino+Real+Brasileiro%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fars-brl%22%3B%7D%7D%7D%7D; r_p_s_n=1; SKpbjs-unifiedid=%7B%22TDID%22%3A%22d430410d-56e7-49b0-a37a-073902154026%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222020-02-28T21%3A04%3A54%22%7D; SKpbjs-unifiedid_last=Tue%2C%2010%20Mar%202020%2016%3A47%3A11%20GMT; SKpbjs-id5id=%7B%22ID5ID%22%3A%22ID5-ZHMOKpBSEzJOgnxK5I01h3MLuHH5IoVTmT8S0reNKg%22%2C%22ID5ID_CREATED_AT%22%3A%222020-03-09T20%3A13%3A10.809Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Afalse%2C%223PIDS%22%3A%5B%5D%7D; SKpbjs-id5id_last=Mon%2C%2009%20Mar%202020%2020%3A13%3A11%20GMT; _gid=GA1.2.1944987953.1583770968; _VT_content_727585_2=1; PHPSESSID=qfasaemc15jhkihumhs50bj2sq; geoC=BR; prebid_page=0; prebid_session=0; gtmFired=OK; StickySession=id.86503289004.491.br.investing.com; GED_PLAYLIST_ACTIVITY=W3sidSI6IjJPMi8iLCJ0c2wiOjE1ODM4NjI2MzQsIm52IjoxLCJ1cHQiOjE1ODM4NjI2MTMsImx0IjoxNTgzODYyNjMxfSx7InUiOiJGK2xxIiwidHNsIjoxNTgzODYyMzQxLCJudiI6MCwidXB0IjoxNTgzODU4ODUzLCJsdCI6MTU4Mzg1ODg4MX1d; nyxDorf=ODxmPTFuMHIxbmtnZCk5MmUzMHU%2FOmZgNjI%3D',
}
data = {
    "curr_id":"1473",
    "smlID":"106819",
    "header":"ARS/BRL+Dados+Históricos",
    "st_date":"01/01/2001",
    "end_date":"01/01/1981",
    "interval_sec":"Daily",
    "sort_col":"date",
    "sort_ord":"ASC",
    "action":"historical_data"
}

page = requests.post('https://br.investing.com/instruments/HistoricalDataAjax', headers=head, data=data)
tree = html.fromstring(page.content)

linha = 0
contador = 1

with open('BancoArsBrl2001a1981.csv', 'w', newline='') as csvfile:
    fieldnames = ['Data', 'Último', 'Abertura', 'Máxima', 'Mínima', 'Variação']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()

    while True:
        try:
            data = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[1]/text()' % contador))[0]
            ultimo = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[2]/text()' % contador))[0]
            abertura = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[3]/text()' % contador))[0]
            maxima = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[4]/text()' % contador))[0]
            minima = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[5]/text()' % contador))[0]
            var = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[6]/text()' % contador))[0]

            
            spamwriter.writerow({'Data': data, 'Último': ultimo, 'Abertura': abertura,'Máxima': maxima, 'Mínima': minima, 'Variação': var})
            
            linha = linha + 1
            contador = contador + 1
            print(data,ultimo,abertura,maxima,minima,var)
            
        except IndexError: 
            break
            
