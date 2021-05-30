#############################################
# HOMEWORK 1: Running Python code from the command line.
#############################################

# You are expected to run a python file with "py" extension from the command line.
# For example, you have a file named hi.py and have the code print("name, surname") in it.
# Open the console of your computer, go to the directory where the hi.py file is located, and code "python hi.py" from there.
# When you run it, "name, surname" should be written on your screen.
# It is explained how to do it step by step.

# Step 1: Create python file named "hi.py" in PyCharm.
# Step 2: Write the following code in this file and save it: print("I'm Burak Kanber HOMEWORK OK, it's very easy")
# Step 3: Now you need to navigate to the directory (folder) where the "hi.py" file is located from the console.
# Fortunately, it's easy with PyCharm. In the menu on the left, whichever folder the hi.py file is in
# Right click on that folder and select: "open in > terminal".
# Terminal screen will open at the bottom of PyCharm. You are now in the same directory (folder) as the hi.py file.
# Step 4: In the console you should write the following code: python hi.py
# Step 5: Take a screenshot of your output and share it in your group.

###############################################
# HOMEWORK 2: Create a virtual environment with your own name and do the following.
###############################################
conda env list
###############################################
# Task 1: Create a virtual environment under your own name, install python 3 during creation.
###############################################
conda create -n bkanber python=3
###############################################
# Task 2: Activate the environment you created.
###############################################
conda activate bkanber
###############################################
# Task 3: List the installed packages.
###############################################
conda list
###############################################
# Task 4: Download the current version of Numpy and version 1.2.1 of Pandas into Environment at the same time.
###############################################
conda install numpy pandas=1.2.1
###############################################
# Task 5: What is the version of the downloaded Numpy?
###############################################
conda list numpy
###############################################
# Task 6: Upgrade Pandas. What is the new version?
###############################################
conda upgrade pandas
###############################################
# Task 7: Delete Numpy from environment.
###############################################
conda remove numpy
###############################################
# Task 8: Download the Seaborn library and the matplotlib library with their current versions at the same time.
###############################################
conda install seaborn matplotlib
###############################################
# Task 9: Export the libraries in the virtual environment with the version information and examine the yaml file.
###############################################
conda env export>bkanber.yaml
###############################################
# Task 10: The environment you created is deleted.
###############################################
conda deactivate
conda env remove -n bkanber
# Hint: Deactivate environment first.





###############################################
# ASSIGNMENT 3: List Comprehension Applications
###############################################

###############################################
# Task 1: Capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.
###############################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# Read the data set from the beginning and try to obtain the following output.

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notes:
# Non-numeric names should also grow.
# Must be done with a single list comp structure.


###############################################
# Task 1 Solution
###############################################
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

# Primitive method:
A = []
for col in df.columns:
    if df[col].dtype != "O":
        A.append("NUM_" + col.upper())
    else:
        A.append(col.upper())

df.columns = A

# If we do it with the comprehension method:
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
###############################################
# Task 2: Write "FLAG" AT THE END of the variables that do NOT contain "no" in their name.
###############################################

# Notes:
# All variable names must be uppercase.
# A single list should be made with comp.

# Expected output:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']

###############################################
# Task 2 Solution
#############################################
# With the primitive method:
df = sns.load_dataset("car_crashes")
df.columns
A = []
for col in df.columns:
    if "no" not in col:
       A.append(col.upper()+"_FLAG")
    else:
        A.append(col.upper())
df.columns = A

# With the comprehension method:
[col.upper()+"_FLAG" if "no" not in col else col.upper() for col in df.columns]
###############################################
# Task 3: Create a new df by selecting the names of the variables that are DIFFERENT from the variable names given below.
###############################################

# df.columns
# og_list = ["abbrev", "no_previous"]

# Notes:
# First, create a new list named new_cols using list comprehension according to the list above.
# Then create a new df by selecting these variables with df["new_cols"] and name it new_df.

# Expected output:

# new_df.head()
#
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630


###############################################
# Task 3 Solution
#############################################
# With the primitive method:
df = sns.load_dataset("car_crashes")
df.columns
og_list = ["abbrev", "no_previous"]
new_cols = []
for col in df.columns:
    if col not in og_list:
        new_cols.append(col)

new_df = df[new_cols]
new_df.head()

# With comprehension method:
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()
