# SAS-Workbench-Boost-Credit-Scorecard-Performance
---

This is a notebook that demonstrates the process of building credit risk scorecard models, and then incorporating synthetic dat to boost their performance, using a platform called SAS Viya Workbench. SAS Viya Workbench is a data science platform, similar to AWS Sagemaker.

The data used in this demonstration is data from Lending Club, which is publicly available [here](https://www.kaggle.com/datasets/itssuru/loan-data). In this notebook, we prepare and bin the data, then train logistic regression models and gradient boosting classifiers from two packages - scikit-learn and the SAS Viya ML package (which is specific to Workbench and uses the same syntax as scikit-learn). Then, the same pipeline is run using a 1 million row synthetically generated sample with a boosted event rate of 40% for the target event for the same set of algorithms.

A scorecard is then built from the Workbench model, and these models are then operationalise into a centralised model repository through API call.


## Methodology and Notebook Execution
---

Unless you have access to a SAS Viya Workbench environment, you will not be able to run this notebook - so please feel free to substitute the Workbench code, or just use the methodology in the notebook as a template. Additional API layers were written on top of SAS functionality, as indicated in the data_preprocess.py script.

The methodology itself was based on a client experience. Normally boosting target events is performed with a very low event rate like in scams data (less than 2%), but you may still see some uplift in examples such as this one.
