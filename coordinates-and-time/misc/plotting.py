
x_ticks = ax.get_xticks()
x_ticks = [datetime.utcfromtimestamp(xi) for xi in x_ticks]
x_labels = [d.strftime(datefmt) for d in x_ticks]

ticks_loc = ax.get_xticks().tolist()
ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
ax.set_xticklabels(x_labels)
