# HCV-Egy-ML

# 2 features for each KNN(10) classifier, apply polynomial of degree 4
majority accuracy = ranges from 22% to 44 % in four classes while tha max accuracy was 33 %

# 2 features // //  // , ploynomial of degree 8
features 216 and 494 ==> accuracy = 65% for 2 classes (best estimator)


# accuracy 31 % on four classes based 3 features that have the highest std_dev from
KNN(3)


# poly of 5 on selected featurs( alt 12, rna 12/eot/ef, baselline histological grading)
without descretization
considering only two featurs randomly 
knn(10) ==> 500 estimators
max_accuracy = 33.2 featurs (13, 251)
majority accuracy = 27.5

# poly of 5 on selected featurs( alt 12, rna 12/eot/ef, baselline histological grading)
without descretization
considering 3 featurs randomly 
knn(10) ==> 500 estimators
max_accuracy = 33.49 featurs (8, 250, 251)
majority accuracy = 26.7

# poly of 4 on selected featurs( BMI, alt 12/after 24, rna Base/4/12/eot/ef, epigastric pain, Plat, baselline histological grading)
without descretization
with MinMaxScalar
feature selection => 0.5 max std_dev
considering only 1 feature out of 92 randomly  
LinearSVC() ==> 100 estimators
max_accuracy = 33.93 feature 28 only
majority accuracy = 28.15