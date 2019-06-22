## Train a classifier to label words from entries in a X-Russian dictionary
## with continuation class aka lexicon names (to be used in a Lexc-based
## morphological transducer for X)
##
## INPUT: (category \t entry word \t the rest of the dictionary entry)+
## EXAMPLE:
## CC		А	I союз противит разг а, тогда как, в то время как —	Хуш, ваъданг канча3— Кирк центнер дан — А кизлар-чи3 —	Юз» (Ойбек «О в шаба халар») Ну, каково тво« обяз I тельство3— По сорок центнеров — А у девушек3— Сто*
## IJ		А	II межд 1, вырсжает вопрос удивление и т п Р, да3, что3, ними дединг? а3 что ты сказал3 а3 ростданми’ а3 неужели правда3 мен хам бораман, а3 я тоже пойду, да3 2 (произносится протяжно) выражает удивление, до гадку а, да, вот как, вот оно что, а, тушундим а, пончл а, биламан, биламан а, зияю знаю
## QST		-а	(-я — после гласных иногда пишется отдельно) частица 1 выражает удивление недоумение, опасение со жаление, восхищение, утверждение қаранг-а, қандай ба~ ^ор! смотрите, какая весна» у жуда қув экан-а! какой он оказывается, хитрец» билмайман эмиш-а’ подумайте, он не знает1, аттанг-а! как жаль», какая досада» шамоллаб цолмаса майли-я’ как бы он ие простудился!, 2 выражает иронию иронический вопрос, билмайман дегин-а? ты го воришь, что не знаешь да3
## N1,ADV		АБАД	вечность; // навеки то ~ поэт навеки навсегда на вечные времена на веки вечные
## A1		АБАДИЙ	вечный, // вечно навеки навечно, навсегда -шуҳрат вечная слава ~ равишда, ~ суратда навеки, на всегда, ~ колдирмок оставлять навеки увековечивать
##
## TODO support multilabel classification for real

import nltk

nltk.classify.megam.config_megam("/home/selimcan/local/megam-64")

## Void -> nltk.classify.ClassifierI
def main():

    raw_train_data = []
    with open("training_data.csv") as inf:
        for line in inf:
            cat, word, *expl = line.strip().split('\t')
            raw_train_data.append((cat, word, ' '.join(expl)))

    train_data = []
    for label, word, expl in raw_train_data:
        train_data.append((word_expl2featvec(word, expl), label))

    classifier =  nltk.classify.MaxentClassifier.train(train_data, algorithm='megam',
                                                       trace=0, max_iter=10)

    with open('dev_data.csv') as inf:
        for line in inf:
            try:
                word, expl = line.strip().split('\t')
                label = classifier.classify(word_expl2featvec(word, expl))
                print(label, word, expl, sep='\t')
            except ValueError:
                print(line)
    print(nltk.classify.util.accuracy(classifier, train_data))
    return classifier

def word_expl2featvec(word, expl):
    """String String -> dictionary String->String)

    Given entry word, explanation, return feature vector.""" 
    fv = {'len': str(len(word)), 
          'pre1': word[:1], 'pre2': word[:2], 'pre3': word[:3], 
          'pre4': word[:4], 'pre5': word[:5], 
          'suf1': word[-1:],'suf2': word[-2:], 'suf3': word[-3:], 
          'suf4': word[-4:], 'suf5': word[-5:], 
          'contains-': '-' in word} 
    for w in expl.split(): 
        fv[w] = True
        fv[w[-3:]] = True 
#    for ngram in char_ngrams(expl, 4): 
#        fv[ngram] = True 
    return fv

def char_ngrams(s, n):
    """String -> (listof String)

    Return character n-grams from s."""
    return [s[i:i+n] for i in range(len(s)-n+1)]

if __name__ == '__main__':
    main()
