

def sample_size_calc(alpha, beta, conversion_base, conversion_desired):

    z_table_alpha = {90: 1.645,
                     95: 1.96,
                     98: 2.326,
                     99: 2.576}

    z_table_beta = {80: 0.84,
                    90: 1.28,
                    95: 1.645}

    c1 = conversion_base/100
    c2 = ((conversion_desired/100)*c1) + c1

    pool_variance = (c1 * (1 - c1)) + (c2 * (1 - c2))

    return int(round((pool_variance / (c1-c2)**2) *
                     (z_table_beta[beta] + z_table_alpha[alpha])**2, 0))


def unequal_samples(n, k):

    j = 100-k
    ratio = round((j / k), 2)
    adjusted_sample = int(round((n * (1 + ratio)**2) / (ratio * 4), 0))
    control_sample = int(round(adjusted_sample / (1+ratio), 0))
    test_sample = int(round((adjusted_sample - control_sample), 0))

    return (ratio, adjusted_sample, control_sample, test_sample)

    # N = sample
    # N1 = (n(1+k)**2 )/ 4*k
    #control = N1/(1+k)
    #variant = k*N1/(1+k)

    # N = 1688 k= 0,9

    # n1 = (1688*3.61)/7,6 = 802

    # control = 802/1,9 = 422
    # variant = 0,9* 802 /1,9 = 382
