#without stemming

import time
import os
import logging
import os.path
import sys
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from gensim.corpora import WikiCorpus
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer 
import nltk
nltk.download('stopwords')
lemmatizer = WordNetLemmatizer() 

#Finding all xml files for cleaning 
def find_the_way():
    path = './xmls/'
    xml_files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.bz2' in file:
                xml_files.append(os.path.join(r, file))
    return xml_files
files=find_the_way()
#Removing stopwords
stop_words = set(stopwords.words('english')) 


for i in files:
    second=time.time()#time stamp for all processing time
    outputfilenames=i[7:-4]+".txt"
    print(outputfilenames)
    output_plaintext= open(outputfilenames, 'w')
    #gensim wikicorpus tool
    wiki = WikiCorpus(i, lemmatize=False, dictionary={})
    counter=0
    for text in wiki.get_texts():
        try:
            filtered_sentence=[]
            for w in text:
                if w not in stop_words :
                    temp=lemmatizer.lemmatize(w)#lemmatization
                    filtered_sentence.append(temp)
            #Writing outputs in a text files        
            output_plaintext.write(bytes(' '.join(filtered_sentence), 'utf_8').decode('utf_8') + '\n')
        except:
            counter=counter+1
            if counter==1:
                print(text)
            continue
#error checking
    print(float(time.time()-second))
    output_plaintext.close()
    print("error=",counter)










