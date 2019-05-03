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
       [(:seq (char-set "IVX")) (token 'HOM-NUM lexeme)]
       [(:+ upper-case) (token 'UPPER-CASE lexeme)]
       [(:+ (:or alphabetic numeric "–" "«" "»" "," "-"))
        (token 'W lexeme)]
       ["." (token 'DOT lexeme)]
       ["Мәдәни җомга" (token 'BIBL lexeme)]))
    (edot-2015-lexer port))
  next-token)
