import pandas as pd
import gensim
import collections
from gensim.models import Doc2Vec
import multiprocessing
from gensim.parsing.preprocessing import STOPWORDS as stop_words
from nltk.tokenize import word_tokenize
from scipy.stats import pearsonr


cores = multiprocessing.cpu_count()
assert gensim.models.doc2vec.FAST_VERSION > -1


data1 = pd.read_csv('teste.csv')
data2 = pd.read_csv('./dt_small/movies.csv')
df1 = data1[['movieId','synopsis']]
df2 = data2[['movieId','title']]
df = pd.merge(df1, df2, left_on='movieId', right_on='movieId')


#data = pd.read_csv('wiki_movies.csv')
#data.head()
#df = data[['Title','Plot','Genre']]
#df['id'] = df.index
#df.rename(columns={'Plot':'plot'}, inplace=True)
#df.iloc[0,1]

df['synopsis']=df['synopsis'].astype(str)
#Data cleaning
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
#Cria Modelo Doc2vec

def modela():
    train_corpus = list(read_corpus(df['synopsis']))
    test_corpus = list(read_corpus(df['synopsis'], tokens_only=True))
    model = Doc2Vec(dbow_words=1, vector_size=100, min_count=4, windown=10, negative=5, epochs=20, alpha=0.025, min_alpha=0.001, workers=cores)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    model.save("alpha.model")

modela()
model= Doc2Vec.load("alpha.model")

def filmes(id=-1,nome='NULL'):
    if nome!='NULL':
        id = df.loc[df['title']==nome].index[0]
    #print(id)
    for title in df.title.tolist()[id]:
        print ("Query: ", title)
    vec = model.docvecs.most_similar(id,topn=15)
    for name in vec:
        print('Similares ',df.loc[df['title']==name[0],['title']],'=', name[1])

#print(filmes(1))
#print(filmes(nome="Harry Potter and the Philosopher's Stone"))

print(pearsonr(model.docvecs[13862], model.docvecs[12775]))
