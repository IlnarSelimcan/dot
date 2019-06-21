# coding: utf-8
with open('/tmp/trainuzb') as inf:
    for line in inf:
        cat, word, *expl = line.strip().split('\t')
        
with open('/tmp/trainuzb') as inf:
    for line in inf:
        print(line)
        cat, word, *expl = line.strip().split('\t')
        
with open('/tmp/trainuzb') as inf:
    for line in inf:
        cat, word, *expl = line.strip().split('\t')
        
raw_train_data = []
with open('/tmp/trainuzb') as inf:
    for line in inf:
        cat, word, *expl = line.strip().split('\t')
        raw_train_data.append((cat, word, expl))
        
raw_train_data
raw_train_data = []
with open('/tmp/trainuzb') as inf:
    for line in inf:
        cat, word, *expl = line.strip().split('\t')
        raw_train_data.append((cat, word, ' '.join(expl)))
        
        
raw_train_data
raw_train_data = []
with open('/tmp/trainuzb') as inf:
    for line in inf:
        cat, word, *expl = line.strip().split('\t')
        raw_train_data.append((cat, word, ' '.join(expl)))
        
        
raw_train_data = []
with open('/tmp/trainuzb') as inf:
    for line in inf:
        cat, word, *expl = line.strip().split('\t')
        raw_train_data.append((cat, word, ' '.join(expl)))
        
        
raw_train_data
get_ipython().run_line_magic('ls', '')
## String String String
## String String String -> String (dictionary String->String)
def raw2real(cat, word, expl):
    """Given label ,entry word, explanation, return label, feature vector."""
    return (cat, {'pre1': word[:1], 'pre2': word[:2], 'pre3': word[:3],
                  'pre4': word[:4], 'pre5': word[:5],
                  'suf1': word[-1:],'suf2': word[-2:], 'suf3': word[-3:],
                  'suf4': word[-4:], 'suf5': word[-5:]})
                  
raw2real(raw_train_data[1])
raw_train_data[1]
raw2real(*raw_train_data[1])
def raw2real(cat, word, expl):
    """Given label ,entry word, explanation, return label, feature vector."""
    fv =  {'len': str(len(word)),
           'pre1': word[:1], 'pre2': word[:2], 'pre3': word[:3],
           'pre4': word[:4], 'pre5': word[:5],
           'suf1': word[-1:],'suf2': word[-2:], 'suf3': word[-3:],
           'suf4': word[-4:], 'suf5': word[-5:]}
    return fv
             
raw2real(*raw_train_data[1])
def raw2real(cat, word, expl):
    """Given label ,entry word, explanation, return label, feature vector."""
    fv =  {'len': str(len(word)),
           'pre1': word[:1], 'pre2': word[:2], 'pre3': word[:3],
           'pre4': word[:4], 'pre5': word[:5],
           'suf1': word[-1:],'suf2': word[-2:], 'suf3': word[-3:],
           'suf4': word[-4:], 'suf5': word[-5:]}
    for w in expl.split():
        fv[w] = True
    return (cat, fv)
    
             
raw2real(*raw_train_data[1])
map(raw2real, raw_train_data)
list(map(raw2real, raw_train_data))
def raw2real(cat, word, expl):
    """Given label ,entry word, explanation, return label, feature vector."""
    fv =  {'len': str(len(word)),
           'pre1': word[:1], 'pre2': word[:2], 'pre3': word[:3],
           'pre4': word[:4], 'pre5': word[:5],
           'suf1': word[-1:],'suf2': word[-2:], 'suf3': word[-3:],
           'suf4': word[-4:], 'suf5': word[-5:]}
    for w in expl.split():
        fv[w] = True
    return (cat, fv)
             
[raw2real(*rti) for rti in raw_train_data]
import nltk
nltk.classify.megam.config_megam
nltk.classify.megam.config_megam()
nltk.classify.megam.config_megam("/home/selimcan/local/megam-64")
me = nltk.classify.MaxentClassifier.train()
[raw2real(*rti) for rti in raw_train_data]
td = [raw2real(*rti) for rti in raw_train_data]
me = nltk.classify.MaxentClassifier.train(td, algorithm='megam', trace=0, max_iter=10)
nb = nltk.classify.NaiveBayesClassifier.train(td)
td
temp = []
for l,f in td:
    temp.append((f, l))
    
temp
td = temp
t
td
nb = nltk.classify.NaiveBayesClassifier.train(td)
td
td[1]
td[2]
td[30]
td[30][0]
nb.classify(td[30][0])
for i, ti in enumerate(td):
    print(i, ti[0]['pre5'], ti[0]['suf5'])
    
nb.classify(td[126][0])
nb.classify(td[142][0])
nb.classify(td[88][0])
nb.classify(td[24][0])
nb.classify(td[133][0])
me = nltk.classify.MaxentClassifier.train(td, algorithm='megam', trace=0, max_iter=15)
me.classify(td[133][0])
me.classify(td[146][0])
me.classify(td[151][0])
me.classify(td[143][0])
me.classify(td[144][0])
get_ipython().run_line_magic('save', 'train')
get_ipython().run_line_magic('save', 'current_session ~/train')
get_ipython().run_line_magic('save', 'current_session')
get_ipython().run_line_magic('save', 'current_session ~/0')
get_ipython().run_line_magic('save', 'current_session ~0/')
