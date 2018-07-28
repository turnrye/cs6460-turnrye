---
title: Learning Rapidly Changing Frameworks
author:
- name: Ryan Turner
  email: rturner63@gatech.edu
  affiliation: Georgia Institute of Technology
abstract:
  Developers often face difficulties when learning new frameworks that are volatile -- ones that are quickly changing and have little long-term support and feature-deprecation periods. As teams work to improve developer experience, they must take into account how developers learn these frameworks and produce learning materials that best meet the developers needs. Informal learning is well understood, and many learning tools have been examined for use by developers. This research seeks to answer how developers learn rapidly-changing frameworks.

  38 developers responded to a brief survey with details about how they learned React Native, a current example of a rapidly changing framework. This survey looked at the respondent's background, the tools they used in the past, and details of their experience over the previous 90 days. The data was compared to normal distributions to look for preferences and patterns.

  Developers were shown to have favorite tools and commonly used tools, though the two didn't directly align. Learning was immediately put to use in most cases. Developers most often did not complete all of the materials, but they still had positive outcomes. Over one-third of developer's learning during the period was a result of changes in the framework itself.

  While this research specifically examined React Native, many of the learner preferences may be applied to other frameworks and technologies. A learner behavioral pattern emerges that may be considered to build more effective educational material.
keyword: 
- just in time
- framework
- rapidly-changing
---

# Introduction

Studying rapidly-changing technology like augmented reality and artificial intelligence most often takes the form of informal learning. For these, often documentation and samples are all the materials provided. Looking at more established topics like desktop computing and service management, the case is quite different. Corresponding certifications exist like CompTIA A+ and ITIL Foundation with accompanying curriculum and a network of professional teachers. Learning options vary greatly as the technology's maturity level changes. While computer science as a whole is a young practice compared to other kinds of engineering, certain topics pose bigger challenges to learners.

There is a wide body of knowledge on informal learning, as well as learning by developers. However, there has not been significant study on how learning occurs in various contexts. One such context is in the use of a framework, which is defined as "a form of software reuse that primarily promotes the reuse of entire architectures within a narrowly defined application domain" [@pasetti2002software]. Couple that framework with rapid change, and learners show behaviors best summarized as "just in time learning".

**How do developers learn rapidly-changing frameworks?**

To answer this question, the "where, when, and why" are considered. Specifically, the three following research questions are investigated:

**RQ1: What learning tools are preferred?**

Understanding what tools are preferred helps to identify what traits developers prefer in their tools, as well as what content creators use. In pursuing this, various tools for learning will be considered. Some examples include institution-sponsored courses, massive open online courses (MOOCs), books, weblog tutorials, forum and knowledge market threads, workshops, and even hackathons. This can answer what best suits rapidly-changing frameworks. This detail represents **where** the learning occurs.

**RQ2: Is their learning motivated by a pressing need?**

When working with rapidly changing frameworks, developers may choose to learn just-in-time to solve a new problem. Other developers may instead respond to rapid change by closely following progress and proactively learning new materials. These two are enabled by different kinds of educational content: the former needs to be problem based and easily found, whereas the latter needs to be more engaging and use constructionism. This detail represents **when** the learning occurs.

**RQ3: What scope of knowledge do developers pursue?**

The scope of learning tools widely varies, from weeks-long MOOCs to ten-minute read weblog posts. This question asks whether the learner is studying to move on with their day or instead to better understand something they already practice. They may be using tools entirely, piece-meal, or just referencing code snippets. This answers **why** the learning occurs. 

# Related Work

Learning rapidly-changing frameworks is most often informal, which is defined as learning with little structure and often as the byproduct of some other activity [@marsick2001informal]. It is "relevant to practice in many cultures and contexts" and "[takes] place wherever people have need, motivation, and opportunity for learning" [@marsick2001informal]. While this method is often looked at from a business context [@marsick2001informal; @noe2014learning], motivation could come as uncertainty of creating a new solution or resolving a bug in code. Informal learning is also often defined by a social component. For example, while the trigger may be local to an individual, it is often the result of an external change such as results of a tester's work or a request from a product owner. Informal learning takes place around frequently and regularly.

Significant literature exists covering various kinds of informal learning tools and the way that they are consumed. Developers have many solutions available for learning. The next paragraphs describe the informal learning activities that take place within a subset of these.

In research of programmer's tool usage, peer interaction leads to learning and discovery [@murphy2011peer]. Discovery is more specifically called "the first stage of some kinds of learning." @murphy2011peer contrasts peer interaction from Marsick's definition of informal learning; however, when considered according to the definition above, the distinctions fade. In this work, @murphy2011peer demonstrates how situations like happenstance interaction, pair programming, and even change notification often result in peer observations and recommendations. These represent the "discoveries" of tools, but in some cases they also represent the teaching material itself: with pair programming, the peer interaction often creates an incidental situated learning experience.

Hackathons are presented as "excellent informal learning platforms" [@nandi2016hackathons]. A hackathon is a "fast-paced event where competitors work in teams to go from an idea to working software or hardware within a single day or a weekend." Peer learning is common place in this setting. Consistent with the definition of informal learning, at hackathons the problems create the need, the gamification create the motivation, and the industry mentors plus online resources create the opportunity. While the research focuses on learnings within teams, they also recognize that the learning environment created at a hackathon excels at producing industry-relevant learnings and skills. It is considered a "great opportunity to learn" by participants [@nandi2016hackathons]. Frameworks may be introduced or reviewed at these events, though the researchers did not consider this.

MOOCs present as popular online digital learning tools today. Popular examples include Coursera, edX, and Udacity. When considering learning theories within MOOCs, there tend to be either connectivism-driven MOOCs (cMOOCs) or extension MOOCs (xMOOCs) [@yousef2014review]. These are significantly different in their application of learning models, and more needs to be done to make use of informal, personalized, or professional learning on these platforms [@yousef2014review]. From anecdote, MOOCs appear to be a popular tool to learn frameworks.

Informal learning, specifically by developers about emerging topics, relates to the following statement: "What antecedents and conditions facilitate continuous learning, especially informal learning, and knowledge sharing?" [noe2014learning]. In considering the form of learning, @noe2014learning mention that "informal learning may be equally important to or even more important than other forms of learning." In fact, informal learning is so prevalent in organizations that it may account for up to 75% of learning [@noe2014learning; @bear2008tapping]. Yet, the future issue is still proposed: "What are the antecedents and consequences of informal learning?" [@noe2014learning].

# Methodology

![Respondents had varied experience levels with JavaScript. \label{goodExperience}](../survey-results/js_experience.pdf){ width=50% height=40% }

![Respondents had varied experience levels with React Native. \label{reasonableUse}](../survey-results/rn_familiarity.pdf){ width=50% height=40% }

To better understand learning in this area, developers use of learning tools was reviewed. Ideally, developers would have been observed in their learning. Instead, a survey approach was taken. This is partly due to the feasibility to observing these interactions as well as the importance of capturing responses from a diverse audience. Finally, this approach permitted developers to report on their perceptions of the learning: why did it occur, how successful was it, and how soon was it put to use. Much of this would be lost by an outside observer.

The sample population used was limited to React Native practitioners and their use of the framework. This helped the survey target a cohesive group of respondents, and the author's networking in the community aided in soliciting responses. React Native is a widely used framework with the second highest contributor count on GitHub in 2017 [@githuboctoverse]. Its varied population of users coupled with its pre-stable status makes for an excellent case as a rapidly changing framework to study.

A questionnaire survey was promoted through Twitter, chatrooms, mailing lists, and signs at a conference. Many respondents did not qualify for the survey and had their responses removed due to inexperience with the framework. Of those who remained, most were professional developers who had a medium-to-light level of experience with JavaScript (see figure \ref{goodExperience}). About half of the respondents were beginner React Native users, and the rest of the respondents were evenly split between completing a single project, completing multiple projects, and daily use (see figure \ref{reasonableUse}).

The questionnaire survey starts by asking about the respondent's experience professionally, formal learning in programming, experience with JavaScript, and familiarity with React Native. React Native familiarity was used as a filtering question; if the respondent indicated no familiarity, the survey ended.

For respondents who were familiar with React Native, they were then asked questions about their learning and use in the previous 3 months. This was time limited in order to avoid asking the respondent to describe experiences beyond recollection. First, the respondents were asked "What learning tools have you used? Check all that apply." 11 options for this question were presented, plus an unstructured other option. These options wildly varied between the formal and informal, small and large. Respondents were then asked to estimate how much of their time was spent learning as a percentage of their overall work, though this data did not produce meaningful results. Next, they were asked what tool was the most useful to them. The remainder of the questions asked were limited to their use of that tool, seeking to understand when the learning took place, how it was used, and how beneficial it was.

The respondent data was collected and then reviewed. Python *pandas* was utilized in order to interpret the data and send it to *Scipy.stats* module and *matplotlib* for analysis and visual representation. Using this approach, some basic counts and pivot tables provide insights to respondent's preferences, and analyses like the chi square test and the Kruskal Wallis test were utilized to calculate statistical significance on the data.

# Results

Overall, 38 subjects provided qualified survey results. In this section, answers to the three research questions and general trends in the data are presented.

## Specific tools are preferred, but usage doesn't necessarily follow

Respondents indicated 172 different instances of tool usages in the past 3 months. Developers showed that specific tools were used more frequently than others. A chi-squared test comparing the results to a normal distribution resulted in $p=5.80\times 10^{-18}$. Clear leaders in tool usage included Stack Overflow, Blogs, and Documentation. Online classes, peer discussion, and project examples were middle of the pack performers. The least commonly used tools included source code, hackathons, chat, workshops, university courses, books, and microblogs. The tool usage frequency is indicated in figure \ref{toolUsage}.

![A clear preference for specific learning tools emerged. \label{toolUsage}](../survey-results/tool_usage.pdf){ width=50% height=40% }

Each subject was asked to indicate a single preferred learning tool. A chi-squared test comparing the results to a normal distribution resulted in $p=0.063$. There was a clearer split between winners and losers in this area; the winners were stack overflow, blogs, online classes, books, and peer discussion; all other tools had significantly less learner preference. Documentation and examples, which showed average and above average usage occurrence, notably received no selections. The tool usage frequency is indicated in figure \ref{toolPreference}, with categories that received no selections omitted.

Some selections like hackathons, workshops, and microblogs were indicated as favorites by their only users. This is likely a result of users having an individual recent or highly significant learning session rather than a recurring learning pattern.

![Developers indicated more polarized tool preference than usage. \label{toolPreference}](../survey-results/best_tool.pdf){ width=50% height=40% }

## Most learning was applied the same day

In the general case, respondents indicated how soon they used what they learned. $55.3\%$ of respondents indicated that it was immediately put to use. The second most common time delay was a day or so at $15.8\%$. The remainder of responses was nearly evenly split between many days, not yet, and it was to explain an existing usage. For specific occurrences, refer to figure \ref{howSoon}.

![Nearly three-quarters of usage occurred within a day. \label{howSoon}](../survey-results/how_soon_was_it_used.pdf){ width=50% height=40% }

While learners are following just-in-time learning practices, the specific reasons for this weren't well understood. $34.2\%$ of learners were responding to changes in the framework as indicated in figure \ref{changeResponse}. Other reasons like new feature needs, inexperience, and curiosity weren't evaluated but likely contributed.

![Over one-third of developers learning rapidly changing frameworks were doing so in response to a change in the framework. \label{changeResponse}](../survey-results/learning_in_response_to_change.pdf){ width=50% height=40% }

## Learners generally don't complete the full learning unit, but it's still useful

Learning module completion varied by tool. Tools with fewer than 5 responses were removed due to sample size being too small. With the resulting dataset, a Kruskal-Wallis test comparing the number of completions vs non-completions grouped by tool resulted in $p=0.053$. Stack Overflow specifically showed an 8:1 ratio of non-completions to completions, while blogs showed 1:6. Online courses and peer discussions showed a 2:1 ratio, and documentation was even. Refer to figure \ref{completionByTool} for a visual representation.

![Learning unit completion varied highly by tool. \label{completionByTool}](../survey-results/completion_by_tool.pdf){ width=50% height=40% }

Despite generally not completing the full unit, user satisfaction was high. Figure \ref{learnerSatisfaction} shows that the most popular selection was a 4 out of 5 on satisfaction. Blogs likely present in a way that promotes complete consumption, perhaps by presenting significant information on a cohesive topic until the very end.

![Learners are generally satisfied, though there is still more room to improve. \label{learnerSatisfaction}](../survey-results/needs_satisfied.pdf){ width=50% height=40% }

# Limitations

This research surveyed the community that uses React Native. Both the way the data was collected and the population surveyed present as limitations to this work's generalized contributions. While this work may apply to other web or mobile frameworks, some of the presumptions made may not match those for others.

In the sample used for this work, the social norms practiced by the developers may show favoritism to specific tools and methods of consumption. React Native was originally developed and is presently supported by Facebook [@facebook], a social networking company. On the developer support page, Stack Overflow, forums, chat, and microblogs are all suggested as ways to get help [@facebook]. As a result of the framework's recognition of these, other tools may be at a disadvantage. In fact, as of July 2018, there are no references to books or courses in the support documentation.

Additionally, React Native shares a lot in common with ReactJS, a JavaScript web frontend framework. Users of React Native often come from a web development background, which has many differences with software development. Detailed analysis of the difference can be found in @mendes2014web, but of specific interest are differences in application characteristics, people involved in development, and social issues. These differences likely limit the applicability of this work.

The challenges of React Native's mission also limit the application of this research. React Native ultimately creates iOS and Android mobile applications and relies on their native APIs to enable much of its functionality. The learner frequently is required to look at these upstream projects, which expands the scope of learning beyond what other frameworks may require. This also puts users in the position of watching for changes in the parent APIs in order to anticipate future work in React Native. For instance, React Native's [0.56 release](https://github.com/react-native-community/react-native-releases/blob/master/CHANGELOG.md#056) responds to many previously announced changes in dependencies like Babel, iOS API, Xcode IDE, and Android SDK. Developers working on the React Native platform are sometimes forced to learn just-in-time with the framework's change even though it's highly anticipated; learners of frameworks with simpler dependency trees may not be forced into this pattern.

This research was conducted by surveys alone, which limited how the subjects were interrogated. To help increase response rate, the length of the survey was limited. Respondents were asked detailed questions only about their most useful tool; research of tools beyond their favorite may reveal other usage patterns. Additionally, in making the survey straight forward for the respondents, some statistical analysis was made more complicated. More traditional survey design may result in better data.

Finally, some aspects of the survey asked about a 90 day time period. This is a long time for respondents to recollect, so there may be inaccuracies in their reporting. Additionally, within this time period learning may have occurred for multiple reasons. Respondents were asked about a single occurrence, not the entire set. The problems faced may be related to current events in the framework, like a defect in the most recent release or an emerging trend in user interface design. These specific, widespread cases may skew the responses to the learning patterns that best address that issue rather than issues in general.

# Conclusion

Software developers often have formal learning backgrounds, yet much of their technical contributions come from informal learning. While various kinds of informal learning tools have been studied, there is little understanding of how they are used, especially in emerging technologies. In fact, learning tools like MOOCs and peer discussion have been studied to understand their contributions to developer knowledge, but this has generally been oriented from the specific tool perspective or informal learning overall.

Developers using rapidly-changing frameworks often need to use areas that are new, or are impacted by changes to existing areas they already use. In this use, learners have specific sets of tools they depend on day-to-day and primarily preferences. Most knowledge is immediately put to use. Learners generally don't complete the full course, but that doesn't mean there are subpar learning outcomes. In general, learners reported high satisfaction.

Developers were polled about their learning React Native, which is a leading mobile development framework with many industry sponsors. With monthly releases that have hundreds of contributions, there is a lot of regular change. Its developers generally are working in JavaScript, and some web technologies are used. This population may not be like others outside of the mobile and web development space.

# Future Work

This study may be considered a pilot study. More data is needed and the survey needs updating to reach more substantial conclusions. Detail about tool specific learning outcomes may be possible, and correlations between learning tool usage and overall learning duration may also be possible. Additionally, future work with this survey could restructure answers to result in data that is more practically analyzed.

Originally, interview surveys were planned as well to collect qualitative data and investigate the motivation behind learning. Low survey participation prevented this from occurring. While surveys did not take place, a survey script was prepared and is available for future use in [the repository](https://github.com/turnrye/learning-rapidly-changing-frameworks).

## References