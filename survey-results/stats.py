#!/usr/bin/env python
"""
This file runs all of the statistical analyses used for this research project
"""

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

df = pd.read_csv("survey-results-filtered-coded.csv", delimiter=",")

def calculate_total_tool_usages():
    total_usages = df[['stack_overflow','blog','microblog','online_class','book','peer_discussion','hackathon','professional_workshop','university_class','documentation','reference_implementation','source_code','chat']].sum(axis=0)
    print "## Tool Usage"
    print total_usages
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
    print stats.chisquare(total_usages.values)
    print ''

def calculate_best_tool():
    best_tool = df.groupby('best_tool')['best_tool'].count()
    print "## Favorite Tools"
    print best_tool
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
    print stats.chisquare(best_tool.values)
    print ''

def does_satisfaction_vary_with_tool():
    coded_results = df.groupby('best_tool')['needs_satisfied'].apply(list).drop(best_tools_with_fewer_than_5_respondents)
    print '## Satisfaction by Tool'
    print df.groupby('best_tool')[['needs_satisfied']].mean()
    print '### Kruskal Wallis test'
    print stats.kruskal(*coded_results)
    print ''

def does_satisfaction_vary_with_unit_completion():
    coded_results = df.groupby('best_tool')['completed_learning_unit'].apply(list).drop(best_tools_with_fewer_than_5_respondents)
    print '## Completion by Tool'
    print coded_results
    print '### Kruskal Wallis test'
    print stats.kruskal(*coded_results)
    print ''

def tool_completion():
    coded_results = df.groupby('best_tool')['completed_learning_unit'].agg([lambda val: val.count() - val.sum(), 'sum']).rename(columns={'sum': 'Completed Unit', '<lambda>': 'Didn\'t Complete Unit'}).drop(best_tools_with_fewer_than_5_respondents)
    print '## Completion vs Non Completion by Tool'
    print coded_results
    usage_plot = coded_results.plot(kind='bar', title='Tool Usage', colormap='Set3')
    usage_plot.set_xlabel("")
    usage_plot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    usage_plot.set_ylabel("Number of respondents")
    usage_plot.set_xticklabels(['Stack Overflow', 'Blog', 'Online course', 'Peer discussion', 'Documentation'])
    figure = usage_plot.get_figure()
    figure.set_tight_layout(True)
    figure.savefig("completion_by_tool.pdf")
    plt.close()
    print ''

def learning_in_response_to_change():
    coded_results = df['was_learning_in_response_to_change'].value_counts()
    print '## Learning in Response to Change'
    print coded_results
    learning_plot = coded_results.plot(kind='pie', title='Was Learning in Response to Change', colormap='Set3')
    learning_figure = learning_plot.get_figure()
    learning_figure.set_tight_layout(True)
    learning_figure.savefig("learning_in_response_to_change.pdf")
    plt.close()
    print ''

def how_soon_was_it_used():
    coded_results = df['how_soon_was_it_used'].value_counts()
    print '## How Soon Was It Used'
    print coded_results
    learning_plot = coded_results.plot(kind='pie', title='How Soon Was It Used', colormap='Set3', autopct='%1.1f%%', labels=None, shadow=True, startangle=90)
    learning_plot.set_ylabel("")
    learning_plot.legend(coded_results.index, loc='best', prop={'size': 8})
    learning_plot.axis('equal')
    learning_figure = learning_plot.get_figure()
    learning_figure.set_tight_layout(True)
    learning_figure.savefig("how_soon_was_it_used.pdf")
    plt.close()
    print ''

best_tools_with_fewer_than_5_respondents = df['best_tool'].unique()[df['best_tool'].value_counts() < 5]
calculate_best_tool()
calculate_total_tool_usages()
does_satisfaction_vary_with_tool()
does_satisfaction_vary_with_unit_completion()
tool_completion()
learning_in_response_to_change()
how_soon_was_it_used()
