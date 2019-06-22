## A script which helps to label words from a paper dictionary with categories
## of an HFST/LEXC-based morphological transducer.
##
## Given a text file with a dictionary, where each line is of the following
## form:
##
## [CommaSeparatedLabels] \tab entryWord \tab restOfTheEntry
##
## for example:
##
## CC	А	I союз противит разг а, тогда как, в то время как — Хуш, ваъданг канча3— Кирк центнер дан — А кизлар-чи3 —Юз» (Ойбек «О в шаба халар») Ну, каково тво обяз I тельство3— По сорок центнеров — А у девушек3— Сто*
## IJ	А	II межд 1, вырсжает вопрос удивление и т п Р, да3, что3, ними дединг? а3 что ты сказал3 а3 ростданми’ а3 неужели правда3 мен хам бораман, а3 я тоже пойду, да3 2 (произносится протяжно) выражает удивление, до гадку а, да, вот как, вот оно что, а, тушундим а, пончл а, биламан, биламан а, зияю знаю
## N1,ADV	АБАД	вечность; // навеки то ~ поэт навеки навсегда на вечные времена на веки вечные
##
## or
##
## АБАДИЙ	вечный, // вечно навеки навечно, навсегда -шуҳрат вечная слава ~ равишда, ~ суратда навеки, на всегда, ~ колдирмок оставлять навеки увековечивать
##
## that is just the entry word + the rest of the entry
##
## iterates over the lines of the file, taking the next unlabeled line,
## suggesting a label for it, asking for feedback, re-training the classifier
## and saving the state after feedback received for BATCH_SIZE entries,
## taking the next unlabeled line, and so on.
##
## TODO support multilabel classification for real

from collections import namedtuple
import pickle, sys, os.path, nltk


############
## Constants


## http://users.umiacs.umd.edu/~hal/megam/
PATH_TO_MEGAM_BINARY = "/home/selimcan/local/megam-64"
nltk.classify.megam.config_megam(PATH_TO_MEGAM_BINARY)

## model gets retrained after feedback for BATCH_SIZE entries is provided
BATCH_SIZE = 10

BACKUP = "ws.pickle"

DICTIONARY = sys.argv[1]

###################
## Data definitions


WS = namedtuple('WS', ['model', 'done', 'todo'])
## WorldState is WS(nltk.classify.ClassifierI, (listof Entry), (listof Entry)
## interpretation: classfier, labeled entries, unlabeled entries

## Entry is (tupleof Label, String, String)
## interpretation: an entry of a monolingual dictionary with a label,
##                 entry word, and the rest of the entry (with translations
##                 or definitinos)

## Label is String or False
## interpretation: if String - category in the transducer, if False - not set


############
## Functions


def main2(ws, memorized):
    """ WS -> WS 

    Train a classifier based on labeled entries in ws0.done, and iterate over
    unlabeled entries in ws0.todo, asking the user for feedback and re-training
    the model each time such feedback is provided.
    """

    if memorized == 0 or memorized == BATCH_SIZE:
        memorized = 0
        train_data = []
        for label, word, rest in ws.done:
            train_data.append((word_rest2featvec(word, rest), label))
        model = nltk.classify.MaxentClassifier.train(train_data,
                                                          algorithm='megam',
                                                          trace=0, max_iter=15)
        with open(BACKUP, 'wb') as outf:
            pickle.dump(ws, outf)
    else:
        model = ws.model

    _, word, rest = ws.todo[0]
    guess = model.classify(word_rest2featvec(word, rest))
    print(guess, word, rest, sep='\t')
    feedback = input("\n'ok' if guessed label correct, else correct label or 's' to skip: ")
    if feedback.lower() == 'ok':
        main2(WS(model, ws.done + [(guess, word, rest)], ws.todo[1:]), memorized+1)
    elif feedback.lower() == 's':
        main2(WS(model, ws.done, ws.todo[1:]), memorized)
    else:
        main2(WS(model, ws.done + [(feedback.upper(), word, rest)], ws.todo[1:]), memorized+1)

def word_rest2featvec(word, rest):
    """String String -> dictionary String->String)

    Given entry word, and the rest of the entry, return feature vector."""
    fv = {'len': str(len(word)), 
          'pre1': word[:1], 'pre2': word[:2], 'pre3': word[:3], 
          'pre4': word[:4], 'pre5': word[:5], 
          'suf1': word[-1:],'suf2': word[-2:], 'suf3': word[-3:], 
          'suf4': word[-4:], 'suf5': word[-5:], 
          'contains-': '-' in word} 
    for w in rest.split(): 
        fv[w] = True
        fv[w[-3:]] = True 
    for ngram in char_ngrams(rest, 5): 
        fv[ngram] = True 
    return fv

def char_ngrams(s, n):
    """String -> (listof String)

    Return character n-grams from s."""
    return [s[i:i+n] for i in range(len(s)-n+1)]

if __name__ == '__main__':
    if os.path.isfile(BACKUP):
        with open(BACKUP, 'rb') as bf:
            ws0 = pickle.load(bf)
    else:
        with open(DICTIONARY) as inf:
            done, todo = [], []
            for line in inf: 
                line = line.strip()
                try:
                    label, word, rest = line.split('\t')
                    done.append((label, word, rest))
                except ValueError:
                    try:
                        word, rest = line.split('\t')
                        todo.append((False, word, rest))
                    except ValueError:
                        pass
        ws0 = WS(False, done, todo)
    main2(ws0, 0)
