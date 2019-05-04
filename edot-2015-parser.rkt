#lang brag

dictionary : entry+
entry : (form [hom-num] [form] [pos] sense)
      | (form [hom-num] [form] [pos] senses+)
sense: def /DOT cit*
senses : (sense-num def /DOT cit*)
cit : quote bibl
form : UPPER-CASE
hom-num : HOM-NUM
def : (W | UPPER-CASE)*
quote : ((W | UPPER-CASE | DOT)+ (DOT | OTHEREOSMARK)+)+
bibl : BIBL [/DOT]
pos : POS
sense-num : SENSE-NUM