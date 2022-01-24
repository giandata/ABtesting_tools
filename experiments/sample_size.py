

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
