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
Wikicorpus is a tool to work on wiki dump xml files provided by gensim. Using this tool it can be easily created text files that is includes only article titles and texts because, this module deals with unwanted tags, frames or infoboxes easily. 
In most of the NLP project needs preprocessing steps to clean the dataset and create workable scheme. Although preporcessing steps depends on the nature of the project, frequently used steps are converting lowercase, removing stopwords and applying lemmatisation. It can be done mentioned preprocessed steps with using Wikicorpus tool. Also
