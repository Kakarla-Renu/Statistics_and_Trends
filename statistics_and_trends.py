"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots()
    sns.scatterplot(data=df,x='enrollee_id',y='experience')
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots()
    sns.countplot(data=df,x='experience')
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots()
    sns.histplot(data=df,x='enrollee_id',y='experience')
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    mean =df[col].mean()
    stddev =df[col].std()
    skew =ss.skew(df[col])
    excess_kurtosis =ss.kurtosis(df[col])
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    print(df.describe())
    print(df.head())
    print(df.tail())
    print(df.corr())
    return df


def writing(moments, col):
    mean,stddev,skew,ex_kur=moments
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    # Delete the following options as appropriate for your data.
    # Not skewed and mesokurtic can be defined with asymmetries <-2 or >2.
    sk_des="not skewed"
    if skew>2:
        sk_des="right-skewed"
    elif skew<-2:
        sk+des="left-skewed"
    kur_des= "mesokurtic"
    if ex_kur > 1:
        kur_des = "leptokurtic (peaked)"
    elif ex_kur < -1:
        kurtosis_desc = "platykurtic (flat)"
    print('The data was right/left/not skewed and platy/meso/leptokurtic.')
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = '<your chosen column for analysis>'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
