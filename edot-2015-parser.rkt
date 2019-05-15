#lang brag

dictionary : entry+
entry : (form [hom-num] [form] [pos] [etym] usage* sense [phrases])
      | (form [hom-num] [form] [pos] [etym] usage* senses+ [phrases])
      | (form pos [etym] xr)
sense: usage* def /DOT cit*
senses : (sense-num [pos /CONV] usage* def /DOT cit*)
cit : quote [bibl]
form : UPPER-CASE
hom-num : HOM-NUM
def : (W | UPPER-CASE)*
quote : ((W | UPPER-CASE | HOM-NUM | DOT)+ (DOT | OTHEREOSMARK)+)+
bibl : BIBL [/DOT]
pos : POS
sense-num : SENSE-NUM
xr : /XR W+
usage : USAGE
phrases: /PHRASEMARK  (W|UPPER-CASE)+
etym : ETYM