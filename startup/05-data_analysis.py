# data analysis

# %lifelines
@register_line_magic
def lifelines(line):
    s = ("from pandas import DataFrame, Series\n"
        "import lifelines\n"
        "from lifelines import KaplanMeierFitter, NelsonAalenFitter, AalenAdditiveFitter, CoxPHFitter"
        )
    _ip.run_code(s)

# %stats
@register_line_magic
def stats(line):
    _ip.run_code("import scipy.stats as stats")
    _ip.run_line_magic("lifelines", line)


del stats, lifelines
