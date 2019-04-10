#lang racket

; Scrap the Explanatory Dictionary of Tatar (2015-1017) from suzlek.antat.ru

(require net/url)

(define BASE-URL "http://suzlek.antat.ru/fullart.php?id=")
;(define START-ID 183797)
(define START-ID 201561)
(define END-ID 201562)

;(make-directory "edot")
(for ([id (in-range START-ID END-ID)])
  (define idstr (number->string id))
  (define outp (open-output-file (string-append "edot/" idstr ".html")))
  (copy-port (get-pure-port (string->url (string-append BASE-URL idstr))) outp)
  (close-output-port outp)
  (display idstr)
  (newline)
  (sleep (random 1 3)))