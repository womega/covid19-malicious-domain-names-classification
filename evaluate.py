# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:27:07 2022

@author: womega

"""

from offline_eval import *
from online_eval import evaluate_ht


# ---- Main ----


"""
Main function - enter code here to run/process data into pre-specified
splits and output
"""


def main():

    set_seed(42)

    X_sub, X_nosub, y_sub, y_nosub = load_file('dataset.csv')

    print("\n\nEvaluating classifiers with \"Subdomain level\" feature ...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    evaluate_models(X_sub, y_sub, 1)

    print("\n\nCalculating AUROCs with \"Subdomain level\" feature ...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    draw_rocs(X_sub, y_sub, 1)

    print("\n\nEvaluating classifiers without \"Subdomain level\" feature ...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    evaluate_models(X_nosub, y_nosub, 0)

    print("\n\nCalculating AUROCs without \"Subdomain level\" feature ...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    draw_rocs(X_nosub, y_nosub, 0)
    
    print("\n\nEvaluating Hoeffding Trees ... ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    evaluate_ht()

main()