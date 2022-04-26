from helper_functions import *

def draw_rocs(X, y, ds):
    f_name = ''
    if ds == 0:
        f_name = 'AUROCs without \"Subdomain level\" feature'
    elif ds == 1:
        f_name = 'AUROCs with \"Subdomain level\" feature'
    # Classifiers
    clfs = [DecisionTreeClassifier(),
            RandomForestClassifier(verbose=0),
            GradientBoostingClassifier(verbose=0),
            XGBClassifier(eval_metric='logloss',
                          use_label_encoder=False),
            SVC(probability=True, verbose=0),
            MLPClassifier(verbose=0)]
    colors = ['r', 'g', 'b', 'c', 'm', 'y']
    fig = plt.figure(figsize=(20, 10))
    plt.ioff()
    i = 0
    mean_f = []
    mean_t = []
    mean_a = []
    mean_s = []
    accs = []
    getattr(tqdm, '_instances', {}).clear()
    for classifier in tqdm(clfs):
        tprs = []
        aucs = []
        mean_fpr = np.linspace(0, 1, 100)
        #plt.figure(figsize=(10, 10))
        acc = []
        for train, test in cv.split(X, y):
            sc = StandardScaler()
            X_train = sc.fit_transform(X.iloc[train])
            X_test = sc.transform(X.iloc[test])
            probas_ = classifier.fit(
                X_train, y.iloc[train]).predict_proba(X_test)
            # Compute ROC curve and area the curve
            fpr, tpr, thresholds = roc_curve(
                y.iloc[test], probas_[:, 1])
            tprs.append(np.interp(mean_fpr, fpr, tpr))
            tprs[-1][0] = 0.0
            roc_auc = auc(fpr, tpr)
            aucs.append(roc_auc)
            acc.append(classifier.score(
                X_test, y.iloc[test]))
        accs.append(acc)
        mean_tpr = np.mean(tprs, axis=0)
        mean_tpr[-1] = 1.0
        mean_auc = auc(mean_fpr, mean_tpr)
        std_auc = np.std(aucs)
        mean_f.append(mean_fpr)
        mean_t.append(mean_tpr)
        mean_a.append(mean_auc)
        mean_s.append(std_auc)
        plt.plot(mean_fpr, mean_tpr, color=colors[i],
                 label=r'Mean ROC %s (AUC = %0.4f $\pm$ %0.4f)' % (
            str(type(classifier)).split(".")[-1][:-2], mean_auc, std_auc),
            lw=2, alpha=.8)
        i += 1

    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
             label='Chance', alpha=.8)
    plt.xlabel('False Positive Rate', fontsize=18)
    plt.ylabel('True Positive Rate', fontsize=18)
    plt.title(f_name, fontsize=18)
    plt.legend(loc="lower right", prop={'size': 15})
    # plt.show()
    plt.ioff()
    plt.savefig(f_name + '.png')


def evaluate_models(X, y, ds):
    f_name = ''
    if ds == 0:
        f_name = 'Evaluation Metrics without \"Subdomain level\" feature'
    elif ds == 1:
        f_name = 'Evaluation Metrics with \"Subdomain level\" feature'
    clfs = [DecisionTreeClassifier(),
            RandomForestClassifier(verbose=0),
            GradientBoostingClassifier(verbose=0),
            XGBClassifier(eval_metric='logloss',
                          use_label_encoder=False),
            SVC(verbose=0),
            MLPClassifier(verbose=0)]
    names = []
    times = []
    accs = []
    f1s = []
    tprs = []
    tnrs = []
    precisions = []
    getattr(tqdm, '_instances', {}).clear()
    for classifier in tqdm(clfs):
        clf = make_pipeline(StandardScaler(), classifier)
        clf_name = str(type(classifier)).split(".")[-1][:-2]
        clf_scr = cross_validate(clf, X, y,
                                 cv=cv, scoring=scoring, n_jobs=-1)
        clf_scr = append_avgs(clf_scr)
        names.append(clf_name)
        times.append(clf_scr['fit_time'][10])
        accs.append(clf_scr['test_accuracy'][10])
        precisions.append(clf_scr['test_precision'][10])
        f1s.append(clf_scr['test_f1'][10])
        tprs.append(clf_scr['test_sensitivity'][10])
        tnrs.append(clf_scr['test_specificity'][10])

    metrics = {"Classifier": names, "Fit Time (s)": times,
               "F-1": f1s, "Precision": precisions,
               "Accuracy": accs, "TPR": tprs, "TNR": tnrs}
    metrics_df = pd.DataFrame(metrics)

    metrics_df.to_csv(f_name + '.csv', index=False, header=True)

    fig = plt.figure(figsize=(20, 10))
    plt.ion()
    plt.title(f_name, fontsize=18)
    plt.grid(True)
    plt.plot(names, accs,
             label='Accuracy', marker='o', linestyle='--',)
    plt.plot(names, precisions,
             label='Precision', marker='o', linestyle='--',)
    plt.plot(names, f1s,
             label='F-1 score', marker='o', linestyle='--',)
    plt.plot(names, tprs,
             label='TPR', marker='o', linestyle='--',)
    plt.plot(names, tnrs,
             label='TNR', marker='o', linestyle='--',)
    plt.xlabel('Classifier')
    plt.ylabel('Performance')
    plt.xticks(names, names)
    plt.legend()
    plt.ioff()
    plt.savefig(f_name + '.png')
