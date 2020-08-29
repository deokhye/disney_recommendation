import pandas as pd
import numpy as np

titile_df = pd.read_csv('movies_title.csv', names=['title', 'code'])
reple_df = pd.read_csv('movies_reple.csv', names=['code', 'reple'])
plot_df = pd.read_csv('after_pre_plot.csv', names=['code', 'plot'])

# title_reple_df = pd.merge(titile_df, reple_df, on='code')
# title_reple_df.to_csv("title_reple.csv", mode='w',index=False)

title_plot_df = pd.merge(titile_df, plot_df, on='code')
title_plot_df.to_csv("title_after_plot.csv", mode='w',index=False)
