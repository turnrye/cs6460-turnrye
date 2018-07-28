#!/usr/bin/env python
"""
This file runs all of the statistical analyses used for this research project
"""

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

df = pd.read_csv("survey-results-filtered-coded.csv", delimiter=",")

def respondent_background():
    print "## Background information"
    print ''
    print "```"
    print df.groupby('experience')['experience'].count()
    print df.groupby('formal_study')['formal_study'].count()
    print df.groupby('js_experience')['js_experience'].count()
    print df.groupby('rn_familiarity')['rn_familiarity'].count()
    print "```"
    print ''
    usage_plot = df.groupby('experience')['experience'].count().plot(kind='barh', title='Professional Experience', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_yticklabels(['Student', 'Full time', 'Related area'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("experience.pdf")
    plt.close()
    usage_plot = df.groupby('formal_study')['formal_study'].count().plot(kind='barh', title='Prior Formal Learning in Software Development', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_yticklabels(['No', 'Yes'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("formal_study.pdf")
    plt.close()
    usage_plot = df.groupby('js_experience')['js_experience'].count().plot(kind='barh', title='JavaScript Use', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_yticklabels(['Preferred language', 'Extensive use', 'Light use'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("js_experience.pdf")
    plt.close()
    usage_plot = df.groupby('rn_familiarity')['rn_familiarity'].count().plot(kind='barh', title='React Native Use', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_yticklabels(['Daily', 'Many projects', 'One project', 'Tinkerer'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("rn_familiarity.pdf")
    plt.close()

def calculate_total_tool_usages():
    total_usages = df[['stack_overflow','blog','microblog','online_class','book','peer_discussion','hackathon','professional_workshop','university_class','documentation','reference_implementation','source_code','chat']].sum(axis=0)
    print "## Tool Usage"
    print ''
    print "```"
    print total_usages
    print "```"
    print ''
    print "### Total sample count"
    print ''
    print "```"
    print total_usages.sum()
    print "```"
    print ''
    usage_plot = total_usages.plot(kind='bar', title='Tool Usage in Past 3 Months', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_xticklabels(['Stack Overflow','Blog','Microblog','Online Class','Book','Peer Discussion','Hackathon','Workshop','University Class','Documentation','Example','Source','Chat'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("tool_usage.pdf")
    plt.close()
    print '### Chi Square'
    print ''
    print "```"
    print stats.chisquare(total_usages.values)
    print "```"
    print ''

def calculate_best_tool():
    best_tool = df.groupby('best_tool')['best_tool'].count()
    print "## Favorite Tools"
    print ''
    print "```"
    print best_tool
    print "```"
    print ''
    usage_plot = best_tool.plot(kind='bar', title='Favorite Tool', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_xticklabels(['Stack Overflow','Blog','Microblog','Online Class','Book','Peer Discussion','Hackathon','Workshop','University Class','Documentation','Example','Source','Chat'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("best_tool.pdf")
    plt.close()
    print '### Chi Square'
    print ''
    print "```"
    print stats.chisquare(best_tool.values)
    print "```"
    print ''

def does_satisfaction_vary_with_tool():
    coded_results = df.groupby('best_tool')['needs_satisfied'].apply(list).drop(best_tools_with_fewer_than_5_respondents)
    print '## Satisfaction by Tool'
    print ''
    print "```"
    print df.groupby('best_tool')[['needs_satisfied']].mean()
    print "```"
    print ''
    print '### Kruskal Wallis test'
    print ''
    print "```"
    print stats.kruskal(*coded_results)
    print "```"
    print ''

def does_satisfaction_vary_with_unit_completion():
    coded_results = df.groupby('best_tool')['completed_learning_unit'].apply(list).drop(best_tools_with_fewer_than_5_respondents)
    print '## Completion by Tool'
    print ''
    print "```"
    print coded_results
    print "```"
    print ''
    print '### Kruskal Wallis test'
    print ''
    print "```"
    print stats.kruskal(*coded_results)
    print "```"
    print ''

def tool_completion():
    coded_results = df.groupby('best_tool')['completed_learning_unit'].agg([lambda val: val.count() - val.sum(), 'sum']).rename(columns={'sum': 'Completed Unit', '<lambda>': 'Didn\'t Complete Unit'}).drop(best_tools_with_fewer_than_5_respondents)
    print '## Completion vs Non Completion by Tool'
    print ''
    print "```"
    print coded_results
    print "```"
    print ''
    usage_plot = coded_results.plot(kind='bar', title='Tool Usage', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_xticklabels(['Stack Overflow', 'Blog', 'Online course', 'Peer discussion', 'Documentation'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("completion_by_tool.pdf")
    plt.close()

def learning_in_response_to_change():
    coded_results = df['was_learning_in_response_to_change'].value_counts()
    print '## Learning in Response to Change'
    print ''
    print "```"
    print coded_results
    print "```"
    print ''
    learning_plot = coded_results.plot(kind='pie', title='Was Learning in Response to Change', colormap='Set3', autopct='%1.1f%%', labels=None, shadow=True)
    learning_figure = learning_plot.get_figure()
    learning_plot.legend(coded_results.index, loc='best', prop={'size': 8})
    learning_plot.set_ylabel("")
    learning_plot.axis('equal')
    learning_figure.set_tight_layout(True)
    learning_figure.savefig("learning_in_response_to_change.pdf")
    plt.close()
    print ''

def how_soon_was_it_used():
    coded_results = df['how_soon_was_it_used'].value_counts()
    print '## How Soon Was It Used'
    print ''
    print "```"
    print coded_results
    print "```"
    print ''
    learning_plot = coded_results.plot(kind='pie', title='How Soon Was It Used', colormap='Set3', autopct='%1.1f%%', labels=None, shadow=True)
    learning_plot.set_ylabel("")
    learning_plot.legend(coded_results.index, loc='best', prop={'size': 8})
    learning_plot.axis('equal')
    learning_figure = learning_plot.get_figure()
    learning_figure.set_tight_layout(True)
    learning_figure.savefig("how_soon_was_it_used.pdf")
    plt.close()

def needs_satisfied():
    coded_results = df['needs_satisfied']
    print '## User Satisfaction'
    print ''
    print "```"
    print coded_results
    print "```"
    print ''
    learning_plot = coded_results.plot(kind='hist', title='User Satisfaction', colormap='Set3', bins=4, histtype='stepfilled')
    learning_plot.set_xlim((1,5))
    learning_plot.set_xticklabels(['Not satisfied (1)', '', '', '', '', '', '', '', 'Satisfied (5)'])
    learning_figure = learning_plot.get_figure()
    learning_figure.set_tight_layout(True)
    learning_figure.savefig("needs_satisfied.pdf")
    plt.close()

best_tools_with_fewer_than_5_respondents = df['best_tool'].unique()[df['best_tool'].value_counts() < 5]
respondent_background()
calculate_best_tool()
calculate_total_tool_usages()
does_satisfaction_vary_with_tool()
does_satisfaction_vary_with_unit_completion()
tool_completion()
learning_in_response_to_change()
how_soon_was_it_used()
needs_satisfied()
