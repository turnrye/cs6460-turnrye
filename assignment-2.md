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
  - family: Apple
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
---
# Ryan Turner's Assignment 2

I'd like to focus on a research track for this course. This was a rather straight forward decision for me, as in the past I've worked on both materials and development of educational tech: I did this as part of my job to help onboard new team members. In my undergraduate studies, I worked in a biology research lab helping with bioinformatics. I did not have the chance to participate in any of the writing; given the opportunity today, I'd like to do that.

Recently, I've begun working as a community team member on the React Native project. This is an open-source hybrid mobile development framework created by Facebook. My contributions to date have been in organizing and writing the changelog and managing the channel for community release discussion. What I've anecdotally observed is that students learn React Native far differently from other mobile frameworks. I plan to focus on the following aspects of learning hybrid mobile development:

**How do developers learn the React Native framework, and how is it perceived by its learners?**

**RQ1: Do engineers find learning React Native development simpler than learning traditional native application development?**

**RQ2: Where do developers learn React Native development?**

**RQ3: How widely are hybrid mobile app development frameworks included in university undergraduate programs, like lesson plans and course projects?**

@que2016 inspired the first question, however I found a number of the conclusions made to be unsubstantiated. Many presumptions were made regarding the ease of developing using JavaScript and HTML when compared with native app languages like Objective-C and Java. While I personally agree with these statements, I didn't find comfort in these statements being made without evidence of citation, survey, or study. I also found that from time to time the author referred to applications written with the Cordova as being developed in HTML5, which didn't honestly represent the effort – while UI is written in HTML, the functionality is written in JavaScript. I think RQ1 warrants further research.

The second research question was motivated by my own personal experience. In my university studies, I had learned iOS development, and here at the OMSCS program I've had the opportunity to learn Android development. Partly this is due to what materials and resources exist from the platforms themselves [@iosdeveloperuniversityprogram, @googledeveloperstraining]. I've also found Cordova and PhoneGap used in university projects. However, despite frequent use in industry, I've not found instances of React Native in a higher education setting. So, I'm interested to learn where developers are learning React Native. There are many online resources for this, however most are quickly out of date or low quality (once again, first hand knowledge). This question will look at both traditional school resources and online courses.

The third research question comes to help ground the rest of the research. For instance, if RQ2 turns out to scarcely mention university studies, we may find that it is not due to poor student learning outcomes but rather lack of exposure. I did find examples of courses and curriculums teaching both native iOS and Android development [@payne2014teaching, @sprinkle2011teaching] as well as honing in on a single platform (typically Android, since unlike iOS, development can take place on any computer) [@mahmoud2010mobile]. However, there were no examples of courses teaching hybrid app development that I could find. I instead suspect that students may be self-teaching, even when used for a project in a course.

## References