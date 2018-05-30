---
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
---
# Ryan Turner's Assignment 2

I'd like to focus on a research track for this course. This was a rather straight forward decision for me, as in the past I've worked on both materials and development of educational tech: I did this as part of my job to help onboard new team members. In my undergraduate studies, I worked in a biology research lab helping with bioinformatics. I did not have the chance to participate in any of the writing; given the opportunity today, I'd like to do that.

Recently, I've begun working as a community team member on the React Native project. This is an open-source hybrid mobile development framework created by Facebook. My contributions to date have been in organizing and writing the changelog and managing the channel for community release discussion. In my job, I'm an engineering manager for a mobile app development team – we use React Native extensively. My perception in industry is that this technology is not as widely understood as other solutions like Apache Cordova and Ionic. I'd like to research how React Native development compares to traditional native app development. At this point, the questions I'm considering answering are as follows.

**RQ1: Do React Native applications receive poorer ratings than traditional native applications?**

**RQ2: Are React Native applications released on a faster cadence than traditional native applications?**

**RQ3: Do engineers find learning React Native development simpler than learning traditional native application development?**

**RQ4: Are the top applications in the app stores written without the use of hybrid frameworks?**

The first question came to mind as I read @hu2018studying and @noei2017study. From Hu's work [-@hu2018studying], I realized that cross-platform apps received inconsistent ratings across platforms. This leads me to believe that hybrid applications that do not take care to differentiate their user experience and featureset by platform will be rated poorly compared with applications that only target one platform. React Native and Ionic both have easy means to specify feature differences by platform, however I suspect they are not widely in use. This leads me to suspect that RQ1 will be true. There is also good advice in this paper regarding how to collect reviews and rating for analysis that will be useful. 

From @noei2017study, I realized a good amount of detail of how to go about finding Android apps to analyze, decompiling them, and then running static analysis tools on them. I also have begun to form some predictions of the outcome of my questions: I suspect that RQ1 will be false, as @noei2017study found that the APK size has a positive effect on app reviews. Hybrid applications are larger in size than native apps [@que2016], so one would suspect that will lead to more positive app reviews.

The second question came to mind as I read @huynh2017hybrid. This paper thoroughly evaluates the use of the Ionic Framework. While the paper may serve as a good structure for a similar one on React Native, there are also numerous differences between the technology that may lead to a different approach. For instance, with React Native there are a number of industry-leader firms that use the framework: Facebook, Instagram, Skype, Uber, Walmart, Tesla, Salesforce, Sony, Pinterest, and more [@reactshowcase]. The outcomes of these firms applications can be evaluated to draw conclusions of how they are perceived by users. Additionally, the paper mentions but does not support or further investigate the potential impact on developer learning or development velocity. I suspect that an easier metric to measure will be release cycles, since historical release data can be found oneline. While this doesn't directly show the difficulty of learning, it does illustrate how quickly features and maintenace work can be created.

@que2016 also inspired the third question, however I found a number of the conclusions made to be unsubstantiated. Many presumptions were made regarding the ease of developing using JavaScript and HTML when compared with native app languages like Objective-C and Java. While I personally agree with these statements, I didn't find comfort in these statements being made without evidence of citation, survey, or study. I also found that from time to time the author referred to applications written with the Cordova as being developed in HTML5, which didn't honestly represent the effort – while UI is written in HTML, the functionality is written in JavaScript. I think RQ3 warrants further research.

The forth question came to mind as I further investigated these topics and continued to see papers covering app reviews and ratings. For instance, @huynh2017hybrid does not examine the impact on user satisfaction of delivering a "write-once-and-run-anywhere" (WORA) experience. After reviewing @hu2018studying and @noei2017study however, considering their findings on different user expectations and concerns, I believe this should be researched.

Throughout my reading, I found that many researchers mine app stores to see data about both the applications themselves and usage statistics on them. It's also common for researchers to take advantage of the many mobile profiling tools and measure performance data like memory and CPU utilization, battery temperature, and network transfer. I believe that using techniques borrowed from these papers, all four of my proposed research questions can be explored. Additionally, my contribution besides applying these published techniques will be in creating a system to identify the usage of React Native from reverse engineering applications. This then could enable future research related to identifying the use of hybrid frameworks. I believe that answering these four questions will help inform educators and employers alike to invest the right amount of effort in React Native.

## References