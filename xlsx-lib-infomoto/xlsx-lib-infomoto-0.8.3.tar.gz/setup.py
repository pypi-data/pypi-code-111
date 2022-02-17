# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xlsx-lib-infomoto',
 'xlsx-lib-infomoto.xlsx_lib.domain',
 'xlsx-lib-infomoto.xlsx_lib.domain.abs',
 'xlsx-lib-infomoto.xlsx_lib.domain.autodiagnosis',
 'xlsx-lib-infomoto.xlsx_lib.domain.components',
 'xlsx-lib-infomoto.xlsx_lib.domain.distribution',
 'xlsx-lib-infomoto.xlsx_lib.domain.electronic',
 'xlsx-lib-infomoto.xlsx_lib.domain.engine',
 'xlsx-lib-infomoto.xlsx_lib.domain.frame',
 'xlsx-lib-infomoto.xlsx_lib.domain.generic_replacements',
 'xlsx-lib-infomoto.xlsx_lib.domain.hiss_immobilizer',
 'xlsx-lib-infomoto.xlsx_lib.domain.motorcycle_model',
 'xlsx-lib-infomoto.xlsx_lib.domain.power_supply',
 'xlsx-lib-infomoto.xlsx_lib.domain.shared',
 'xlsx-lib-infomoto.xlsx_lib.domain.smart_key',
 'xlsx-lib-infomoto.xlsx_lib.domain.tightening_specifications',
 'xlsx-lib-infomoto.xlsx_lib.domain.xlsx_elements',
 'xlsx-lib-infomoto.xlsx_lib.domain.xlsx_elements.exceptions',
 'xlsx-lib-infomoto.xlsx_lib.modules']

package_data = \
{'': ['*'],
 'xlsx-lib-infomoto': ['.git/*',
                       '.git/hooks/*',
                       '.git/info/*',
                       '.git/logs/*',
                       '.git/logs/refs/heads/*',
                       '.git/logs/refs/remotes/origin/*',
                       '.git/objects/01/*',
                       '.git/objects/02/*',
                       '.git/objects/03/*',
                       '.git/objects/04/*',
                       '.git/objects/05/*',
                       '.git/objects/06/*',
                       '.git/objects/07/*',
                       '.git/objects/08/*',
                       '.git/objects/09/*',
                       '.git/objects/0a/*',
                       '.git/objects/0b/*',
                       '.git/objects/0c/*',
                       '.git/objects/0f/*',
                       '.git/objects/11/*',
                       '.git/objects/12/*',
                       '.git/objects/14/*',
                       '.git/objects/15/*',
                       '.git/objects/16/*',
                       '.git/objects/17/*',
                       '.git/objects/18/*',
                       '.git/objects/19/*',
                       '.git/objects/1a/*',
                       '.git/objects/1b/*',
                       '.git/objects/1d/*',
                       '.git/objects/1e/*',
                       '.git/objects/1f/*',
                       '.git/objects/20/*',
                       '.git/objects/21/*',
                       '.git/objects/22/*',
                       '.git/objects/23/*',
                       '.git/objects/25/*',
                       '.git/objects/26/*',
                       '.git/objects/27/*',
                       '.git/objects/28/*',
                       '.git/objects/29/*',
                       '.git/objects/2b/*',
                       '.git/objects/2c/*',
                       '.git/objects/2d/*',
                       '.git/objects/2e/*',
                       '.git/objects/2f/*',
                       '.git/objects/30/*',
                       '.git/objects/31/*',
                       '.git/objects/32/*',
                       '.git/objects/33/*',
                       '.git/objects/35/*',
                       '.git/objects/36/*',
                       '.git/objects/38/*',
                       '.git/objects/39/*',
                       '.git/objects/3a/*',
                       '.git/objects/3b/*',
                       '.git/objects/3d/*',
                       '.git/objects/3e/*',
                       '.git/objects/3f/*',
                       '.git/objects/40/*',
                       '.git/objects/41/*',
                       '.git/objects/42/*',
                       '.git/objects/43/*',
                       '.git/objects/44/*',
                       '.git/objects/45/*',
                       '.git/objects/46/*',
                       '.git/objects/48/*',
                       '.git/objects/49/*',
                       '.git/objects/4a/*',
                       '.git/objects/4b/*',
                       '.git/objects/4c/*',
                       '.git/objects/4d/*',
                       '.git/objects/4e/*',
                       '.git/objects/4f/*',
                       '.git/objects/50/*',
                       '.git/objects/51/*',
                       '.git/objects/52/*',
                       '.git/objects/53/*',
                       '.git/objects/54/*',
                       '.git/objects/55/*',
                       '.git/objects/56/*',
                       '.git/objects/57/*',
                       '.git/objects/59/*',
                       '.git/objects/5a/*',
                       '.git/objects/5b/*',
                       '.git/objects/5c/*',
                       '.git/objects/5d/*',
                       '.git/objects/5f/*',
                       '.git/objects/60/*',
                       '.git/objects/61/*',
                       '.git/objects/62/*',
                       '.git/objects/63/*',
                       '.git/objects/64/*',
                       '.git/objects/65/*',
                       '.git/objects/67/*',
                       '.git/objects/68/*',
                       '.git/objects/69/*',
                       '.git/objects/6b/*',
                       '.git/objects/6c/*',
                       '.git/objects/6d/*',
                       '.git/objects/6e/*',
                       '.git/objects/6f/*',
                       '.git/objects/70/*',
                       '.git/objects/71/*',
                       '.git/objects/72/*',
                       '.git/objects/73/*',
                       '.git/objects/74/*',
                       '.git/objects/75/*',
                       '.git/objects/76/*',
                       '.git/objects/77/*',
                       '.git/objects/78/*',
                       '.git/objects/79/*',
                       '.git/objects/7b/*',
                       '.git/objects/7c/*',
                       '.git/objects/7d/*',
                       '.git/objects/7e/*',
                       '.git/objects/80/*',
                       '.git/objects/81/*',
                       '.git/objects/82/*',
                       '.git/objects/83/*',
                       '.git/objects/84/*',
                       '.git/objects/87/*',
                       '.git/objects/88/*',
                       '.git/objects/89/*',
                       '.git/objects/8a/*',
                       '.git/objects/8c/*',
                       '.git/objects/8e/*',
                       '.git/objects/8f/*',
                       '.git/objects/90/*',
                       '.git/objects/91/*',
                       '.git/objects/92/*',
                       '.git/objects/93/*',
                       '.git/objects/94/*',
                       '.git/objects/95/*',
                       '.git/objects/96/*',
                       '.git/objects/97/*',
                       '.git/objects/98/*',
                       '.git/objects/99/*',
                       '.git/objects/9a/*',
                       '.git/objects/9b/*',
                       '.git/objects/9c/*',
                       '.git/objects/9d/*',
                       '.git/objects/9e/*',
                       '.git/objects/a0/*',
                       '.git/objects/a1/*',
                       '.git/objects/a2/*',
                       '.git/objects/a3/*',
                       '.git/objects/a4/*',
                       '.git/objects/a6/*',
                       '.git/objects/a7/*',
                       '.git/objects/a8/*',
                       '.git/objects/aa/*',
                       '.git/objects/ac/*',
                       '.git/objects/ad/*',
                       '.git/objects/ae/*',
                       '.git/objects/af/*',
                       '.git/objects/b0/*',
                       '.git/objects/b1/*',
                       '.git/objects/b2/*',
                       '.git/objects/b3/*',
                       '.git/objects/b4/*',
                       '.git/objects/b5/*',
                       '.git/objects/b7/*',
                       '.git/objects/b8/*',
                       '.git/objects/b9/*',
                       '.git/objects/ba/*',
                       '.git/objects/bb/*',
                       '.git/objects/bc/*',
                       '.git/objects/bd/*',
                       '.git/objects/be/*',
                       '.git/objects/c0/*',
                       '.git/objects/c1/*',
                       '.git/objects/c2/*',
                       '.git/objects/c3/*',
                       '.git/objects/c4/*',
                       '.git/objects/c5/*',
                       '.git/objects/c6/*',
                       '.git/objects/c7/*',
                       '.git/objects/c8/*',
                       '.git/objects/c9/*',
                       '.git/objects/ca/*',
                       '.git/objects/cb/*',
                       '.git/objects/cc/*',
                       '.git/objects/cd/*',
                       '.git/objects/ce/*',
                       '.git/objects/cf/*',
                       '.git/objects/d0/*',
                       '.git/objects/d1/*',
                       '.git/objects/d2/*',
                       '.git/objects/d3/*',
                       '.git/objects/d4/*',
                       '.git/objects/d5/*',
                       '.git/objects/d7/*',
                       '.git/objects/d8/*',
                       '.git/objects/d9/*',
                       '.git/objects/da/*',
                       '.git/objects/db/*',
                       '.git/objects/de/*',
                       '.git/objects/df/*',
                       '.git/objects/e0/*',
                       '.git/objects/e1/*',
                       '.git/objects/e3/*',
                       '.git/objects/e5/*',
                       '.git/objects/e6/*',
                       '.git/objects/e7/*',
                       '.git/objects/e8/*',
                       '.git/objects/e9/*',
                       '.git/objects/ea/*',
                       '.git/objects/ec/*',
                       '.git/objects/ed/*',
                       '.git/objects/ee/*',
                       '.git/objects/ef/*',
                       '.git/objects/f0/*',
                       '.git/objects/f1/*',
                       '.git/objects/f2/*',
                       '.git/objects/f3/*',
                       '.git/objects/f4/*',
                       '.git/objects/f5/*',
                       '.git/objects/f6/*',
                       '.git/objects/f7/*',
                       '.git/objects/f8/*',
                       '.git/objects/f9/*',
                       '.git/objects/fa/*',
                       '.git/objects/fb/*',
                       '.git/objects/fc/*',
                       '.git/objects/ff/*',
                       '.git/refs/heads/*',
                       '.git/refs/remotes/origin/*',
                       '.git/refs/tags/*',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11.rar',
                       'xlsx_lib/files/CBR 250 R ´11/*',
                       'xlsx_lib/files/CBR 250 R ´11/FORZA 125 ´15/*',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA ATLANTIC 125 200 ´02.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA BURGMAN AN 400  ´09 ´16.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA CB 1300 ´08.xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA FORZA 125 ´15 .xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA GSX-S 1000 ´15.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA PEGASO 650 ´93 ´00.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/files/FICHA XVS 950 STAR ´14.xlsx',
                       'xlsx_lib/json/146/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/146/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/146/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/146/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/146/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/146/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/146/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/146/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/146/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/146/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/146/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/146/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/146/FORZA 125 ´15.json',
                       'xlsx_lib/json/146/FORZA 125 ´15.json',
                       'xlsx_lib/json/146/FORZA 125 ´15.json',
                       'xlsx_lib/json/146/FORZA 125 ´15.json',
                       'xlsx_lib/json/146/FORZA 125 ´15.json',
                       'xlsx_lib/json/146/FORZA 125 ´15.json',
                       'xlsx_lib/json/146/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/146/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/146/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/146/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/146/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/146/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/146/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/146/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/146/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/146/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/146/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/146/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/146/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/146/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/146/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/146/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/146/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/146/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/681/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/681/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/681/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/681/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/681/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/681/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/681/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/681/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/681/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/681/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/681/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/681/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/681/FORZA 125 ´15.json',
                       'xlsx_lib/json/681/FORZA 125 ´15.json',
                       'xlsx_lib/json/681/FORZA 125 ´15.json',
                       'xlsx_lib/json/681/FORZA 125 ´15.json',
                       'xlsx_lib/json/681/FORZA 125 ´15.json',
                       'xlsx_lib/json/681/FORZA 125 ´15.json',
                       'xlsx_lib/json/681/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/681/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/681/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/681/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/681/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/681/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/681/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/681/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/681/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/681/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/681/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/681/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/681/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/681/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/681/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/681/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/681/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/681/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/773/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/773/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/773/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/773/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/773/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/773/ATLANTIC 125 200 ´02.json',
                       'xlsx_lib/json/773/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/773/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/773/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/773/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/773/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/773/BURGMAN AN 400  ´09 ´16.json',
                       'xlsx_lib/json/773/FORZA 125 ´15.json',
                       'xlsx_lib/json/773/FORZA 125 ´15.json',
                       'xlsx_lib/json/773/FORZA 125 ´15.json',
                       'xlsx_lib/json/773/FORZA 125 ´15.json',
                       'xlsx_lib/json/773/FORZA 125 ´15.json',
                       'xlsx_lib/json/773/FORZA 125 ´15.json',
                       'xlsx_lib/json/773/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/773/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/773/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/773/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/773/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/773/GSX-S 1000 ´15.json',
                       'xlsx_lib/json/773/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/773/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/773/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/773/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/773/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/773/PEGASO 650 ´93 ´00.json',
                       'xlsx_lib/json/773/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/773/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/773/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/773/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/773/XVS 950 STAR ´14.json',
                       'xlsx_lib/json/773/XVS 950 STAR ´14.json']}

install_requires = \
['openpyxl-image-loader>=1.0.5,<2.0.0',
 'openpyxl>=3.0.7,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'python-camel-model-infomoto>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'xlsx-lib-infomoto',
    'version': '0.8.3',
    'description': '',
    'long_description': None,
    'author': 'tomasdarioam',
    'author_email': 'tomasdarioam@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
