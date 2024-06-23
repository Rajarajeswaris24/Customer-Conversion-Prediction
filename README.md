Customer Conversion Prediction

Problem Statement:

	You are working for a new-age insurance company and employ multiple outreach plans to sell term insurance to your customers. Telephonic marketing campaigns still remain one of the most effective ways to reach out to people however they incur a lot of cost. Hence, it is important to identify the customers that are most likely to convert beforehand so that they can be specifically targeted via call. We are given the historical marketing data of the insurance company and are required to build a ML model that will predict if a client will subscribe to the insurance.
 
DATASET:

	The historical sales data is available as a compressed file here. 


APPROACH:

    1.Import the required packages.
    
    2.Load the dataset.
    
    3.Clean the dataset.
      a.Remove duplicates(total data 45211 after removing duplicates total data 45205).
      
      b.Missing values( no Nan values in the dataset).
      
      c.Data Type conversion(no incorrect format).
      
      d.Structured dataset.
      
      e.Remove outliers(column ‘age’,’dur’,’num_calls’ consists of outliers).
      
    4.Target variable y has maximum ‘no’ so mapped ‘no’ as 1 and ‘yes’ as 0 to perform EDA.
    
    5.EDA(Exploratory Data Analysis) and Encode.
    
      a.Group the column ‘y’ and mean of column ‘age’ and plot.
      
      b.Group the column ‘y’ and mean of column ‘day’ and plot.
    
      c.Group the column ‘y’ and mean of column ‘dur’ and plot.
    
      d.Group the column ‘y’ and mean of column ‘num_calls’ and plot.
    
      e.Group the column ‘job’ and mean of column ‘y’ and plot.
      
        Mapped the column job based on mean values in this ‘blue- collar’ mean is 0.92 so mapped with 12 then ‘entrepreneur’ mapped with 11 likewise mapped according to mean values.
    
      f.Group the column ‘marital’ and mean of column ‘y’ and plot.
    
        Mapped the column ‘marital’ according to mean values ‘single’ as 1, ‘divorced’ as 2 and ‘married’ as 3.
    
      g. Group the column ‘education_qual’ and mean of column ‘y’ and plot.
    
        Mapped the column ‘education_qual’ according to mean  values.
    
      h.Group the column ‘call_type’ and mean of column ‘y’ and plot.
     
        Map the column ‘call_type’ according to the mean values.
    
      i.Group the column ‘mon’ and mean of column ‘y’ and plot.
    
        Map the column ‘mon’ according to the highest  mean map with higher value.
    
      j.Group the column ‘prev_outcome’ and mean of column ‘y’ and plot.
   
         Map the column ‘prev_outcome’ according to the mean values.
    
    6.Save the mapped column using pickle.
    
    7.Given dataset is an imbalanced dataset 88% ‘no’ and only 11% ‘yes’.
    
    8.Split the dataset into train and test data.
    
    9.Balance the dataset using SMOTE(Synthetic Minority Oversampling Technique). Can also use Cluster- centroid and Smoteenn. But in this dataset using smote got the best f1_score.
    
    10.Model fit and evaluation.
    
      a.LogisticRegression F1 score: 0.9007163703900238
      
      b.DecisionTreeClassifier F1 score: 0.9191093861709734
      
        After cross validation at max_depth 18
        
        DecisionTreeClassifier F1 score: 0.9211865713845047
      
      c.RandomForestClassifier F1 score: 0.9329923273657289
      
        After cross validation at n_estimators 500 max_depth 25 and max_features ‘log2’
        
        RandomForestClassifier F1 score: 0.9339473011000256
        
      d.XGBClassifier F1 score: 0.9378427787934186
      
        After cross validation at learning_rate 0.6
        
        XGBClassifier F1 score: 0.9383451059535822
        
      e.So the best model is the XGBClassifier, save fine tuned XGBClassifier model using pickle.
    
    11.Feature importance of fine tuned XGBClassifier
    
    12.Then load the saved encoder and model in streamlit with the select box and text_input to predict whether the client will subscribe or will not subscribe to the insurance policy.








				

