---
title: "Hybrid Mobile Apps Quality, Speed to Market, and Adoption: A Look At React Native"
date: "May 2018"
author: "Ryan Turner"
classoption: twocolumn
references:
- id: reactshowcase
  type: webpage
  author:
  - family: Facebook
  issued:
  - year: '2018'
  accessed:
  - year: '2018'
    month: '5'
    day: '26'
  title: React native · a framework for building native apps using react
  URL: https://facebook.github.io/react-native/showcase.html

- id: huynh2017hybrid
  type: article-journal
  author:
  - family: Huynh
    given: Minh
  - family: Ghimire
    given: Prashant
  - family: Truong
    given: Donny
  issued:
  - year: '2017'
  title: 'Hybrid app approach: Could it mark the end of native app domination?'
  title-short: Hybrid app approach
  container-title: Issues in Informing Science and Information Technology
  page: '049-065'
  volume: '14'

- id: noei2017study
  type: article-journal
  author:
  - family: Noei
    given: Ehsan
  - family: Syer
    given: Mark D
  - family: Zou
    given: Ying
  - family: Hassan
    given: Ahmed E
  - family: Keivanloo
    given: Iman
  issued:
  - year: '2017'
  title: A study of the relation of mobile device attributes with the user-perceived
    quality of android apps
  container-title: Empirical Software Engineering
  publisher: Springer
  page: '3088-3116'
  volume: '22'
  issue: '6'

- id: hu2018studying
  type: article-journal
  author:
  - family: Hu
    given: Hanyang
  - family: Wang
    given: Shaowei
  - family: Bezemer
    given: Cor-Paul
  - family: Hassan
    given: Ahmed E
  issued:
  - year: '2018'
  title: Studying the consistency of star ratings and reviews of popular free hybrid
    android and iOS apps
  container-title: Empirical Software Engineering
  publisher: Springer
  page: '1-26'
- id: liu2017
  type: paper-conference
  author:
  - family: Liu
    given: W.
  - family: Zou
    given: Y.
  - family: Yang
    given: Y.
  - family: Cheng
    given: W.
  - family: Zhang
    given: G.
  issued:
  - year: '2017'
    month: '12'
  title: How app update affects app download in iOS appstore
  container-title: 2017 3rd ieee international conference on computer and communications
    (iccc)
  page: '2499-2502'
  keyword: iOS (operating system);mobile computing;app developers;app download;app
    update;average downloads;digital distribution platforms;end users;metric named
    Pulling Rate;mobile applications;mobile stores;release strategies;third-party
    appstore;Ecosystems;Extraterrestrial measurements;Google;Libraries;Mobile applications;Software;AppStore;Measurement;Update;component
  DOI: 10.1109/CompComm.2017.8322985

- id: que2016
  type: paper-conference
  author:
  - family: Que
    given: P.
  - family: Guo
    given: X.
  - family: Zhu
    given: M.
  issued:
  - year: '2016'
    month: '12'
  title: A comprehensive comparison between hybrid and native app paradigms
  container-title: 2016 8th international conference on computational intelligence
    and communication networks (cicn)
  page: '611-614'
  keyword: hypermedia markup languages;mobile computing;HTML5 language;hybrid app
    paradigm;mobile application development;native app paradigm;Androids;Hardware;Humanoid
    robots;Mobile communication;Smart phones;Testing;Tools;hybrid;mobile app paradigm;native;performance
  DOI: 10.1109/CICN.2016.125
- id: taftPhoneGap
  type: webpage
  author:
  - family: Taft
    given: Darryl K.
  issued:
  - year: '2009'
  title: PhoneGap simplifies iPhone, android, blackberry development
  URL: http://www.eweek.com/development/phonegap-simplifies-iphone-android-blackberry-development
  accessed:
  - year: '2018'
    month: '5'
    day: '31'
- id: Mercado:2016:ICD:2993259.2993268
  type: paper-conference
  author:
  - family: Mercado
    given: Iván Tactuk
  - family: Munaiah
    given: Nuthan
  - family: Meneely
    given: Andrew
  issued:
  - year: '2016'
  title: The impact of cross-platform development approaches for mobile applications
    from the user’s perspective
  container-title: Proceedings of the international workshop on app market analytics
  collection-title: WAMA 2016
  publisher: ACM
  publisher-place: New York, NY, USA
  page: '43-49'
  keyword: cross-platform, mobile development, quality, user reviews
  URL: http://doi.acm.org/10.1145/2993259.2993268
  DOI: 10.1145/2993259.2993268
  ISBN: '978-1-4503-4398-5'

- id: Ali:2017:SAD:3104086.3104099
  type: paper-conference
  author:
  - family: Ali
    given: Mohamed
  - family: Joorabchi
    given: Mona Erfani
  - family: Mesbah
    given: Ali
  issued:
  - year: '2017'
  title: 'Same app, different app stores: A comparative study'
  title-short: Same app, different app stores
  container-title: Proceedings of the 4th international conference on mobile software
    engineering and systems
  collection-title: MOBILESoft ’17
  publisher: IEEE Press
  publisher-place: Piscataway, NJ, USA
  page: '79-90'
  keyword: Android, app stores, cross-platform apps, iOS
  URL: https://doi.org/10.1109/MOBILESoft.2017.3
  DOI: 10.1109/MOBILESoft.2017.3
  ISBN: '978-1-5386-2669-6'
---

Traditionally, mobile application development is dominated by the languages and APIs provided by device manufacturers. Hybrid mobile application development has existed for nearly a decade [@taftPhoneGap], however new advancements have been made in ease of development and performance with the introduction of Ionic and React Native. There are few academic studies on these more modern hybrid frameworks. React Native is significantly different in the way in which development takes place as well as its performance and feature set compared with Ionic, more traditional hybrid frameworks, and the standard native app development frameworks. In this research, React Native will be compared to traditional native app development in three aspects: the end user's perception of quality, the speed of the software development life cycle, and adoption in the app stores. Established techniques will be repeated with React Native to offer a comparison. The rest of this writing will focus first on the existing research as it exists, why React Native is significantly different and demands the research be repeated, and end with the tasks that will take place in order to answer these questions.

## Existing Research on Hybrid Mobile App Development

- Comparison of development paradigm (cordova)
- Advantages of hybrid over native dev (ionic, which is based on cordova)
- Cross platform user perception
- Prevalance of hybrid apps in the app stores, across different segments

## Distinguishing React Native from Other Hybrid Frameworks

- Open framework
- JavaScript + native UI
- Focus on performance
- Big community of modules

## Research Approach

- Reverse engineer apps to find use of React Native
- Crawl reviews, analyze sentiment, ratings, and release timeline across popular RN and non RN apps
- Survey developer community for input and benchmarks of react native to traditional dev

## References
