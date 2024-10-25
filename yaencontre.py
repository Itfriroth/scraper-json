import scrapy
import json
from urllib.parse import urlencode
import random

    def start_requests(self):
      dato=["alava-provincia","albacete-provincia","alicante-alacant-provincia","almeria-provincia","corvera-de-asturias-provincia","avila-provincia","badajoz-provincia","balears-illes-provincia","barcelona-provincia","burgos-provincia","cantabria-provincia","castellon-castello-provincia","ceuta-provincia","ciudad-real-provincia","coruna-a-provincia","cuenca-provincia","caceres-provincia","cadiz-provincia","cordoba-provincia","girona-provincia","granada-provincia","guadalajara-provincia","guipuzcoa-provincia","huelva-provincia","huesca-provincia","jaen-provincia","leon-provincia","lleida-provincia","lugo-provincia","melilla-provincia","murcia-provincia","malaga-provincia","navarra-provincia","ourense-provincia","palencia-provincia","palmas-las-provincia","pontevedra-provincia","rioja-la-provincia","salamanca-provincia","santa-cruz-de-tenerife-provincia","segovia-provincia","sevilla-provincia","soria-provincia","tarragona-provincia","teruel-provincia","toledo-provincia","valencia-valencia-provincia","valladolid-provincia","vizcaya-bizkaia-provincia","zamora-provincia","zaragoza-provincia","madrid"]
      for a in dato:
        url=('NameWeb')
        yield scrapy.Request(url=url,callback=self.parse_ya)
    
    def parse_ya(self,response):
        data=response.body
        dat=json.loads(data)
        try:
          rac= dat['result']['totalItems']
        except:
          print("error en rac, parse_ya")
        #print(rac)
        div =rac/45
        if rac > 10000:
          dire=223
        else:
          dire=int(div)+1
        if dire <1:
          dire=1
        for i in range(1,dire+1):
          pag=str(i)
          urll=response.request.url[:-1]
          url=urll+pag
          yield scrapy.Request(url=url,callback=self.parse_arw)
        dato=["alava-provincia","albacete-provincia","alicante-alacant-provincia","almeria-provincia","corvera-de-asturias-provincia","avila-provincia","badajoz-provincia","balears-illes-provincia","barcelona-provincia","burgos-provincia","cantabria-provincia","castellon-castello-provincia","ceuta-provincia","ciudad-real-provincia","coruna-a-provincia","cuenca-provincia","caceres-provincia","cadiz-provincia","cordoba-provincia","girona-provincia","granada-provincia","guadalajara-provincia","guipuzcoa-provincia","huelva-provincia","huesca-provincia","jaen-provincia","leon-provincia","lleida-provincia","lugo-provincia","melilla-provincia","murcia-provincia","malaga-provincia","navarra-provincia","ourense-provincia","palencia-provincia","palmas-las-provincia","pontevedra-provincia","rioja-la-provincia","salamanca-provincia","santa-cruz-de-tenerife-provincia","segovia-provincia","sevilla-provincia","soria-provincia","tarragona-provincia","teruel-provincia","toledo-provincia","valencia-valencia-provincia","valladolid-provincia","vizcaya-bizkaia-provincia","zamora-provincia","zaragoza-provincia","madrid"]
        for i in dato:
          url=('NameWeb')
          yield scrapy.Request(url=url,callback=self.parse_al)

    def parse_al(self,response):
        data=response.body
        dat=json.loads(data)
        try:
          rac= dat['result']['totalItems']
        except:
          print("error en rac, parse_al")
        #print(rac)
        div =rac/45
        if rac > 10000:
          dire=223
        else:
          dire=int(div)+1
        if dire <1:
          dire=1
        for i in range(1,dire+1):
          pag=str(i)
          urll=response.request.url[:-1]
          url=urll+pag
          yield scrapy.Request(url=url,callback=self.parse_alq)

    def parse_alq(self,response):
          data=response.body
          dat=json.loads(data)
          try:
            total= dat['result']['totalItems']
          except:
            print("error en Total, en parse_alq")
          ur="https://www.yaencontre.com"
          cuenta=0
          tit= dat['result']['items']
          for element in tit:
              cuenta+=1
          for i in range(0,cuenta):
            try:
              titulo= dat['result']['items'][i]['realEstate']['title']
            except:
              titulo='Sin datos'
            try:
              precio= dat['result']['items'][i]['realEstate']['price']
            except:
              precio='Sin datos'
            try:
              mtrs2= dat['result']['items'][i]['realEstate']['area']
            except:
              mtrs2='Sin datos'
            try:
              cuartos=dat['result']['items'][i]['realEstate']['rooms']
            except:
              cuartos='Sin datos'
            try:
              banios=dat['result']['items'][i]['realEstate']['bathrooms']
            except:
              banios='Sin datos'
            try:
              operation=dat['result']['items'][i]['realEstate']['operation']
            except:
              operation='Sin datos'
            try:
              url=dat['result']['items'][i]['realEstate']['url']
            except:
              url='Sin datos'
            try:
              urlpropi=dat['result']['items'][i]['realEstate']['owner']['url']
            except:
              urlpropi="Sin datos"
            try:
              propietario=dat['result']['items'][i]['realEstate']['owner']['name']
            except:
              propietario='sin datos'
            try:
              tlfpropietario=dat['result']['items'][i]['realEstate']['owner']['virtualPhoneNumber']
            except:
              tlfpropietario='Sin datos'
            try:
              zone=dat['result']['items'][i]['realEstate']['address']['qualifiedName']
            except:
              zone='Sin datos'
            muni= zone.split(',')
            try:
              municipio=dat['result']['location']
            except:
              municipio='Problema con el municipio'
            try:
              zona=muni[0]+muni[1]
            except:
              zona='Problema con la zona'
            urll=ur+url
            if ("Ático"in titulo)or("ático"in titulo):
              categoria="Atico"
            elif ("Piso"in titulo)or("piso"in titulo):
              categoria="Piso"
            elif ("Dúplex"in titulo)or("dúplex"in titulo):
              categoria="Duplex"
            elif ("Estudio"in titulo)or("estudio"in titulo):
              categoria="Estudio"
            elif ("Casa"in titulo)or("casa"in titulo):
              categoria="Casa o Chalet"
            elif ("Apartamento"in titulo)or("apartamento"in titulo):
              categoria="Apartamento"
            elif ("loft"in titulo)or("Loft"in titulo):
              categoria="Loft"
            else:
              categoria="Sin datos"
            #quitando el IF, quitas el filtro para que solo salgan los particulares
            if "inmobiliarias" in urlpropi:
              pass
            else:
              yield{
                'Categoria':categoria,
                'Banios':banios,
                'Link':urll,
                'Municipio':municipio,
                'Tipo_de_Operacion':operation,
                'Titulo':titulo,
                'Telefono':tlfpropietario,
                'Precio':precio,
                'Metros2': mtrs2,
                'Vendedor':propietario,
                'Habitaciones': cuartos,
                'Zona':zona,
                }
          print(cuenta)

    def parse_arw(self,response):
          data=response.body
          dat=json.loads(data)
          try:
            total= dat['result']['totalItems']
          except:
            print("error en Total, en parse_arw")
          ur="https://www.yaencontre.com"
          cuenta=0
          tit= dat['result']['items']
          for element in tit:
              cuenta+=1
          for i in range(0,cuenta):
            try:
              titulo= dat['result']['items'][i]['realEstate']['title']
            except:
              titulo='Sin datos'
            try:
              precio= dat['result']['items'][i]['realEstate']['price']
            except:
              precio='Sin datos'
            try:
              mtrs2= dat['result']['items'][i]['realEstate']['area']
            except:
              mtrs2='Sin datos'
            try:
              cuartos=dat['result']['items'][i]['realEstate']['rooms']
            except:
              cuartos='Sin datos'
            try:
              banios=dat['result']['items'][i]['realEstate']['bathrooms']
            except:
              banios='Sin datos'
            try:
              operation=dat['result']['items'][i]['realEstate']['operation']
            except:
              operation='Sin datos'
            try:
              url=dat['result']['items'][i]['realEstate']['url']
            except:
              url='Sin datos'
            try:
              urlpropi=dat['result']['items'][i]['realEstate']['owner']['url']
            except:
              urlpropi="Sin datos"
            try:
              propietario=dat['result']['items'][i]['realEstate']['owner']['name']
            except:
              propietario='sin datos'
            try:
              tlfpropietario=dat['result']['items'][i]['realEstate']['owner']['virtualPhoneNumber']
            except:
              tlfpropietario='Sin datos'
            try:
              zone=dat['result']['items'][i]['realEstate']['address']['qualifiedName']
            except:
              zone='Sin datos'
            muni= zone.split(',')
            try:
              municipio=dat['result']['location']
            except:
              municipio='Problema con el municipio'
            try:
              zona=muni[0]+muni[1]
            except:
              zona='Problema con la zona'
            urll=ur+url
            if ("Ático"in titulo)or("ático"in titulo):
              categoria="Atico"
            elif ("Piso"in titulo)or("piso"in titulo):
              categoria="Piso"
            elif ("Dúplex"in titulo)or("dúplex"in titulo):
              categoria="Duplex"
            elif ("Estudio"in titulo)or("estudio"in titulo):
              categoria="Estudio"
            elif ("Casa"in titulo)or("casa"in titulo):
              categoria="Casa o Chalet"
            elif ("Apartamento"in titulo)or("apartamento"in titulo):
              categoria="Apartamento"
            elif ("loft"in titulo)or("Loft"in titulo):
              categoria="Loft"
            else:
              categoria="Sin datos"
            #quitando el IF, quitas el filtro para que solo salgan los particulares
            if "inmobiliarias" in urlpropi:
              pass
            else:
              yield{
                'Categoria':categoria,
                'Banios':banios,
                'Link':urll,
                'Municipio':municipio,
                'Tipo_de_Operacion':operation,
                'Titulo':titulo,
                'Telefono':tlfpropietario,
                'Precio':precio,
                'Metros2': mtrs2,
                'Vendedor':propietario,
                'Habitaciones': cuartos,
                'Zona':zona,
                }
          print(cuenta)
          
