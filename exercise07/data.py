import numpy as np

D=0
R=1

# Data:
# From https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state
state_history_2016 = np.array([
[R,D,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,R,R,D,R,R,R,R,R],
[R,D,R,R,R,D,D,R,R,R,R,R],
[R,R,R,R,R,D,D,D,D,D,D,D],
[R,R,R,R,R,D,R,R,R,D,D,D],
[R,R,R,R,R,D,D,D,D,D,D,D],
[R,D,R,R,R,D,D,D,D,D,D,D],
[D,D,D,D,D,D,D,D,D,D,D,D],
[R,D,R,R,R,R,D,R,R,D,D,R],
[R,D,D,R,R,D,R,R,R,R,R,R],
[R,D,D,R,D,D,D,D,D,D,D,D],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,R,D,D,D,D,D,D,D],
[R,R,R,R,R,R,R,R,R,D,R,R],
[R,R,R,R,D,D,D,D,R,D,D,R],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,D,R,R,R,D,D,R,R,R,R,R],
[R,D,R,R,R,D,D,R,R,R,R,R],
[R,R,R,R,R,D,D,D,D,D,D,D],
[R,D,D,R,R,D,D,D,D,D,D,D],
[D,D,R,R,D,D,D,D,D,D,D,D],
[R,R,R,R,R,D,D,D,D,D,D,R],
[R,D,D,D,D,D,D,D,D,D,D,D],
[R,D,R,R,R,R,R,R,R,R,R,R],
[R,D,R,R,R,D,D,R,R,R,R,R],
[R,R,R,R,R,D,R,R,R,R,R,R],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,R,D,D,R,R,D,D,D],
[R,R,R,R,R,D,D,R,D,D,D,D],
[R,R,R,R,R,D,D,D,D,D,D,D],
[R,R,R,R,R,D,D,D,R,D,D,D],
[R,D,R,R,D,D,D,D,D,D,D,D],
[R,D,R,R,R,R,R,R,R,D,R,R],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,D,R,R,R,D,D,R,R,D,D,R],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,D,D,D,D,D,D,D,D],
[R,D,R,R,R,D,D,D,D,D,D,R],
[R,D,D,R,D,D,D,D,D,D,D,D],
[R,D,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,D,R,R,R,D,D,R,R,R,R,R],
[R,D,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,R,R,R,R,R,R,R,R],
[R,R,R,R,R,D,D,D,D,D,D,D],
[R,R,R,R,R,R,R,R,R,D,D,D],
[R,R,R,R,D,D,D,D,D,D,D,D],
[R,D,D,R,D,D,D,R,R,R,R,R],
[R,D,R,R,D,D,D,D,D,D,D,R],
[R,R,R,R,R,R,R,R,R,R,R,R]])

# State names
state_names = [
"Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"D.C.",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"]

# Same order as state_names.
# Data from 2012 column of https://en.wikipedia.org/wiki/Electoral_College_(United_States)#Chronological_table
state_electors = [9, 3, 11, 6, 55, 9, 7, 3, 3, 29, 16, 4, 4, 20, 11, 6, 6, 8, 8, 4, 10, 11, 16, 10, 6, 10, 3, 5, 6, 4, 14, 5, 29, 15, 3, 18, 7, 7, 20, 4, 9, 3, 11, 38, 6, 3, 13, 12, 5, 10, 3]



state_history = state_history_2016[:,:-1]
state_vote_2012 = state_history_2016[:,-2]
state_vote_2016 = state_history_2016[:,-1]

state_last_vote = state_vote_2012 # [v[-1] for v in state_history]
