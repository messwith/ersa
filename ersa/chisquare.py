"""Chi square testing and hypothesis inference"""
#   Copyright (c) 2015 by
#   Richard Munoz <rmunoz@nygenome.org>
#   Jie Yuan <jyuan@nygenome.org>
#   Yaniv Erlich <yaniv@nygenome.org>
#
#   All rights reserved
#   GPL license

from scipy import stats
import math

#confidence interval? get the inverse cdf at p=ci,p=1-ci
def likelihoodRatioTest(Lr, Ln, df=2, ci=0.05):
    ratio = -2*math.log(Lr) + 2*math.log(Ln)

    lowerCI = stats.chi2.ppf(ci,2)
    upperCI = stats.chi2.ppf(1-ci,2)
    return 1-stats.chi2.cdf(ratio, df), lowerCI, upperCI
