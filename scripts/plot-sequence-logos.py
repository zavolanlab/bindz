###############################################################################
#
#   Script to plot sequence logos for motifs
#
#   AUTHOR: Krish Agarwal
#   AFFILIATION: University_of_Basel
#   CONTACT: akrish136@gmail.com
#   CREATED: 02-08-2020
#   LICENSE: Apache_2.0
#
###############################################################################

import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import logomaker
from argparse import ArgumentParser, RawTextHelpFormatter

##### Using argparse to get input from command line #####
parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)

parser.add_argument(
    "--input_file",
    dest="input_file",
    help="input files for sequence logos",
    required=True,
    metavar="FILE",
)

parser.add_argument(
    "--output_location",
    dest="output_location",
    help="location where the png logos will be saved",
    required=True,
    metavar="DIR",
)

try:
    options = parser.parse_args()
except Exception:
    parser.print_help()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

#### Storing commnad line arguments in variables ####
input_file = options.input_file
output_location = options.output_location


main_file = str(input_file)
main_file_temp = (
    main_file + "_temp"
)  # create a temporary file which will store only the required data
main_file_temp2 = (
    main_file + "_temp2"
)

filename = os.path.split(main_file)[-1]  # filename of the input file

#### Calculate total number of lines in the file ####
j = 0
with open(main_file) as f:
    for line in f:
        j = j + 1

#### Copy the contents of the file to temp except 1st, 2nd and last line ####
i = 0
with open(main_file) as f:
    with open(main_file_temp, "w") as f1:
        for line in f:
            if i != 0 and i != 1 and i != j - 1:
                f1.write(line)
            i = i + 1

#### Logic to replace T with U in temp file ####            
fin = open(main_file_temp, "rt")
fout = open(main_file_temp2, "wt")

i=0
for line in fin:
    words = line.split()
    if(i!=0 and float(words[1]) == float(words[4]) == float(words[2]) == float(words[3]) == 25.0):
            line = words[0] + "\t25.0\t25.0\t25.01\t24.99\n"
    fout.write(line.replace('T', 'U'))
    i = i+1

fin.close()
fout.close()

crp_matrix_df = pd.read_csv(
    main_file_temp2, delim_whitespace=True, index_col=0
)  # read csv and convert to dataframe
crp_matrix_df.head()

#### Delete the temporary files ####
os.remove(main_file_temp)  
os.remove(main_file_temp2)

prob_mat = logomaker.transform_matrix(
    crp_matrix_df, from_type="probability", to_type="information"
)
logo = logomaker.Logo(
    prob_mat,
    fade_probabilities=True, ## will fade the smaller probabilities
    stack_order="small_on_top",
)

final_png = os.path.join(output_location, filename)  # location for saving the file
final_png = final_png + ".png"

axes = plt.gca() # get current axes of the plots
axes.set_ylim([0, 2]) # set the y-axis limits from 0 to 2

#### Hide the top and the right axes of the plot ####
axes.spines['right'].set_color('none') 
axes.spines['top'].set_color('none')
axes.spines['left'].set_color('none')

plt.savefig(final_png)  # final png saved
