#lang br/quicklang

(provide (rename-out [bf-module-begin #%module-begin]))

(require racket/pretty)

(define-macro (bf-module-begin PARSE-TREE)
  #'(#%module-begin
     (display (pretty-format 'PARSE-TREE))))