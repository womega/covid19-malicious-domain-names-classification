# COVID-19 Malicious Domain Names Classification (under review)

---

> Paul K. Mvula, Paula Branco, Guy-Vincent Jourdan, Herna L. Viktor

---

## Article link:

***to be updated***

[ESWA](https://www.journals.elsevier.com/expert-systems-with-applications)

---
## Description

This repository includes the dataset feature descriptions and code used in the article above.

The repository is organized as follows:

* **benign_domains** - contains all the examples of benign domains in csv format
* **malign_domains** - contains all the examples of malign domains in csv format
* **dataset** - contains the malign and benign domains in csv format
* **dataset_description** - contains the main characteristics of the dataset
* **evaluate.py** - runs all the evaluations (online and oflline) and builds the tables/figures in the paper using the **imports_.py**, **offline_eval.py**, **online_eval.py**, **helper_functions.py** scripts.

The extracted features can be exploited by conventional machine learning algorithms or combined with other features for experiments.

---
## Features Description

Feature | Type | Description |
--------|------|-------------|
Domain |	string|	|the domain name|
Num_words|	integer|	the number of words in the domain, extracted using [wordninja](https://github.com/keredson/wordninja)|
Num_chars|	integer|	the number of characters in the domain|
Hyphen|	boolean|	contains hyphens?|
Entropy_sdsu|	float|	entropy with SLD and Suffix|
Entropy_nosdsu|	float|	entropy without SLD and Suffix|
Entropy_nosu|	float|	entropy without Suffix|
Tranco_Rank|	boolean|	on Tranco List ?|
Longest_word_ratio|	float|	Ratio of the longest word to length of domain|
Typos|	boolean|	contains typos? (typos generated using [dnstwist](https://github.com/elceef/dnstwist))|
Freenom_TLD|	boolean	|Freenom suffix?|
Other_numbers|	boolean|	Other numbers than 19?|
Subdomain levels|	integer|	Number of Sub-domain levels|
Label|	integer|	1: legitimate, 0: malicious|



---

Cite as:

***to be updated upon acceptance***
