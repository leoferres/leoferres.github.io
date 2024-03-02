---
layout: post
title:  "Countries with (C/X)DR studies"
date:   2019-11-29 00:00:00 -0300
categories: mobility cdr countries
---

# Countries with (C/X)DR studies

## Introduction

People have been asking me why CDR investigations are only carried out
in "third world" countries like Chile
([??!!](https://en.wikipedia.org/wiki/Economy_of_Chile)), there's even
a bit of a more formal (but limited)
[study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6072975/) coming
to the same conclusions. After seeing much work in the area and
knowning this wasn't right, I asked [this Twitter
question](https://twitter.com/leoferres/status/1173009065494110208),
and took the Netmob 2010, 2011, 2013, 2015 and 2017 booklets of
abstracts that can be found [here](http://netmob.org/) and ran the
following code on them:

## Processing

{% highlight shell %}
#!/bin/bash
echoerr() { echo "$@" 1>&2; }
while read line; do
	echoerr $line
	echo $line
	pdfgrep --color=always --cache -n -i "$line" netmob_abstracts_*.pdf
done < listofcountries.txt
{% endhighlight %}

I only worked with the oral presentation booklets (not posters or the
D4D challenge). This produced

{% highlight shell %}
wc -l bib/countriesfound.txt
66135 bib/countriesfound.txt
{% endhighlight %}

using a `listofcountries.txt` file that I found on the internet. Many
of these lines are false positives though, either because of
mismatches "Mali" -> "Nor*mali*zed" or other similar effects. I then
spent some time checking out the files by hand, and recording the ones
that were effectively a mention of a specific country's CDR dataset.

## Results

The following table is simply an "existence" table, I'm not
exhaustive, but rather would like to show which countries have been
studied using these methods *at least once*.

| Continent         | Country       |   Page |    Subscribers | Length (mo) | Year | Contributor        |
|-------------------+---------------+--------+----------------+-------------+------+--------------------|
| Europe            | Andorra       |    105 |        1264292 |           1 | 2017 | NetMob             |
| America (South)   | Argentina     |    104 |      40000000? |           5 | 2013 | NetMob             |
| Europe            | Austria       |     55 |              ? |           ? | 2013 | NetMob             |
| Europe            | Belgium       | [source](https://arxiv.org/pdf/0905.0692.pdf) |        2500000 |           6 | 2009 | [@leoferres](https://twitter.com/leoferres)       |
| America (South)   | Brazil        |     46 |              ? |         0.6 | 2013 | NetMob             |
| America (South)   | Chile         |    126 |         142988 |         0.5 | 2017 | NetMob             |
| Asia (East)       | China         |     85 |              ? |           6 | 2017 | NetMob             |
| Europe            | Estonia       |     87 |          48871 |         0.3 | 2015 | NetMob             |
| Europe            | France        | [source](https://theses.ncl.ac.uk/jspui/handle/10443/4399) |       48500000 |    5 (2007) | 2018 | [@Metti_Hoof](https://twitter.com/Metti_Hoof)      |
| Europe            | Portugal      |     72 |              ? |           6 | 2013 | NetMob             |
| Europe            | Spain         |     72 |              ? |           6 | 2013 | NetMob             |
| America (Central) | Haiti         |     74 |        2900000 |           2 | 2015 | NetMob             |
| Asia (South)      | India         |    109 |        4000000 |           3 | 2015 | NetMob             |
| Europe            | Ireland       |     57 |         500000 |           ? | 2011 | NetMob             |
| Europe            | Italy         |     56 |              ? |          10 | 2010 | NetMob             |
| America (Central) | Mexico        |     42 |       1000000s |           6 | 2015 | NetMob             |
| Africa            | Namibia       |    117 |        4500000 |          50 | 2017 | NetMob             |
| Africa            | Senegal       |    117 |        9500000 |          12 | 2017 | NetMob             |
| Asia              | Nepal         |     58 |       12900000 |           ? | 2017 | NetMob             |
| Europe            | Netherlands   |    103 |              ? |          36 | 2011 | NetMob             |
| Europe            | Norway        |    145 |            509 |           ? | 2013 | NetMob             |
| Africa            | Rwanda        | [source](https://academic.oup.com/restud/article/86/3/1033/5061115?guestAccessKey=8628aed3-426d-4fc6-af39-bd5561c493a3) | 400000/1500000 |          56 | 2015 | [@deaneckles](https://twitter.com/deaneckles)      |
| Europe            | Slovenia      |    173 |           5000 |           1 | 2013 | NetMob             |
| Asia              | Sri Lanka     |     75 |              ? |           ? | 2017 | NetMob             |
| Europe            | Switzerland   |    118 |             38 |          10 | 2013 | NetMob             |
| Africa            | Tanzania      |    146 |         415000 |           4 | 2017 | NetMob             |
| America (North)   | United States |     47 |         475000 |           2 | 2011 | NetMob             |
|-------------------+---------------+--------+----------------+-------------+------+--------------------|
| Asia              | Bangladesh    | [source](https://link.springer.com/article/10.1007/s10584-016-1753-7) |        5100000 |           3 | 2016 | =@arutherfordium=  |
| Europe?           | England       | [source](http://www.uvm.edu/pdodds/files/papers/others/everything/beep2010a.pdf) |       65000000 |           1 | 2010 |  [@arutherfordium](https://twitter.com/arutherfordium)  |
| Asia              | Pakistan      | [source](https://www.pnas.org/content/112/38/11887.long) |       39000000 |           7 | 2015 | [@arutherfordium](https://twitter.com/arutherfordium)  |
| Asia              | Turkey        | [source](https://d4r.turktelekom.com.tr/) |        3500000 |           ? | 2017 | [@arutherfordium](https://twitter.com/arutherfordium)  |
| Europe            | Switzerland   | [source](https://diegopuga.org/papers/calling.pdf) |        2700000 |          12 | 2019 | [@ProfDiegoPuga](https://twitter.com/ProfDiegoPuga)   |
| America (South)   | Colombia      | [source](https://www.unglobalpulse.org/news/using_mobile_traces_curve_Zika_spread_Colombia) |        7000000 |           6 | 2018 | [@danielapaolotti](https://twitter.com/danielapaolotti) |
| Africa            | Cote D'Ivoire | [source](https://link.springer.com/article/10.1140/epjds/s13688-015-0053-1) |        5000000 |           5 | 2012 | [@lbravoc](lbravoc)         |


## Conclusions

These are some general conclusions I glean from the table above. They
are, alas, not scientific at this point, but anecdotal and would be
happy to discuss them. In fact, someone should do a much more
in-depth/serious study and let the community know. For now, this
should suffice for me so I can just redirect some types of questions I
get to this website.

1. There's not really a preference for non-European/developing
   countries, at least not in this "there is (at least one) dataset
   for country X" review table,
2. the above being said, it does seem that CDR work prioritizes
   certain countries (Haiti, as the foremost example), but they also
   seem to do so for humanitarian reasons, instead of less-strict
   privacy laws (people will do whatever they can to help, including
   giving out otherwise sensitive information... these are not leaks),
3. most of these studies analyze mobile data /from their own contries/
   rather than taking data from other countries, except maybe the D4R
   Challenge and Haiti datasets, which were designed for external
   help.

## Notes

1. This is just *one conference* (albeit the most prominent one,
   NetMob) and still, not all papers have been included, meaning I'm
   completely sure that there area many, many other countries/regions
   that have been studies using C/XDR datasets. [ *NB*: As more
   submissions trickle in, I will have to add other sources. ]
2. Sometimes, there may be little information about a dataset in a
   given country, but then it has been studied further in some other
   paper. I have recorded the page and edition of NetMob with the
   most information.
3. There might also be some points where I've missed a piece of
   information, or even a better dataset from the same region. This
   should not impact strongly (or logically negatively) on the fact
   that there *exists* a dataset for that region.
4. This is of course, and by necessity, quick and dirty. Anyone can
   ask me for pull requests, it'd be fantastic to have a rather
   complete list of datasets that have been published. I might come
   back to this running a more exhaustive search in the Netmob pages,
   or I might not, but one thing that could be done is search for all
   instances of the word "data" and see if there are other countries
   that were not picked up by the countries' restrictive regular
   expressions (or more likely cities as well).

## Acknowledgements

I'd like to thank the following people for their Twitter replies:
Esteban Moro, Martha Gonzalez, Jari Saramaki, Nuria Oliver, Erki
Saluveer, Yves-Alexander de Montjoye, Alex Rutherford.

Hope it's useful.
