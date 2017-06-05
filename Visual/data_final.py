import pandas as pd
import numpy as np
import json
from json import load
import requests


bold_url = 'http://0.0.0.0/bold'
bold_ori = requests.get(bold_url).json()
bold_data = bold_ori['_items']

T1w_url = 'http://0.0.0.0/T1w'
T1w_ori = requests.get(T1w_url).json()
T1w_data = T1w_ori['_items']


full_df = pd.DataFrame(columns = ['iqm', 'value', 'label'])

for record in bold_data:
	for k in record.keys():
		iqm_data = k
		value_data = record[k]
		label_data = 'sub-' + record['task_id']
		tmp = pd.DataFrame([[iqm_data, value_data, label_data]],
							columns=['iqm', 'value', 'label'])
		full_df = full_df.append(tmp)

for record in T1w_data:
	for k in record.keys():
		iqm_data = k
		value_data = record[k]
		label_data = 'sub-' + record['subject_id']
		tmp = pd.DataFrame([[iqm_data, value_data, label_data]],
							columns=['iqm', 'value', 'label'])
		full_df = full_df.append(tmp)

def select_row(name):
	return full_df.loc[full_df['iqm'] == name]

#single field
select_row("cjv").to_csv('cjv.csv', index=False)
select_row("cnr").to_csv('cnr.csv', index=False)
select_row("efc").to_csv('efc.csv', index=False)
select_row("fber").to_csv('fber.csv', index=False)
select_row("wm2max").to_csv('wm2max.csv', index=False)

#multiple fields
def combine(df1, df2, df3):
	tmp = df1.append(df2)
	return tmp.append(df3)

def two(name1, name2, path):
	tmp1 = select_row(name1)
	tmp2 = select_row(name2)
	tmp1.append(tmp2).to_csv(path, index=False)

def three(name1, name2, name3, path):
	tmp1 = select_row(name1)
	tmp2 = select_row(name2)
	tmp3 = select_row(name3)
	tmp1.append(tmp2).append(tmp3).to_csv(path, index=False)


def four(name1, name2, name3, name4, path):
	tmp1 = select_row(name1)
	tmp2 = select_row(name2)
	tmp3 = select_row(name3)
	tmp4 = select_row(name4)
	tmp1.append(tmp2).append(tmp3).append(tmp4).to_csv(path, index=False)

def five(name1, name2, name3, name4, name5, path):
	tmp1 = select_row(name1)
	tmp2 = select_row(name2)
	tmp3 = select_row(name3)
	tmp4 = select_row(name4)
	tmp5 = select_row(name5)
	tmp1.append(tmp2).append(tmp3).append(tmp4).append(tmp5).to_csv(path, index=False)

three("snr_csf", "snr_gm", "snr_wm", 'snr.csv')
three("snrd_csf", "snrd_gm", "snrd_wm", 'snrd.csv')
four("fwhm_avg", "fwhm_x", "fwhm_y", "fwhm_z", 'fwhm.csv')
two("qi_1", "qi_2", 'qi.csv')
two("inu_range", "inu_med", 'inu.csv')
three("icvs_csf", "icvs_gm", "icvs_wm", 'icvs.csv')
three("rpve_csf", "rpve_gm", "rpve_wm", 'rpve.csv')
three("tpm_overlap_csf", "tpm_overlap_gm", "tpm_overlap_wm", 'tpm_overlap.csv')
five("summary_bg_mean", "summary_bg_stdv", "summary_bg_k", "summary_bg_p05", "summary_bg_p95", 'summary_bg.csv')
five("summary_csf_mean", "summary_csf_stdv", "summary_csf_k", "summary_csf_p05", "summary_csf_p95", 'summary_csf.csv')
five("summary_gm_mean", "summary_gm_stdv", "summary_gm_k", "summary_gm_p05", "summary_gm_p95", 'summary_gm.csv')
five("summary_wm_mean", "summary_wm_stdv", "summary_wm_k", "summary_wm_p05", "summary_wm_p95", 'summary_wm.csv')


