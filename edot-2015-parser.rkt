#lang brag

dictionary : entry+
entry : (form [hom-num] [form] [pos] [etym] usage* sense [phrases])
      | (form [hom-num] [form] [pos] [etym] usage* senses+ [phrases])
      | (form pos [etym] usage* xr)
sense : (usage* def /DOT cit*)
      | sense-num [W+] [newpos] senses+
senses : (sense-num [newpos] usage* def /DOT cit*)
cit : quote [bibl]
form : UPPER-CASE
hom-num : HOM-NUM
def : ( (W | UPPER-CASE)* )
    | xr
quote : ((W | UPPER-CASE | HOM-NUM | DOT)+ (DOT | OTHEREOSMARK)+)+
bibl : BIBL [/DOT]
pos : POS
newpos : POS /CONV
sense-num : SENSE-NUM
xr : /XR W+
usage : USAGE
phrases: /PHRASEMARK  (W|UPPER-CASE)+
etym : ETYM