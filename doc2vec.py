import pandas as pd
import numpy as np

import gensim
from gensim.models import Doc2Vec
import multiprocessing
from gensim.parsing.preprocessing import STOPWORDS as stop_words
from nltk.tokenize import word_tokenize

cores = multiprocessing.cpu_count()
assert gensim.models.doc2vec.FAST_VERSION > -1

df = pd.read_csv("D:\Documentos\Movie\movielens\ResultadoFinal.csv")
df.rename(columns={'text':'plot'}, inplace=True)

df['plot']=df['plot'].astype(str)

def read_corpus(data, tokens_only=False):
    for i, line in enumerate(data):
        
        text = gensim.utils.simple_preprocess(line)
        #text = word_tokeninze(line)
        tokens = [w for w in text if not w in stop_words]
        if tokens_only:
            yield tokens
        else:
            # For training data, add tags
            yield gensim.models.doc2vec.TaggedDocument(tokens, [i])
            
train_corpus = list(read_corpus(df['plot']))
test_corpus = list(read_corpus(df['plot'], tokens_only=True))

model = Doc2Vec(dm=0, vector_size=200, window=8, min_count=8, workers=cores, epochs=20)


model.build_vocab(train_corpus)
model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)

#df['id'] = df.index

def filmes(id=-1,nome='NULL'):
    if nome!='NULL':
        id = df.loc[df['title']==nome].index[0]
    #print(id)
    for title in df.title.tolist()[id:id+1]:
        print ("Query: ", title)    
    vec = model.docvecs.most_similar(id,topn=12)
    for name in vec:
        print('Similares ',df.loc[df['id']==name[0],['title', 'genres']],'=', name[1])

print(filmes(3574))