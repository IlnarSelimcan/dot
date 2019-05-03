#lang brag

dictionary : entry+
entry : form [hom-num] def /DOT quote /DOT bibl
form : UPPER-CASE
hom-num : HOM-NUM
def : (W | UPPER-CASE)*
quote : (W | UPPER-CASE)*
bibl : BIBL

;entry : headword [ s hom ] ; [ pos ] def [ quote ] [ bibl ]
;headword : "А"
;hom : "I" | "II" | "III" | "IV" | "V"
;pos : "ы." | "и."
;def : sym+ "."
;quote : sym+ "."
;bibl : "Мәдәни җомга" | "һ.Такташ"
;sym : "А" |
;"а" | "ә" | "б" | "в" | "г" | "д" | "е" | "ё" | "ж" | "җ" | "з" | "и" | "й" |
;"к" | "л" | "м" | "н" | "ң" | "о" | "ө" | "п" | "р" | "с" | "т" | "у" | "ү" |
;"ф" | "х" | "ц" | "ч" | "ш" | "щ" | "ъ" | "ы" | "ь" | "э" | "ю" |"я" |
;"–" | "«" |"»" | "," | "-" | " "
;/s : /" "*
