import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def to_float(lst):
	return [float(x) for x in lst]

def parse_data(filename):
	xx = []
	total_rev = []
	tip_perc = []
	weather_feat = [[],[],[]]
	f = open(filename)
	for line in f:
		date,value = line.strip().split("\t")
		value = value.strip().split(",")
		value = to_float(value)
		xx.append(date)
		total_rev.append(value[0])
		tip_perc.append(value[1])
		# PRCP
		weather_feat[0].append(value[3])
		# SNWD
		# weather_feat[1].append(value[4])
		# SNOW
		weather_feat[1].append(value[5])
	return xx, [total_rev, tip_perc], weather_feat

def plot_hist_line(xx, hist_var,hist_label, line_var,line_label, title_label):
	plt.figure()
	hist_num = len(hist_var)
	line_num = len(line_var)
	x = np.array(range(len(xx)))
	# the histogram of the data
	hist_width = (1-0.1)/hist_num

	bar_color = ['lightblue','orange','lightgreen','b','c','m','g']

	fig, ax1 = plt.subplots()
	for i in range(hist_num):
		ax1.bar(x+i*hist_width,hist_var[i],color=[bar_color[i]], width = hist_width, label=hist_label[i])
	ax1.set_xlabel('Date')
	ax1.set_xticks(x,xx)
	#ax1.set_xticklabels(xx)
	# Make the y-axis label and tick labels match the line color.
	ax1.set_ylabel(' ', color='b')
	for tl in ax1.get_yticklabels():
		tl.set_color('b')
	
	ax2 = ax1.twinx()

	ax2.plot(x, line_var, 'r--',label=line_label[0])

	#ax2.plot(x,line_var[1],'g--')
	ax2.set_xlim([0, len(xx)])
	#print np.array(line_var).ndim

	ax2.set_xticks(x)
	ax2.set_xticklabels(xx)
	ax2.set_ylabel(' ', color='r')
	for tl in ax2.get_yticklabels():
	    tl.set_color('r')
	
	plt.setp(ax1.xaxis.get_majorticklabels(), rotation=70 )
	legend1 = ax1.legend(loc = [0,0.82])
	legend2 = ax2.legend(loc = [0.72,0.92])
	plt.setp(legend1.get_texts(),fontsize='xx-small')
	plt.setp(legend2.get_texts(),fontsize='xx-small')

	plt.title(title_label)
	#plt.show()
	save_label = "_".join(title_label.strip().split(" "))
	fig.savefig(save_label+'.png')

 
def plot_piechart(fracs,frac_label,title_label):
	# make a square figure and axes
	figure(1, figsize=(6,6))
	ax = axes([0.1, 0.1, 0.8, 0.8])

	# The slices will be ordered and plotted counter-clockwise.
	#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
	#fracs = [15, 30, 45, 10]
	explode=(0, 0.05, 0, 0)

	pie(fracs, explode=explode, labels=frac_label, 
		autopct='%1.2f%%', shadow=True, startangle=90)
		# The default startangle is 0, which would start
	    # the Frogs slice on the x-axis.  With startangle=90,
	   	# everything is rotated counter-clockwise by 90 degrees,
	    # so the plotting starts on the positive y-axis.

	title(title_label, bbox={'facecolor':'0.8', 'pad':5})
	save_label = "_".join(title_label.strip().split(" "))
	savefig(save_label+'.png')
	show()


def main():
	'''
	xx, rev_data, weather_feat = parse_data("revweather_weekly")
	plot_hist_line(xx,weather_feat,['PRCP (mm)','SNOW (mm)'],rev_data[0],['Total Revenue ($)'],'Total Revenue vs. Precipitation')
	plot_hist_line(xx,weather_feat,['PRCP (mm)','SNOW (mm)'],rev_data[1],['Tip Percentage (%)'],'Tip Percentage vs. Precipitation')
	'''

	frac_labels = ['TIRU', 'ALL TAXI', 'TAXIFLEET', 'GOTHAM YELLOW','WOODSIDE','TEAM SYSTEMS','MC GUINNESS','S & R MEDALLION','WHITE AND BLUE','QUEENS']
	fracs = [49,11,9,6,4,4,4,4,4,4]
	title_label='Top 10 Revenues'
	plot_piechart(fracs,frac_labels,title_label)
	
if __name__ == '__main__':
	main()
