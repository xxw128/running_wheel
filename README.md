# running_wheel
Mouse activity from running_wheels

For data file 2017_0628_c57.csv
1. run data_parser.py
 In iPython: run the following line:
 %run data_parser.py 2017_0628_c57.csv
 This generates four new files
    2017_0628_c57_values.csv
    2017_0628_c57_values_1h.csv
    2017_0628_c57_mouse_info.csv  
    tidy_data.csv

2. manually do the date shift for mouse id 19-22: delete first 24 hours
    of values, shift cells up. Save the file as tidy_data_shifted.csv

3. to plot using plot_by_date.py
        in iPython, run the following line:
        %run plot_by_date.py 'tidy_data_shifted.csv'
    Save the figure
