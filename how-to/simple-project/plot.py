import numpy as np

import matplotlib.pyplot as plt

# Try to match font used in document in which plot will be embedded.
# If you plan on presenting on screen and including in a paper, you may want
# to have two versions of the plot with different font sizes.
plt.rcParams.update({'font.size': 14, 'font.family': 'Times New Roman'})

lines = np.load('data/lines.npy')
# Here I've colored everything black because I don't thing additional colors
# will add more clarity.
plt.plot(lines[0,:,:], lines[1,:,:],'k')
plt.plot(lines[0,0,:], lines[1,0,:],'k.')
plt.xlabel('y or L')
plt.ylabel('z', rotation=0) # If label is short, I rotate to make easier to read.
plt.axis('equal') # So the field lines are not distorted by non-unity aspect ratio.
plt.title('Field lines for dipole at (y, z) = (0, 0)')
plt.grid()

# Save PNG for copy/paste into PPT. Save SVG for viewing in browser. Save PDF
# Also if plot will be put into a LaTeX document.
plt.savefig('figures/field_lines.png', dpi=300)
plt.savefig('figures/field_lines.svg')
#plt.savefig('figures/field_lines.pdf')

plt.show() # Needed if this script is executed from the command line.
