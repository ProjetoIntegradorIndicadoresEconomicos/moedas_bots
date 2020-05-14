import requests
import csv
from lxml import html

head = {
    "Host":"br.investing.com",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept":"text/plain, */*; q=0.01",
    "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate, br",
    "Content-Type":"application/x-www-form-urlencoded",
    "X-Requested-With":"XMLHttpRequest",
    "Content-Length":"178",
    "Origin":"https://br.investing.com",
    "Connection":"keep-alive",
    "Referer":"https://br.investing.com/currencies/eur-usd-historical-data",
    "Cookie":"SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A3%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A21%3A%22Euro+D%C3%B3lar+Americano%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Feur-usd%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%223%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A30%3A%22D%C3%B3lar+Americano+Iene+Japon%C3%AAs%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fusd-jpy%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%222103%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A32%3A%22D%C3%B3lar+Americano+Real+Brasileiro%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fusd-brl%22%3B%7D%7D%7D%7D; adBlockerNewUserDomains=1582818507; _ga=GA1.2.2000824011.1582818512; _fbp=fb.1.1582818512792.1701084206; G_ENABLED_IDPS=google; __gads=ID=36787e2bf3bf4ed1:T=1582818515:S=ALNI_MY3VdOEfozaa8o5uJfacgBFF_wJlg; SKpbjs-unifiedid=%7B%22TDID%22%3A%2200dce2e5-6622-4241-b0f0-4984765bb851%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222020-02-27T15%3A48%3A49%22%7D; SKpbjs-unifiedid_last=Mon%2C%2009%20Mar%202020%2016%3A27%3A46%20GMT; SKpbjs-id5id=%7B%22ID5ID%22%3A%22ID5-ZHMO2dJCWThyhWR25YeV7pRUqpG32rCWbSOHqB4Vrw%22%2C%22ID5ID_CREATED_AT%22%3A%222020-02-27T15%3A48%3A49.732Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Atrue%2C%223PIDS%22%3A%5B%5D%7D; SKpbjs-id5id_last=Fri%2C%2006%20Mar%202020%2014%3A08%3A37%20GMT; r_p_s_n=1; PHPSESSID=63djrcjp45t410j52glgatmv0g; geoC=BR; prebid_page=0; prebid_session=1; gtmFired=OK; nyxDorf=NjI2YjVqPnxiPWxmZClmZWIwNmkzKjo8NDI%3D; StickySession=id.41148115040.412.br.investing.com; _gid=GA1.2.1396996193.1583771245; GED_PLAYLIST_ACTIVITY=W3sidSI6IkYrbHEiLCJ0c2wiOjE1ODM3NzEzOTAsIm52IjoxLCJ1cHQiOjE1ODM3NzEyNzIsImx0IjoxNTgzNzcxMzg5fV0.",    
}
data = {
    "curr_id":"1",
    "smlID":"106682",
    "header":"EUR/USD+Dados+Históricos",
    "st_date":"30/12/1962", 
    "end_date":"30/12/1981",
    "interval_sec":"Daily",
    "sort_col":"date",
    "sort_ord":"DESC",
    "action":"historical_data",
}

page = requests.post('https://br.investing.com/instruments/HistoricalDataAjax', headers=head, data=data)
tree = html.fromstring(page.content)

linha = 0
contador = 1

with open('bancoEuraDol1981a1962.csv', 'w', newline='') as csvfile:
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

            spamwriter.writerow({'Data': data, 'Último': ultimo, 'Abertura': abertura, 'Máxima': maxima, 'Mínima': minima, 'Variação': var})

            print (data,ultimo,abertura,maxima,minima,var)
            linha = linha + 1
            contador = contador + 1
        except IndexError: # Se não houver mais dados para minerar
            break
            
