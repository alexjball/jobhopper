"""
Default .xlsx parameters for OES data
"""
OES_XLSX_PARAMS = {
    'na_values': ['#', '*', '**'],
    'dtype': {'area': str,
              'area_title': str,
              'area_type': str,
              'naics': str,
              'naics_title': str,
              'i_group': str,
              'own_code': str,
              'occ_code': str,
              'occ_title': str,
              'o_group': str,
              'tot_emp': int,
              'emp_prse': float,
              'jobs_1000': float,
              'loc_quotient': float,
              'pct_total': float,
              'h_mean': float,
              'a_mean': float,
              'mean_prse': float,
              'h_pct10': float,
              'h_pct25': float,
              'h_median': float,
              'h_pct75': float,
              'h_pct90': float,
              'a_pct10': float,
              'a_pct25': float,
              'a_median': float,
              'a_pct75': float,
              'a_pct90': float,
              'annual': str,
              'hourly': str
             }
    }