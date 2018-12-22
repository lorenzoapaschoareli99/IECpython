import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

wiki = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil'
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page, 'html5lib')
list_item = soup.find('li', attrs={'class': '<li class="toclevel-1 tocsection-5"><a href="#Capitais_estaduais"><span class="tocnumber">2</span> <span class="toctext">Capitais estaduais</span></a>
<ul>
<li class="toclevel-2 tocsection-6"><a href="#Acre"><span class="tocnumber">2.1</span> <span class="toctext">Acre</span></a></li>
<li class="toclevel-2 tocsection-7"><a href="#Alagoas"><span class="tocnumber">2.2</span> <span class="toctext">Alagoas</span></a></li>
<li class="toclevel-2 tocsection-8"><a href="#Amapá"><span class="tocnumber">2.3</span> <span class="toctext">Amapá</span></a></li>
<li class="toclevel-2 tocsection-9"><a href="#Amazonas"><span class="tocnumber">2.4</span> <span class="toctext">Amazonas</span></a></li>
<li class="toclevel-2 tocsection-10"><a href="#Bahia"><span class="tocnumber">2.5</span> <span class="toctext">Bahia</span></a></li>
<li class="toclevel-2 tocsection-11"><a href="#Ceará"><span class="tocnumber">2.6</span> <span class="toctext">Ceará</span></a></li>
<li class="toclevel-2 tocsection-12"><a href="#Distrito_Federal"><span class="tocnumber">2.7</span> <span class="toctext">Distrito Federal</span></a></li>
<li class="toclevel-2 tocsection-13"><a href="#Espírito_Santo"><span class="tocnumber">2.8</span> <span class="toctext">Espírito Santo</span></a></li>
<li class="toclevel-2 tocsection-14"><a href="#Goiás"><span class="tocnumber">2.9</span> <span class="toctext">Goiás</span></a></li>
<li class="toclevel-2 tocsection-15"><a href="#Maranhão"><span class="tocnumber">2.10</span> <span class="toctext">Maranhão</span></a></li>
<li class="toclevel-2 tocsection-16"><a href="#Mato_Grosso"><span class="tocnumber">2.11</span> <span class="toctext">Mato Grosso</span></a></li>
<li class="toclevel-2 tocsection-17"><a href="#Mato_Grosso_do_Sul"><span class="tocnumber">2.12</span> <span class="toctext">Mato Grosso do Sul</span></a></li>
<li class="toclevel-2 tocsection-18"><a href="#Minas_Gerais"><span class="tocnumber">2.13</span> <span class="toctext">Minas Gerais</span></a></li>
<li class="toclevel-2 tocsection-19"><a href="#Pará"><span class="tocnumber">2.14</span> <span class="toctext">Pará</span></a></li>
<li class="toclevel-2 tocsection-20"><a href="#Paraíba"><span class="tocnumber">2.15</span> <span class="toctext">Paraíba</span></a></li>
<li class="toclevel-2 tocsection-21"><a href="#Paraná"><span class="tocnumber">2.16</span> <span class="toctext">Paraná</span></a></li>
<li class="toclevel-2 tocsection-22"><a href="#Pernambuco"><span class="tocnumber">2.17</span> <span class="toctext">Pernambuco</span></a></li>
<li class="toclevel-2 tocsection-23"><a href="#Piauí"><span class="tocnumber">2.18</span> <span class="toctext">Piauí</span></a></li>
<li class="toclevel-2 tocsection-24"><a href="#Rio_Grande_do_Norte"><span class="tocnumber">2.19</span> <span class="toctext">Rio Grande do Norte</span></a></li>
<li class="toclevel-2 tocsection-25"><a href="#Rio_Grande_do_Sul"><span class="tocnumber">2.20</span> <span class="toctext">Rio Grande do Sul</span></a></li>
<li class="toclevel-2 tocsection-26"><a href="#Rio_de_Janeiro"><span class="tocnumber">2.21</span> <span class="toctext">Rio de Janeiro</span></a></li>
<li class="toclevel-2 tocsection-27"><a href="#Rondônia"><span class="tocnumber">2.22</span> <span class="toctext">Rondônia</span></a></li>
<li class="toclevel-2 tocsection-28"><a href="#Roraima"><span class="tocnumber">2.23</span> <span class="toctext">Roraima</span></a></li>
<li class="toclevel-2 tocsection-29"><a href="#Santa_Catarina"><span class="tocnumber">2.24</span> <span class="toctext">Santa Catarina</span></a></li>
<li class="toclevel-2 tocsection-30"><a href="#São_Paulo"><span class="tocnumber">2.25</span> <span class="toctext">São Paulo</span></a></li>
<li class="toclevel-2 tocsection-31"><a href="#Sergipe"><span class="tocnumber">2.26</span> <span class="toctext">Sergipe</span></a></li>
<li class="toclevel-2 tocsection-32"><a href="#Tocantins"><span class="tocnumber">2.27</span> <span class="toctext">Tocantins</span></a></li>
</ul>
</li>'})
if list_item:
    name = list_item.text.strip()
all_table = soup.find_all('table')
table = soup.find('table', class_='wikitable sortable')
A=[]
B=[]
C=[]
D=[]
E=[]

for row in table.findAll("tr"): #para tudo que estiver em <tr>
    cells = row.findAll('td') #variável para encontrar <td>
    if len(cells)==5: #número de colunas
        A.append(cells[0].find(text=True)) #iterando sobre cada linha
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find('a').text)
        E.append(cells[4].find(text=True))
A=[]
B=[]
C=[]
D=[]
E=[]

df = pd.DataFrame(index=A, columns=['Posição'])

df['Posição']=A
df['Estado']=B
df['Código/IBGE']=C
df['Capital']=D
df['Área']=E

print (df)
