# nepali-pos-tagger
POS Tagger for Neali. Done for Machine Learning Elevtive of KU

A Parts of Speech Tagger for Nepali Language. <br>
The final program "predictor.py" uses a combination of two method:<br>
1. Statistical Method <br>
2. Decission Tree <br>

We used statistical tagger to tag words which were found to be of a single class. We also assgined the words with tags in which they were classified the maximum times in trainning set. The remaining words were tagged using an "UNK" tag. We used this information as feature for decission tree. A single classifier was trainned for each ambigious class. A global classifier was trained to classify unknown cases. The words were again tagged using the decission trees. To improved the accuracy, we used the decission tree 3 times using the tags of previous iteration as feature. LabelEncoder and OneHotEncoder from scikit library were used to represent the features and Decission Tree from scikit learn library was used for classification. 

Team Members : Prashant Subedi & Bibek Pokhrel.<br>
DataSet being used:  http://cle.org.pk/software/ling_resources/UrduNepaliEnglishParallelCorpus.htm
