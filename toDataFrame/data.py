import pandas as pd
import numpy as np
import json
from json import load


with open('get.json') as data_file:
	ori_data = load(data_file)

data = ori_data['_items']

bold_col = ['aor', 'aqi',
				'dvars_nstd', 'dvars_std', 'dvars_vstd',
				'efc', 'fber', 'fd_mean', 'fd_num', 'fd_perc',
				'fwhm_avg', 'fwhm_x', 'fwhm_y', 'fwhm_z',
				'gcor', 'gsr_x', 'gsr_y',
				'size_t', 'size_x', 'size_y', 'size_z',
				'snr', 'spacing_tr', 'spacing_x', 'spacing_y', 'spacing_z',
				'summary_bg_k', 'summary_bg_mean', 'summary_bg_p05', 'summary_bg_p95', 'summary_bg_stdv',
				'summary_fg_k', 'summary_fg_mean', 'summary_fg_p05', 'summary_fg_p95', 'summary_fg_stdv',
				'tsnr']
bold_count = pd.Series([0, 0, 0, 0, 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0,
						0, 0], index=bold_col)
bold_data = pd.DataFrame(columns=bold_col)

T1w_col = ['cjv', 'cnr', 'efc', 'fber',
			'fwhm_avg', 'fwhm_x', 'fwhm_y', 'fwhm_z',
			'icvs_csf', 'icvs_gm', 'icvs_wm',
			'inu_med', 'inu_range', 'qi_1', 'qi_2',
			'rpve_csf', 'rpve_gm', 'rpve_wm',
			'size_x', 'size_y', 'size_z',
			'snr_csf', 'snr_gm', 'snr_total', 'snr_wm',
			'snrd_csf', 'snrd_gm', 'snrd_total', 'snrd_wm',
			'spacing_x', 'spacing_y', 'spacing_z',
			'summary_bg_k', 'summary_bg_mean', 'summary_bg_p05', 'summary_bg_p95', 'summary_bg_stdv',
			'summary_csf_k', 'summary_csf_mean', 'summary_csf_p05', 'summary_csf_p95', 'summary_csf_stdv',
			'summary_gm_k', 'summary_gm_mean', 'summary_gm_p05', 'summary_gm_p95', 'summary_gm_stdv',
			'summary_wm_k', 'summary_wm_mean', 'summary_wm_p05', 'summary_wm_p95', 'summary_wm_stdv',
			'tpm_overlap_csf', 'tpm_overlap_gm', 'tpm_overlap_wm', 'wm2max']
T1w_count = pd.Series([0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0], index=T1w_col)
T1w_data = pd.DataFrame(columns=T1w_col)


def bold_df(dict):
	for name in bold_col:
		the_data = dict[name]
		bold_data.set_value(bold_count[name], name, the_data)
		bold_count[name] = bold_count[name] + 1

def T1w_df(dict):
	for name in T1w_col:
		the_data = dict[name]
		T1w_data.set_value(T1w_count[name], name, the_data)
		T1w_count[name] = T1w_count[name] + 1


if data[0]['modality'] == "bold":
	for item in data:
		bold_df(item)

if data[0]['modality'] == "T1w":
	for item in data:
		T1w_df(item)

print bold_data, T1w_data
