#lang brag

dictionary : entry+
entry : form [hom-num] [form] [pos] sense+
sense : (sense-num def /DOT cit*)*
      | (def /DOT cit*)
cit : quote /DOT bibl
form : UPPER-CASE
hom-num : HOM-NUM
def : (W | UPPER-CASE)*
quote : (W | UPPER-CASE)*
bibl : BIBL
pos : POS
sense-num : SENSE-NUM