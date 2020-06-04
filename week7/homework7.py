
import json
from json import JSONEncoder
'''
# ex1
family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
"child3" : {
    "name" : "Linus",
    "year" : 2011
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }

}
json.dumps(family,sort_keys=True, indent=4)

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
p=json.loads(sampleJson)
print(p['company']['employee']['payble']['salary'])
'''
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
#     @classmethod
#     def from_json(a, data):
#         return a(**data)
#
#     def __str__(self):
#         return '{}{}{}{}{}'.format(self.name," ",self.engine," ",self.price)
#
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# d=json.dumps(vehicle.__dict__)
# print(d)
#
# class VehlicEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
#
#
# # alternativ tarberak
#
# v = Vehicle("Toyota Rav4", "2.5L", 32000)
# studentJson = json.dumps(v, cls=VehlicEncoder, indent=4)
# print(studentJson)
#
# # 4
# p=Vehicle.from_json(json.loads(d))
# print(type(p))
# print(p)
#



import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()





# for child in root:
#     print (child.tag, child.attrib)
#
# #6
# elemList = []
#
# for elem in tree.iter():
#     elemList.append(elem.tag)
#
# print(elemList)

##7 pordzum em ".//[@year=1992]" tarberak@ chi ashxatum uzum em aranc hstak imanalu te inq@ vori childe-n a gtnem year=1992
# for movie in root.findall("./genre/decade/movie/[year='1992']"):
#     print(movie.attrib)
# #8
#
# a=".//*[@multiple="
# b="'Yes'"
# c="]..."
# d="{}{}{}".format(a,b,c)
# for movie in root.findall(d):
#     print(movie.attrib)


##9
# new_name = root.find(".//*[@title='Back 2 the Future']")
# print(new_name)
# new_name.attrib["title"]="Back to the Future"
# print(new_name.attrib)

# #10
# for check_form in root.findall(".//*format"):
#     if len(check_form.text.split(','))>1:
#         check_form.set('multiple', 'Yes')
#     else:
#         check_form.set('multiple', 'No')

# 11 teri e
i=0
q=0
for decade in root.findall(".//*decade"):
    s=decade.attrib['years'][:-1] #delete last "1980's" <'s>
    print(s)
    s_int=int(s)
    j=0
    for year in decade.findall(".//*year"):
        y_t=year.text
        y_t_int=int(y_t)
        if y_t_int>=s_int and y_t_int<= s_int+9:
            print("yess")
        else:
            a=".//decade[@years='"
            b=y_t+'s'
            c="']"
            h=a+b+c
            dec2000s = root.findall(a+b+c)
             #create new dec
            p1 = root.findall(".//decade/../[@category]")#grnum e te vor category movie a
            l=p1[q].attrib['category'] #
            action = root.find('{}{}{}'.format("./genre/[@category='",l,"']")) #gtnum a movie-n
            if len(dec2000s) == 0:
                new_dec = ET.SubElement(action, 'decade')#nor element vori year-s@ mer es derevs chexacn 2000-n a
                new_dec.attrib["years"] = "" + y_t + "s"
            else:
                new_dec=root.find('{}{}{}{}{}{}'.format("./genre/[@category='", l, "']", "/decade[@years=", "'" + y_t+ "s'", "]"))

            p = root.findall(".//year/..[@title]")
            new_dec.append(p[i]) #avelacnum a movie-n
            print(p[i].attrib)
            dec = root.find('{}{}{}{}{}{}'.format("./genre/[@category='",l,"']","/decade[@years=","'"+s+"s'","]")) #gtnum a sxal graci tex@ ev jnjum

            dec.remove(p[i])

            print(ET.tostring(new_dec, encoding='utf8').decode('utf8'))
            print(ET.tostring(dec, encoding='utf8').decode('utf8'))
            q+=1
        j+=1
        i += 1