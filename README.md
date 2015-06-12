This is a little experiment I ran to cluster economics articles based on running the [Latent Dirichlet Allocation](http://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) algorithm on their titles and abstracts.

## Dependencies

The code is in Python 3 and some of it is in the form of an IPython notebook. The [NLTK](http://www.nltk.org/), [LDA](https://pypi.python.org/pypi/lda), [Scikit-Learn](http://scikit-learn.org/) and [Matplotlib](http://matplotlib.org/) libraries are used.

## Data

The data consists of bibliographic data for selected journals downloaded from [RePec](http://repec.org/). The tree under ftp://ftp.repec.org/opt/amf/RePEc/ conatins metadata in the [AMF](http://amf.openlib.org/doc/ebisu.html) format. The filer `repec.tar.xz` in the repository contains a mirror of selected parts of this tree.

## Running

The clustering code expects the data to live in a sqlite database `repec.sqlite`. To create this database run

    $ ./readrepec.py repec.tar.xz repec.sqlite
    $ ./add_jnames.py repec.sqlite

The actual fitting of the LDA model is done by the IPython notebook `classify.ipynb`. On runnin it it creates HTML files `index.html` and `cluster[nn].html` containing links to the clustered articles.
