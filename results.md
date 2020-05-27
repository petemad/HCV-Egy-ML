# Class 1 vs Class 4
Using BMI and histological grading
and StandardScalar(with_std = True)
SVC ==> 47%
LinearSVC ==> 58.5%


Using BMI - histological grading - jaundice  
and StandardScalar(with_std = True)
SVC ==> 56.4 %
LinearSVC ==> 59.2 %


Using BMI - histological grading - RNA EF  
SVC ==> 50.5
LinearSVC ==> 57%
                                                                    DONE
## Using categorial features
##### StandardScalar(with_std = True)
Blood features (WBC/ RBC/ HGB)
SVC ==>50%
linearSVC ==>51%
                                                                    DONE
RNA features (RNA)
SVC ==>47%
linearSVC ==>47%

                                                                    DONE
#### Without StandardScalar(with_std = True)
Blood features (WBC/ RBC/ HGB)
SVC ==>52%
linearSVC ==>52% (1000000 iteration without convergence (most probably it is diverges))

RNA features (RNA)
SVC ==>47%
linearSVC ==>49%


#### Without StandardScalar(with_std = True)
Blood features (WBC/ RBC/ HGB) and histological grading
SVC ==>52%
linearSVC ==>43% (1000000 iteration without convergence (most probably it is diverges))

RNA features (RNA) and histological grading
SVC ==>47.8%
linearSVC ==>43.5%




## PCA 
n_components = 5
SVM ==> 52%
LinearSVM ==> 50%

# All four classes
normalize and whiten continuous features
SCV() ==> 25.99

Feature selection according to entropy in RandomForest discretized all features ==> 32.58 %

## features division
All continuous features were normalized and whitened
clinical = ['Fever', 'Nausea/Vomting', 'Headache ', 'Diarrhea ', 'Fatigue & generalized bone ache ','Jaundice ', 'Epigastric pain ']
prop = ['Gender','Age', 'BMI']
blood = ['WBC', 'RBC', 'HGB', 'Plat', 'AST 1', 'ALT 1', 'ALT4', 'ALT 12', 'ALT 24', 'ALT 36', 'ALT 48', 'ALT after 24 w', 'Baseline histological Grading']
dna = ['RNA Base', 'RNA 4', 'RNA 12', 'RNA EOT', 'RNA EF']

SVC on each feature subset: avg_acc = 24.72
LinearSVC ==> avg_acc = 27.075

LinearSVC with L1 norm penalty based feature selection acc=26.35