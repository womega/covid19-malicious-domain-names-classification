# COVID-19 Malicious Domain Names Classification

---

> Paul K. Mvula, Paula Branco, Guy-Vincent Jourdan, Herna L. Viktor

---

## Article link:

[COVID-19 malicious domain names classification](https://doi.org/10.1016/j.eswa.2022.117553)

The code (and data) in this article has been certified as Reproducible by [Code Ocean](https://codeocean.com/). To reproduce these experiments, please follow think [link](https://codeocean.com/capsule/2379125/tree/v1).

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

Cite article as:


@article{10.1016/j.eswa.2022.117553, 
         author = {Mvula, Paul K. and Branco, Paula and Jourdan, Guy-Vincent and Viktor, Herna L.}, 
         title = {COVID-19 Malicious Domain Names Classification▪}, 
         year = {2022}, issue_date = {Oct 2022}, 
         publisher = {Pergamon Press, Inc.}, 
         address = {USA}, 
         volume = {204}, 
         number = {C}, 
         issn = {0957-4174}, 
         url = {https://doi.org/10.1016/j.eswa.2022.117553}, 
         doi = {10.1016/j.eswa.2022.117553}, 
         journal = {Expert Syst. Appl.}, 
         month = {oct}, 
         numpages = {10}, 
         keywords = {Hoeffding trees, Cybersecurity, Online learning, Phishing attacks, Supervised learning, Machine learning} }
   
- Code Ocean

@misc{mvula_covid-19_2022,
	title = {{COVID}-19 {Malicious} {Domain} {Names} {Classification}},
	copyright = {MIT License, Creative Commons Attribution Non Commercial 4.0 International},
	url = {https://codeocean.com/capsule/2379125/tree/v1},
	abstract = {The capsule contains code to reproduce results in our paper titled "COVID-19 Malicious Domain Names Classification".},
	urldate = {2022-05-04},
	publisher = {Code Ocean},
	author = {Mvula, Paul and Branco, Paula and Guy-Vincent Jourdan and Viktor, Herna},
	year = {2022},
	doi = {10.24433/CO.0525147.V1},
	note = {Language: en},
	keywords = {machine learning, cybersecurity, COVID-19, Capsule, Computer Science},
}

