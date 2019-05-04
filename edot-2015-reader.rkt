#lang br/quicklang
(require "edot-2015-parser.rkt")

(define (read-syntax path port)
  (define parse-tree (parse path (make-tokenizer port)))
  (define module-datum `(module bf-mod "edot-2015-expander.rkt"
                          ,parse-tree))
  (datum->syntax #f module-datum))
(provide read-syntax)

(require brag/support)
(define (make-tokenizer port)
  (define (next-token)
    (define edot-2015-lexer
      (lexer
       [(:or whitespace "\n") (token lexeme #:skip? #t)]
       [(:seq (:+ (char-set "IVX")) (:* ",")) (token 'HOM-NUM lexeme)]
       [(:+ (:or upper-case "-")) (token 'UPPER-CASE lexeme)]
       [(:or "а." "бәйл." "бәйл. сүз." "и." "иярт." "кер. сүз" "кис."
             "мод. сүз." "мод. ф." "мөн." "рәв." "с." "сан" "терк." "ф."
             "хәб. сүз" "ы." "энд." "ярд.")
        (token 'POS lexeme)]
       ["." (token 'DOT lexeme)]
       [(:+ (char-set "!?")) (token 'OTHEREOSMARK lexeme)]
       [(:+ (:or alphabetic numeric "–" "«" "»" "," "-" "\u00AD" ":"))
        (token 'W lexeme)]
       [(:or "Мәдәни җомга"
             "Һ.Такташ"
             "Ф.Әмирхан"
             "Г.Ибраһимов"
             "Казан утлары"
             "Г.Шәрипова"
             "Г.Шәрипов"
             "Н.Дәүли")
        (token 'BIBL lexeme)]
       [(:seq (:+ (char-set "0123456789")) ")") (token 'SENSE-NUM lexeme)]))
    (edot-2015-lexer port))
  next-token)
