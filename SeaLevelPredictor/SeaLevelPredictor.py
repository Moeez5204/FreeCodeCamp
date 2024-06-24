import os.path
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


data_path = 'epa-sea-level.csv'

df  = pd.read_csv(data_path)

year = df['Year']
CSIRO = df['CSIRO Adjusted Sea Level']

plt.scatter(year,CSIRO)

slope,intercept,R,P,STD = linregress(year,CSIRO)
plt.plot(year,intercept+slope * year,label = 'line of best fit')

Future_Years = range(1880,2050)

plt.plot(Future_Years,intercept + slope * Future_Years,linestyle = "--",label = "Prediction 2050",color = 'green' )

plt.title("Sea level Regression")
plt.xlabel("Year")
plt.ylabel("CSIRO Adjusted Sea Level")
plt.grid(True)
plt.legend()
plt.tight_layout()

script_dir = os.path.dirname(os.path.abspath(__file__))
output_filename=os.path.join(script_dir,'Scatter_Figure')
plt.savefig(output_filename)

plt.show()




def draw_plot():

    plt.savefig('sea_level_plot.png')
    return plt.gca()