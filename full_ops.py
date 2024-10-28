# full_ops.py
# Written by Rohan Palande
# Other contributors: None

# import Python modules

import math # math module
import sys # argv


# Initialize Script Arguments

c_in = float('nan') #input channel count
n_wv = float('nan') #number of weight vectors

# Parse Script arguments

if len(sys.argv)==3:
  c_in = float(sys.argv[1])
  n_wv = float(sys.argv[2])
  ...
else:
  print(\
   'Usage: '\
   'python3 full_ops.py c_in n_wv'\
  )
  exit()

# write script below this line
#Use class slides

c_out = n_wv
h_out = 1 
w_out = 1 
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0 

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
