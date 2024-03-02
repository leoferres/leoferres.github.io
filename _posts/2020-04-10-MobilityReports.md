---
layout: post
title:  "COVID19 Mobility Reports"
date:   2020-04-10 00:00:00 -0300
categories: covid gps mobility
---

# Intro

In the past few weeks, many academic research groups ([including our
own](https://datascience.udd.cl/covid_ids_tef_01.pdf)) have been
working on providing information about mobility in many
countries. This is an incredible effort, carried out during
extraordinary times and by really talented people. There are many
methodologies (using different mobility metrics: radius of gyration,
number of visited places), datasets (gps points, data detail records),
and analysis (trips, activity) going around, so maybe trying to keep a
centralized repository of them, with some commentary, would be
worthwhile both to keep updated and personal edification, and also as
a service to the community. We have done [something similar]({% post_url 2019-11-19-listofcoutriescdr %}) for mobile
stream data research per country. [EDIT 2020-04-28 10:42:16 -0400: A
large group of researchers have written a fantastic essay on the topic
that should be used to frame the discussion of the issues [here](https://advances.sciencemag.org/content/early/2020/04/27/sciadv.abc0764).]

In this instance, I will only look at “in the wild” mobile phone data,
either by telco data (e.g., xdr or cdr), or by other companies that
provide “app” data (e.g., gps data). In the table below, the field
date is the date the report was made publically available, countryis
the country that the report applies to (not necessarily where the
research was carried), the paper field contains a URL link to the
paper (preferably in pdf format) and finally the tags field gives an
idea of the general issue being addressed. So far it’s only been
mobility, plus one study analyzing “social mixing” as well.

Perhaps a small methodological clarification is needed here: xdr data
comes from “meaningful” (i.e., long enough to be billed by the telco)
internet interactions with a cellphone antenna. The gps data comes
from apps in phones (like Facebook, Google, and many (most?) smaller
ones) and usually companies that aggregate them. The gps data is of
“higher quality”, very fine grained, both spatially and temporally,
while xdr data is not (data points at 15 mins intervals or xMB
downloaded, for example, and at the level of antennas, not
individuals). However, xdr usually reports unique devices in the
millions , while gps will depend on the level of adoption of the
different apps being aggregated, roughly in the order of 100,000s
unique devices per country. A new “player” in all this is the madid
value for the dtype field. I assume the authors are talking about the
mobile advertising ID feature in Android and Apple phones. I did not
know about this until yesterday [2020-04-11]. [Here’s some information
about it from Google](https://support.google.com/admanager/answer/6274238?hl=en), and [an article from WIRED](https://www.wired.com/story/ad-id-ios-android-tracking/).

![](/assets/mapchart_20200426.png)

Countries with mobility studies using mobile phone datasets, according
to the table below. Map is courtesy of mapchart.net. Please help
expand this table by sending me an email at <lferres@udd.cl>, through
my Twitter [@leoferres](https://twitter.com/leoferres), or posting in
the comment section below.

* The table with the data, in CSV format is
  [HERE](/assets/cdrscovidworld.csv)

NOTE: There’s a special mention here to the [Google Mobility
effort](https://www.google.com/covid19/mobility/), since it covers the
whole the world! Although a little bit “underexplained”, its simplicty
and informational density make them quite extraordinary. There’s more
information in [their blog post](https://www.blog.google/technology/health/covid-19-community-mobility-reports).

**[2020-04-13 08:07:01 -0400]**: There’s a [memo](https://www.gsma.com/publicpolicy/wp-content/uploads/2020/04/The-GSMA-COVID-19-Privacy-Guidelines.pdf) by the GSMA outlining
some suggestions for the handling of mobile phone data through the
COVID19 crisis. Thanks to Ciro Cattuto for bringing it to my
attention.

**[2020-04-26 10:24:05 -0400]**: There was a big effort in to attempt
a [large scale coverage of mobility in Latin America and the
Caribbean](https://www.iadb.org/es/investigacion-y-datos/movilidad-covid)
by the IADB using gps. There’s [a study by the University of
Texas](https://covid-19.tacc.utexas.edu/projections/) as well in the
United States to using gps to measure social distancing and
projections of deaths. The New York Times ran [a similar
story](https://www.nytimes.com/interactive/2020/04/02/us/coronavirus-social-distancing.html?auth=login-google)
also using gps to see which counties stayed at home. (Interesting,
since it’s been so critical about this methodology before, see [here](https://www.nytimes.com/interactive/2018/12/10/business/location-data-privacy-apps.html)
and [here](https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-cell-phone.html)).

