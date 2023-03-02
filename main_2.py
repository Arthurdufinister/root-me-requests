from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

url = "http://challenge01.root-me.org/programmation/ch1/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')


indice = soup.find_all('sub')[-1]
indice = indice.string

prem_num = soup.find("sub").find_next_sibling(string=True)
prem_num = prem_num.split("=")
prem_num = prem_num[1]
prem_num = prem_num.split("[")
prem_num = prem_num[1]
prem_num = prem_num.split("+")
prem_num = prem_num[0]
prem_num = prem_num.split(" ")
prem_num = prem_num[1]

deux_num = soup.find("sub", string = "n").find_next_sibling(string=True)
deux_num = deux_num.split("]")
deux_num = deux_num[1]
deux_num = deux_num.split("[")
if deux_num[0] == " - ":
    signe= -1
elif deux_num[0] == " + ":
    signe = 1
deux_num = deux_num[1]
deux_num = deux_num.split("*")
deux_num = deux_num[1]
deux_num = deux_num.split(" ")
deux_num = deux_num[1]

u_0 = soup.find("sub", string = "0").find_next_sibling(string=True)
u_0 = u_0.split('"')
u_0 = u_0[0]
u_0 = u_0.split('=')
u_0 = u_0[1]
u_0 = u_0.split(" ")
u_0 = u_0[1]
nombre = u_0

nombre = int(nombre)	
prem_num = int(prem_num)
deux_num = int(deux_num)
indice = int(indice)
signe = int(signe)


def u_nplus1(Un, indicei):
    return (prem_num + Un) + (signe * (deux_num * indicei))
     

for i in range(indice):
    nombre = u_nplus1(nombre, i)


print(requests.get(f"http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result={nombre}").content)


