---
layout: default
---

# NLP4Twitter: The Turin Lectures (June 2016)

[Leo Ferres](http://leoferres.github.io), PhD<br>
Data science Institute<br>
Faculty of Engineering,<br>
Universidad del Desarrollo &<br>
Telefónica R&D Center<br>

- email: [leoferres@udd.cl](mailto:leoferres@gmail.cl), [lferres@udd.cl](mailto:lferres@udd.cl)
- twitter: [@leoferres](https://twitter.com/leoferres)
- github: [leoferres](http://github.com/leoferres)
- instagram: [leoferres](https://www.instagram.com/leoferres/)

## Introduction

In this tutorial, we will analyze and discuss some Natural 
Language Processing (NLP) techniques for extracting detailed information
from free-text fields (noisy text) in tweets. We will assume a "task-driven NLP approach", which means that
our objective will be to define certain common tasks performed on
tweets (e.g., sentiment analysis or rumor detection) using (sometimes non-naïve)
NLP techniques.

Remember that this course is about NLP techniques, not, for example about graph-based approaches (think hashtag identification) for Twitter research. However, some of these models are simple enough that they lend themselves easily to those graph-based approaches: keyword/n-gram-based approaches come to mind.

Another thing I have actually paid attention to is multilingual processing: if there're ever two similar papers, one on a weird language, like, say, Italian, and another one in English, I picked the former one.

Finally, I have tried to go to the origin of ideas, as much as possible, just to put the ideas in their right context. Thankfully, Twitter is young (2006) and research on it even younger. However, this is not the case with NLP, and even less so linguistics. I do wish to be comprehensive though, and this is the first step towards that... **with your help**. But what does "with your help" means?

The Turin Lectures (yes, I'm aware I'm only missing a 'g' for this to be epic, but still) is not your run-of-the-mill course. It will be unusual in the sense that we will all be working and researching papers together, doing research together. Each of us will be working on implementing a paper that does not have code in it, and we will discuss this in class. This is loosely inspired in [Knuth's "Aha" Sessions](https://youtu.be/Lg5rrgIfWWg). We will have to prepare some of this beforehand, so I'm making available some of the papers I consider important for each topic. You will find those beside each of the topics below.

We don't really have that much time, so let's enjoy ourselves and be productive. Happy coding!


## Topics

We will try to cover several topics in this course. Some of them include:

 1. Sentiment analysis/classification
 2. Polarity
 4. Event detection
 5. Topic detection/identification/modeling
 6. Opinion mining
 7. Rumor identification
 8. Credibility
 9. Controversy identification
 10. Spam filtering
 11. Bot detection
 13. Gender identification
 14. Political alignment
 15. Mood/emotion prediction/diffusion
 17. Humor/Irony/Sarcasm/deception/subjectivity identification
 19. Authorship identification
 20. Censorship identification

while some of the NLP techniques include

 1. POS-Tagging
 2. Latent semantic analysis
 3. Dirichlect allocation
 4. web n-grams (co-occurrence)
 5. Language modelling
 6. Semantic enrichment
 7. Corpus creation
 8. Named-entity recognition/resolution
 9. Lexicons
 10. Tweet normalization/content curation (OOVs)
 11. Semantic role labeling
 12. Keyphrase/keyword detection/extraction
 13. Stop words
 14. Comparability/similarity metrics
 15. Language identification
 16. Conceptual/semantic similarity
 17. Content analysis
 
to name but a few of what we might cover. To this, we have to add the "high performance" part of it:

 1. Frameworks: hadoop, spark
 2. Parallel programming: parallel (bash), pyparallel (python)

This is simply a list of topics, I'd be very interesting in hearing what students might be interested in as well. Shoot me [an email](emailto:lferres@udd.cl)!

{% include image.html
            img="./images/my_twitter_wordcloud.png"
            title="test"
            caption="Wordcloud of all the papers in the ACM DL with \"Twitter\" in the title." %}


## Scheduling


### Week 1

- **Lecture 1**: Intro, Sentiment Analysis I <span style="color: red">(Wed 8 Jun 2016 11:00am, Aula E)</span><br>
[ video ] [ [notebooks](https://github.com/leoferres/nlp4twitter_tutorial/tree/master/notebooks/01-SentimentAnalysisI-Notes.ipynb) ] [ extra code ] [ datasets ] [ scribe notes ]

- **Lecture 2**: Sentiment Analysis II <span style="color: red">(Thu 9 Jun 2016 4:00pm, Aula F)</span><br>
[ video ] [ [notebooks](github_place) ] [ extra code ] [ datasets ] [ scribe notes ]

- **Lecture 3**: Event Detection <span style="color: red">(Fri 10 Jun 2016 11:00am, Aula F)</span><br>
[ video ] [ [notebooks](github_place) ] [ extra code ] [ datasets ] [ scribe notes ]

### Week 2

- **Lecture 4**: Topic Detection <span style="color: red">(Mon 13 Jun 2016 2:00pm, Aula F)</span><br>
[ video ] [ [notebooks](github_place) ] [ extra code ] [ datasets ] [ scribe notes ]

- **Lecture 5**: User Profiling <span style="color: red">(Wed 15 Jun 2016 4:00pm, Aula F)</span><br>
[ video ] [ [notebooks](github_place) ] [ extra code ] [ datasets ] [ scribe notes ]

- **Lecture 6**: High-Performance Computing and NLP <span style="color: red">(Fri 17 Jun 2016 11:00am, Aula F)</span><br>
[ video ] [ [notebooks](github_place) ] [ extra code ] [ datasets ] [ scribe notes ]


## Evaluation

 1. A project, 70% of the final grade (preferably with some issues in Italian)
 2. A presentation of an assigned paper, 20% of the final grade
 3. Scribing a lecture: 10% of the final mark

Given that my Italian is non-existent, and that there's always much more work in English, we will try to make this course a contribution to Italian NLP (not that you need it, there's a very healthy tradition on NLP of Italy!).

## Prerequisites

 1. Linux, bash, markdown and python (I could give a short tutorial on
	this as well, but c'mon :)
 2. Some knowledge of probability, but the course will be
	self-contained. Perhaps many of the participants have already read
	Jurafsky and Martin, that should be enough.

## Tools to be used

The first class will be a tutorial on using the following tools:

 - Python version 2.6-2.7 or 3.3+
 - `numpy` version 1.5 or later: http://www.numpy.org/
- `scipy` version 0.10 or later: http://www.scipy.org/
 - `matplotlib` version 1.3 or later: http://matplotlib.org/
 - `scikit-learn` version 0.14 or later: http://scikit-learn.org
 - `ipython` version 2.0 or later, with notebook support:
   http://ipython.org
 - `seaborn` version 0.5 or later
 - `nltk` version 3.2.1 or later: https://github.com/nltk/nltk
 - `spacy` version 0.100.6 or later: https://github.com/spacy-io/spaCy

and we will probably use some other tools in the Python stack.

The easiest way to get these is to use the [conda](https://store.continuum.io/)
environment manager.  I suggest downloading and installing
[miniconda](http://conda.pydata.org/miniconda.html).

Once this is installed, the following command will install all
required packages in your Python environment: 

`$ conda install numpy scipy matplotlib scikit-learn ipython-notebook seaborn`


Alternatively, you can download and install the (very large) Anaconda
software distribution, found at https://store.continuum.io/.

## Downloading the Tutorial Materials

I would highly recommend using git, not only for this tutorial, but
for the general betterment of your life.  Once git is installed, you
can clone the material in this tutorial by using the git address shown
above:

```
$ git clone git://github.com/leoferres/nlp4twitter_tutorial.git
```

If you can't or don't want to install git, there is a link above to
download the contents of this repository as a zip file.  I may make
minor changes to the repository in the days before the tutorial,
however, so cloning the repository is a much better option.