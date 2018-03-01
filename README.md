# Predicting Suicide Ideation

This project builds a machine learning model to predict suicide ideation.The model is trained, validated, and tested using data from the Collaborative Psychiatric Epidemiology Surveys (CPES), 2001-2003 [United States] (ICPSR 20240) http://www.icpsr.umich.edu/icpsrweb/ICPSR/studies/20240

# Motivation/Inspiration
This project was inspired by my experience with Crisis Text Line where I volunteer as a  Crisis Counselor for people in mental health crisis. When a texter exhibits signs of crisis, we ask them if they are thinking about suicide.

### If we can predict suicide ideation
### maybe we can prevent suicide.

# Goal
Build a machine learning model to predict suicide ideation. The mental health field has struggled to predict suicide and suicide ideation in the past. I want to help by continuing to support research with machine learning.

# Process
The machine learning model was trained and tested on the Collaborative Psychiatric Epidemiology Surveys (CPES). It is a combination of three US mental health surveys including both majority and minority populations. The data includes approximately 5,500 features and 20,000 respondents.

# Results
I explored the data using both regularized logistic regression and random forest models. Ultimately I found that small groups of features were ineffective at predicting suicide ideation. My recall scores increased into the thirties and forties only after I substantially increased my number of features.

# Conclusions
As a final model for this project I would recommend the Random Forest model with 1,110 features. It had an accuracy of 91%, recall of 39%, and precision of 74%.

# Next Steps
Next steps for this project include: continue researching and modeling on new datasets , explore themes for most predictive features, and eventually build a new model for features that are not explicitly mental health.

# More About the Data
"The Collaborative Psychiatric Epidemiology Surveys (CPES) were initiated in recognition of the need for contemporary, comprehensive epidemiological data regarding the distributions, correlates and risk factors of mental disorders among the general population with special emphasis on minority groups. The primary objective of the CPES was to collect data about the prevalence of mental disorders, impairments associated with these disorders, and their treatment patterns from representative samples of majority and minority adult populations in the United States. Secondary goals were to obtain information about language use and ethnic disparities, support systems, discrimination and assimilation, in order to examine whether and how closely various mental health disorders are linked to social and cultural issues. To this end, CPES joins together three nationally representative surveys: the NATIONAL COMORBIDITY SURVEY REPLICATION (NCS-R), the NATIONAL SURVEY OF AMERICAN LIFE (NSAL), and the NATIONAL LATINO AND ASIAN AMERICAN STUDY (NLAAS). These surveys collectively provide the first national data with sufficient power to investigate cultural and ethnic influences on mental disorders. In this manner, CPES permits analysts to approach analysis of the combined dataset as though it were a single, nationally representative survey. Each of the CPES surveys has been documented in a comprehensive and flexible manner that promotes cross-survey linking of key data and scientific constructs."
