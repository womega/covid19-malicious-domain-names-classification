from helper_functions import *

def evaluate_ht():
    metrics_ = ['accuracy', 'recall', 'precision',
               'gmean', 'f1', 'kappa', 'running_time']
    names = []
    ks = []
    accs = []
    f1s = []
    recalls = []
    precisions = []
    gmeans = []

    for i in range(1, 7):
        ht = HoeffdingTreeClassifier()
        max_samples = 0
        if i == 1:
            name = 'ST1'
            st = FileStream(name + '.csv')
            max_samples = 40000
            print("\n\nEvaluating on", name, "...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
        elif i == 2:
            name = 'ST2'
            st = FileStream(name + '.csv')
            max_samples = 40000
            print("\n\nEvaluating on", name, "...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
        elif i == 3:
            name = 'ST3'
            st = FileStream(name + '.csv')
            max_samples = 19000
            print("\n\nEvaluating on", name, "...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
        elif i == 4:
            name = 'ST4'
            st = FileStream(name + '.csv')
            max_samples = 19000
            print("\n\nEvaluating on", name, "...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
        elif i == 5:
            name = 'ST5'
            st = FileStream(name + '.csv')
            max_samples = 7500
            print("\n\nEvaluating on", name, "...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
        elif i == 6:
            name = 'ST6'
            st = FileStream(name + '.csv')
            max_samples = 7500
            print("\n\nEvaluating on", name, "...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")

        evaluator = EvaluatePrequential(show_plot=False,
                                        data_points_for_classification=True,
                                        max_samples=max_samples,
                                        metrics=metrics_)

        evaluator.evaluate(stream=st, model=ht)

        measurements = evaluator.get_mean_measurements()
        names.append(name)
        accs.append(ClassificationPerformanceEvaluator.accuracy_score(measurements[0]))
        ks.append(ClassificationPerformanceEvaluator.kappa_score(measurements[0]))
        precisions.append(ClassificationPerformanceEvaluator.precision_score(measurements[0]))
        recalls.append(ClassificationPerformanceEvaluator.recall_score(measurements[0]))
        f1s.append(ClassificationPerformanceEvaluator.f1_score(measurements[0]))
        gmeans.append(ClassificationPerformanceEvaluator.geometric_mean_score(
            measurements[0]))

        metrics = {"Classifier": names, "Accuracy": accs,
                   "k": ks, "Precision": precisions, "Recall": recalls,
                    "F-1": f1s, "G-Mean": gmeans}

        metrics_df = pd.DataFrame(metrics)

        metrics_df.to_csv('online_evaluation.csv', index=False, header=True)

        fig = plt.figure(figsize=(20, 10))
        plt.ion()
        plt.title('Online Evaluation', fontsize=18)
        plt.grid(True)
        plt.plot(names, accs,
                label='Accuracy', marker='o', linestyle='--',)
        plt.plot(names, precisions,
                label='Precision', marker='o', linestyle='--',)
        plt.plot(names, f1s,
                label='F-1 score', marker='o', linestyle='--',)
        plt.plot(names, ks,
                label='k', marker='o', linestyle='--',)
        plt.plot(names, recalls,
                label='Recall', marker='o', linestyle='--',)
        plt.plot(names, gmeans,
                 label='G-Mean', marker='o', linestyle='--',)
        plt.xlabel('Classifier')
        plt.ylabel('Performance')
        plt.xticks(names, names)
        plt.legend()
        plt.ioff()
        plt.savefig('online_evaluation.png')
