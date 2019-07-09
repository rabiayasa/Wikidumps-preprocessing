## Extract the article titles and text from the Wiki XML files and Text Processing steps
# Wiki XML files
Raw XML files includes many tags and unnecessary elements in web pages,that can be templates, pictures, frames,infoboxes and so on. However we need to work just only language examples (articles and titles), so we need to eliminate all unnecessary tags. The best is extract the <title> and <text> tags first. 
  
# Gensim
Gensim is a free Python library designed to work on text files. This library supports some unsupervised algorithms like Word2Vec and gives tool to consturct it.[In here](https://radimrehurek.com/gensim/intro.html), you can look at this library in detailed.

Install gensim
```
pip install --upgrade gensim
```
# Wikicorpus by Gensim
Wikicorpus is a tool to work on wiki dump xml files provided by gensim. Using this tool it can be easily created text files that is includes only article titles and texts because, this module deals with unwanted tags, frames, infoboxes easily and does cleaning special characters and removing punctuations. [In here](https://radimrehurek.com/gensim/corpora/wikicorpus.html), you can look at this module in detailed.


In most of the NLP project needs preprocessing steps to clean the dataset and create workable scheme. Although preporcessing steps depends on the nature of the project, frequently used steps are converting lowercase, removing stopwords and applying lemmatization. It can be done  preprocessed steps(mentioned) using Wikicorpus tool without stopwords. In this project we applied lemmatization with WordNetLemmatizer  and Stopwords provided by NLTK. 

It is removed stopwords like "a", "an","herself", "it","are", "was"...

Lemmatization eliminates the prefixes and suffixes and gives lemma that should be an actual language word.

Example lemmatization;butterflies->butterfly , playing->play

# Advantage of working with partitioned files
Wikidumps average size for English language is 16-17 gb. It is recommended to work with partitioned files in order to see the results of the preprocessing steps on the file and to make possible quick work. In this work, we work partitioned files (total number of xml wikidumps files are 56 , dated 01/05/2019).

The preprocessing outputs are saved as txt files. It can be combined for model training using combination.py file.

Preprocessing Outputs
```
carnegie mellon school architecture pittsburgh pennsylvania degree granting institution one five division carnegie mellon university
college fine art succeeds department architecture founded henry hornbostle architect designed original campus continues offer five 
year undergraduate first professional bachelor architecture degree two three year graduate master architecture first professional 
degree school architecture slogan art technology meet practice current head school stephen lee pedagogy undergraduate curriculum...
```
