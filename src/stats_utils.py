from scipy.stats import norm, beta, zscore, gamma
from math import sqrt

# the functions below aim to replicate the R function here:
# http://stat.ethz.ch/R-manual/R-patched/library/stats/html/power.prop.test.html


def sample_power_probtest(p1, p2, power=0.8, sig=0.05):
    z = norm.isf([sig/2]) #two-sided t test
    zp = -1 * norm.isf([power])
    d = (p1-p2)
    s =2*((p1+p2) /2)*(1-((p1+p2) /2))
    n = s * ((zp + z)**2) / (d**2)
    return int(round(n[0]))


def sample_power_difftest(d, s, power=0.8, sig=0.05):
    z = norm.isf([sig/2])
    zp = -1 * norm.isf([power])
    n = 2 * ((zp + z)**2) / (d**2)
    return int(round(n[0]))


def gab(m, s):
    """
    shape and scale of the gamma distribution
    Args:
        m: mean of the sample
        s: standard deviation of the sample

    Returns:

    """
    a = (1.0 * m / s) ** 2
    b = (s ** 2) / (1.0 * m)
    return a, b

def cohens_d(means=(), stdevs=(), N_samples=()):
    """
    cohens_d giving the effect size between group 1 and group 2

    see http://en.wikipedia.org/wiki/Effect_size#Cohen.27s_d

    :param means: tuple with (M1,M2)
    :param stdevs: tuple with (V1,V2)
    :param N_samples: tuple with (N1,N2)
    :return: float, effect size
    """

    m = means
    s = stdevs
    n = N_samples
    S = sqrt(((n[0] - 1) * s[0] ** 2 + (n[1] - 1) * s[1] ** 2) / (n[0] + n[1] - 2))

    return (m[0] - m[1]) / S


def assess_sample_differences(sample1, sample2, power=None, sig=0.05):
    z = gamma.isf
    pass

if __name__ == '__main__':

    n = sample_power_difftest(0.8, 4.4, power=0.8, sig=0.05)

    print n  #392