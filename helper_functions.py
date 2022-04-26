# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:27:07 2022

@author: womega

"""

from imports_ import *


def set_seed(seed):

    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    random.seed(seed)


cv = StratifiedKFold(n_splits=10)

def specificity(y_true, y_pred):
    tn = confusion_matrix(y_true, y_pred)[0, 0]
    fp = confusion_matrix(y_true, y_pred)[0, 1]
    neg = tn + fp
    return tn/neg


scoring = {'f1': 'f1', 'precision': 'precision', 'accuracy': 'accuracy',
           'sensitivity': 'recall', 'specificity': make_scorer(specificity)}

# Input: csv file's directory
# Output: 25% underspampled feature vectors X and labels y


def load_file(file):

    data = pd.read_csv(file)

    X_nosub = data.drop(['Domain', 'Subdomain levels', 'Label'], axis=1)
    X_sub = data.drop(['Domain', 'Label'], axis=1)
    y = data['Label']

    resample(X_sub, y, "ST1", 0)
    resample(X_nosub, y, "ST2", 0)

    X_s25, y_s25 = resample(X_sub, y, "ST3", 0.25)
    X_ns25, y_ns25 = resample(X_nosub, y, "ST4", 0.25)
    
    resample(X_sub, y, "ST5", 1)
    resample(X_nosub, y, "ST6", 1)

    return X_s25, X_ns25, y_s25, y_ns25
    

def resample(X, y, stname, ratio=0):
    if ratio > 0:
        X_r, y_r = NearMiss(
            sampling_strategy=ratio).fit_resample(X, y)
    else:
        X_r =  X
        y_r = y

    df = pd.concat([pd.DataFrame(X_r, columns=X.columns), pd.Series(y_r, name='Label')], axis=1)

    df = df.sample(frac=1, random_state=1).reset_index(drop=True)

    df.to_csv(stname + '.csv', index=False, header=True)

    if ratio == 0.25:
        return X_r, y_r

def append_avgs(dict):
    avgs = []
    stds = []
    for i in dict:
        avg = np.average(dict[i])
        std = np.std(dict[i])
        avgs.append(avg)
        stds.append(std)
    df = pd.DataFrame(dict)
    df.loc[10] = avgs
    df.loc[11] = stds
    return df


def get_avg(df):
    return df.iloc[[10]].reset_index(drop=True)