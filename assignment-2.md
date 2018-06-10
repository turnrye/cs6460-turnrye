---
references:
- id: iosdeveloperuniversityprogram
  type: webpage
  author:
  - family: Apple
  issued:
  - year: '2018'
  accessed:
  - year: '2018'
    month: '6'
    day: '9'
  title: iOS Developer University Program
  URL: https://developer.apple.com/programs/ios/university/
- id: googledeveloperstraining
  type: webpage
  author:
  - family: Google
  issued:
  - year: '2018'
  accessed:
  - year: '2018'
    month: '6'
    day: '9'
  title: Google Developers Training
  URL: https://developers.google.com/training/android/

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
- id: hu2012curriculum
  type: paper-conference
  author:
  - family: Hu
    given: Wei
  - family: Guo
    given: Hong
  issued:
  - year: '2012'
    month: '8'
  title: Curriculum architecture construction of mobile application development
  container-title: 2012 international symposium on information technologies in medicine
    and education
  page: '43-47'
  volume: '1'
  keyword: computer aided instruction;mobile computing;operating systems (computers);smart
    phones;basic software platforms;curriculum architecture construction;embedded
    operating systems;flexible curriculum architecture;mobile application development
    courses;mobile computing;mobile devices;programming skills;smartphone devices;wireless
    networks;Androids;Computers;Earth Observing System;Humanoid robots;Mobile communication;Training;World
    Wide Web;course design;curriculum;embedded system;mobile application development
  DOI: 10.1109/ITiME.2012.6291243

- id: payne2014teaching
  type: article-journal
  author:
  - family: Payne
    given: Bryson R.
  issued:
  - year: '2014'
    month: '12'
  title: Teaching android and iOS native mobile app development in a single semester
    course
  container-title: J. Comput. Sci. Coll.
  publisher: Consortium for Computing Sciences in Colleges
  publisher-place: USA
  page: '176-183'
  volume: '30'
  issue: '2'
  URL: http://dl.acm.org/citation.cfm?id=2667432.2667458
  ISSN: '1937-4771'

- id: sprinkle2011teaching
  type: paper-conference
  author:
  - family: Sprinkle
    given: Jonathan
  issued:
  - year: '2011'
  title: Teaching students to learn to learn mobile phone programming
  container-title: Proceedings of the compilation of the co-located workshops on dsm’11,
    tmc’11, agere! 2011, aoopes’11, neat’11, & vmil’11
  publisher: ACM
  page: '261-266'

- id: mahmoud2010mobile
  type: paper-conference
  author:
  - family: Mahmoud
    given: Q. H.
  - family: Popowicz
    given: P.
  issued:
  - year: '2010'
    month: '10'
  title: A mobile application development approach to teaching introductory programming
  container-title: 2010 ieee frontiers in education conference (fie)
  page: T4F-1-T4F-6
  keyword: computer aided instruction;computer science education;mobile computing;computer
    engineering education;computer science education;information technology education;introductory
    programming teaching;mobile application development approach;mobile devices;smartphones;Education;Handheld
    computers;Java;Mobile communication;Mobile handsets;Programming profession;CS1;Mobile
    devices;Smartphone programming
  DOI: 10.1109/FIE.2010.5673608
  ISSN: '0190-5848'
title: "Assignment 2"
date: "June 2018"
author: "Ryan Turner"
classoption: twocolumn
---

# Track Selection

I'd like to focus on a research track for this course. This was a rather straight forward decision for me, as in the past I've worked on both materials and development of educational tech: I did this as part of my job to help onboard new team members. In my undergraduate studies, I worked in a biology research lab helping with bioinformatics. I did not have the chance to participate in any of the writing; given the opportunity today, I'd like to do that.

# Theories and Techniques on Learning Mobile App Development

In mobile app development, native frameworks dominate university courses. In my own university studies, I learned iOS development, and here in the OMSCS program Android development is taught in the SDP class. Partly this is due to what materials and resources exist from the platforms themselves [@iosdeveloperuniversityprogram; @googledeveloperstraining]. Interestingly, online courses for hybrid development using frameworks like Ionic, Cordova, and React Native dominate platforms like Udemy and Lynda. I did find examples of courses and curriculums teaching both native iOS and Android development [@payne2014teaching; @sprinkle2011teaching] as well as homing in on a single platform (typically Android, since unlike iOS, development can take place on any computer) [@mahmoud2010mobile]. However, there were no examples of courses teaching hybrid app development that I could find. Instead, I suspect that students are self-teaching, even when the framework is used for a project in a class.

Academic research does show use of Cordova and Ionic in higher education for research projects, but no suggestions were made regarding how the researchers originally learned mobile app development. I suspect that the online lecture is the prevailing media, however this tends to be sub-optimal. Video lectures are expensive to product, and the material is quickly out of date (once again, this is based on my own experience); each hybrid framework does monthly releases. The native frameworks themselves too represent a challenge, as they introduce annual major version releases. Various techniques of mobile development are demonstrated in academic writing, however little focus is given on how the learner went about familiarizing themselves with mobile platform challenges and development framework specifics.

@que2016 does mention some of the potential benefits of teaching hybrid development, such as the time to master the material. Many presumptions were made regarding the ease of developing using JavaScript and HTML when compared with native app languages like Objective-C and Java. While I personally agree with these statements, I didn't find comfort in these statements being made without evidence of citation, survey, or study. I also found that from time to time the author referred to applications written with the Cordova as being developed in HTML5, which didn't honestly represent the effort – while UI is written in HTML, the functionality is written in JavaScript.

In the materials I found discussing courses and materials for teaching mobile app development [@payne2014teaching; @sprinkle2011teaching; @mahmoud2010mobile; @hu2012curriculum], the approach generally was consistent. First, they presented the architecture for their curriculum and positioned it against other types of development. Then, the tools needed for the learners are presented. Finally, a course overview is presented listing the typical assignments. Analysis is done on the outcomes of this curriculum demonstrating its effectiveness and adoption. This approach seems commonplace.

# The Problem to Study

Recently, I've begun working as a community team member on the React Native project. This is an open-source hybrid mobile development framework created by Facebook. My contributions to date have been in organizing and writing the changelog and managing the channel for community release discussion. What I've anecdotally observed is that students learn React Native far differently from native mobile frameworks. I plan to focus on the following aspects of learning hybrid mobile development:

**How do developers learn hybrid mobile app frameworks, and how are the frameworks perceived by learners?**

Below is a draft of research questions that may be considered to guide investigating this question:

**RQ1: Do engineers find learning hybrid development simpler than learning traditional native application development?**

**RQ2: Where do developers learn hybrid development?**

**RQ3: How widely are hybrid mobile app development frameworks included in university undergraduate programs?**

## References