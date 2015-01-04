# nice plotting functions.

# %pyplot, %plt, %plot
@register_line_magic('plt')
@register_line_magic('plot') #this is just alias: if I type plot, I better plot. 
@register_line_magic('pyplot')
@register_line_magic('pyploy') #common mispelling I make
def _pyplot(line):
    _ip.run_line_magic('matplotlib', line)
    _ip.run_code("""from matplotlib import pyplot as plt""")

    # use Bayesian Methods for Hackers plotting style
    _ip.run_code("""plt.style.use('bmh')""")

    # better hists
    def hist_(*args, **kwargs):
        kwargs.pop('alpha', None)
        kwargs.pop('histtype', None)
        kwargs.pop('normed', None)
        return plt.hist(*args, histtype='stepfilled', alpha=0.85, normed=True, **kwargs)

    # <3 figsize
    def figsize(sizex, sizey):
        """Set the default figure size to be [sizex, sizey].
        This is just an easy to remember, convenience wrapper that sets::
          matplotlib.rcParams['figure.figsize'] = [sizex, sizey]
        """
        import matplotlib
        matplotlib.rcParams['figure.figsize'] = [sizex, sizey]

    # aliases
    _ip.user_ns['hist_'] = hist_
    _ip.user_ns['figsize'] = figsize
    _ip.user_ns['plot'] = plt.plot
    _ip.user_ns['subplot'] = plt.subplot

del _pyplot
