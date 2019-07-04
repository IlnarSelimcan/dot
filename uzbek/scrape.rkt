#lang racket

;; Read Uzbek words from stdin, scrape their wiktionary page if any, save
;; the html page in OUTPUT-DIR and return a machine-readable entry

(require net/url
         html-parsing
         sxml/sxpath)

(module+ test
  (require rackunit))

;;;;;;;;;;;;
;; Constants

(define BASE-URL "https://uz.wiktionary.org/wiki/")
(define OUTPUT-DIR "/tmp/uzb/")
(define REQUEST-HEADERS
  '("User-agent: Mozilla/5.0 (compatible; Taruenbot/0.1; +http://taruen.com/apertiumpp/)"))

;;;;;;;;;;;;;;;;;;;;
;; Data definitions

;; An Entry is SXML
;; interp.: a dictionary entry with as much information about an Uzbek word
;;          as possible, ideally in a format conformant with/convertable to TEI 

;;;;;;;;;;;;
;; Functions

(define (main)
  (begin
    (make-directory OUTPUT-DIR)
    (for ([line (in-lines (current-input-port))])
      (define word (string-downcase (string-trim line)))
      (display (fetch (string-append BASE-URL word)))
      (sleep 0.5))))
;      (define outf
;        (open-output-file
;         (string-append OUTPUT-DIR word ".html")))
;      (copy-port
;       (get-pure-port (string->url (string-append BASE-URL word))
;                      #:redirections 3)
;       outf)
;      (close-output-port outf)

;; String -> SXML
;; given a word, scrape an entry from its wiktionary page
(define (w->e w)
  '())

(module+ test
  (check-equal? 1 1))

;; String -> SXML
;; return contents of a webpage as sxml
(define (fetch url)
  (html->xexp
   (port->string (get-pure-port (string->url url) REQUEST-HEADERS
                                #:redirections 3))))


;(module+ main
;  (main))

;;;;;;;;;;;;
;; Test data

(define A
  '(p
    (b (a (@ (class "mw-selflink selflink")) "a") " I")
    (br)
    "\n"
    (span (@ (style "color:darkgreen")) (i "союз противит." (br) "\n" "разг. "))
    (a (@ (href "/wiki/%D0%B0") (title "а")) "а")
    ", "
    (a (@ (href "/wiki/%D1%82%D0%BE%D0%B3%D0%B4%D0%B0") (title "тогда")) "тогда")
    " "
    (a (@ (href "/wiki/%D0%BA%D0%B0%D0%BA") (title "как")) "как")
    ", "
    (a (@ (href "/wiki/%D0%B2") (title "в")) "в")
    " "
    (a (@ (href "/wiki/%D1%82%D0%BE") (title "то")) "то")
    " "
    (a (@ (href "/wiki/%D0%B2%D1%80%D0%B5%D0%BC%D1%8F") (title "время")) "время")
    " "
    (a (@ (href "/wiki/%D0%BA%D0%B0%D0%BA") (title "как")) "как")
    "; -"
    (b " Xoʻsh, vaʼdang qancha? - Qirq sentnerdan. - A qizlar-chi? - Yuz! ")
    "(Ойбек, «О. в. шабадалар») Ну, каково твоё обязательство? - По сорок центнеров. - А у девушек? - Сто!"
    (br)
    "\n"
    (br)
    "\n"
    (b (a (@ (class "mw-selflink selflink")) "a") " II" (br) "\n")
    (span (@ (style "color:darkgreen")) (i "межд." (br) "\n" (b)))
    (b "1")
    " "
    (span (@ (style "color:darkgreen")) (i "выражает вопрос, удивление и т. п."))
    " "
    (a (@ (href "/wiki/%D0%B0") (title "а")) "а")
    "?, "
    (a (@ (href "/wiki/%D0%B4%D0%B0") (title "да")) "да")
    "?, "
    (a (@ (href "/wiki/%D1%87%D1%82%D0%BE") (title "что")) "что")
    "?; "
    (b "nima deding? a? ")
    "что ты сказал? а?; "
    (b "rostdanmi? a? ")
    "неужели правда?; "
    (b "men ham boraman, a? ")
    "я тоже пойду, да?;"
    (br)
    "\n"
    (b "2 ")
    (span (@ (style "color:darkgreen")) (i "(произносится  протяжно) выражает удивление, догадку "))
    (a (@ (href "/wiki/%D0%B0") (title "а")) "а")
    ", "
    (a (@ (href "/wiki/%D0%B4%D0%B0") (title "да")) "да")
    ", "
    (a (@ (href "/wiki/%D0%B2%D0%BE%D1%82") (title "вот")) "вот")
    " "
    (a (@ (href "/wiki/%D0%BA%D0%B0%D0%BA") (title "как")) "как")
    ", "
    (a (@ (href "/wiki/%D0%B2%D0%BE%D1%82") (title "вот")) "вот")
    " "
    (a (@ (href "/wiki/%D0%BE%D0%BD%D0%BE") (title "оно")) "оно")
    " "
    (a (@ (href "/wiki/%D1%87%D1%82%D0%BE") (title "что")) "что")
    "; "
    (b "a, tushundim  ")
    "а, понял; "
    (b "a, bilaman, bilaman ")
    "а, знаю, знаю."
    (br)
    "\n"))

(define ABJAQ
  '(p
    "◆ "
    (span (@ (style "color:darkgreen")) (b "abjaq:" (br) "\n" "~ boʻlmoq " (span (@ (style "font-size:smaller;")) " " (i " "))))
    " повредиться, поломаться, разбиться, искалечиться; "
    (b "abjagʻi chiqdi ")
    "разбился вдребезги (поломался, разбился, покалечился); "
    (b "etikning abjagʻi chiqdi ")
    "сапоги истрепались; ◆ "
    (span (@ (style "color:darkgreen")) (b "~ qilmoq " (span (@ (style "font-size:smaller;")) " " (i " "))))
    " "
    (span (@ (style "color:darkgreen")) (i "или " (b)))
    (b "abjagʻini chiqarmoq ")
    "повредить, поломать, разбить, искалечить."
    (br)
    "\n"))

(define ABR
  '(p
    (b (a (@ (class "mw-selflink selflink")) "abr") (br) "\n")
    (span (@ (style "color:darkgreen")) (i "уст. книжн. "))
    (a (@ (href "/wiki/%D0%BE%D0%B1%D0%BB%D0%B0%D0%BA%D0%BE") (title "облако")) "облако")
    ", "
    (a (@ (href "/wiki/%D1%82%D1%83%D1%87%D0%B0") (title "туча")) "туча")
    "; ◆ "
    (span (@ (style "color:darkgreen")) (b "~i navbahor " (span (@ (style "font-size:smaller;")) " " (i " "))))
    " весенняя туча; весенние облака."
    (br)
    "\n"))