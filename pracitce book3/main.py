import urllib.request

header_kodlarim={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116'
    'Safari/537.36'
}
site_adresi=input("Hangi siteye gitmek istiyorsunuz ? : ")
istek=urllib.request.Request(site_adresi,headers=header_kodlarim)
html=urllib.request.urlopen(istek)
print("\nİstediğiniz sitenin kaynak kodu : \n\n")
print(html.read())

