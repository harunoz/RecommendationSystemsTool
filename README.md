
The complement code is implemented in Python and requires python3 for execution

The packages used in the execution of the program are:


* Surprise Library (only for prediction.py file)


*The code is divided into 3 files functions as follows:*
1. **prediction.py The values from Table 1 to Table 4 calculated with these code. I used http://surpriselib.com/ which is desined for recommender systems.  On line 7-13 we load our datasets. After that line 16 describes that number of folds. This means that, I did test five times and calculate the average. On line 10, we desgin our algorithm, KNNBasic describest that our prediction method and parameters of KNNBasic, k describes number of neighbor, and similarirty options, line 19 specify our similarity method. We did same thing for other similarity metric


2. **recommendation.py
From line 13. in this code we can adjust our parameters, numberOfRecommendation, neighborNumber.

*similarity function --> This method takes trainset as a parameter, and returns user similarity matrix. I used very crude approach for calculating similariy which gives good performance however Table 4 to Table 9 shows that, some traditional similarity methods gives better performance. My crude approach is number of same rating of two user divided by number of rated movies from each user. For the extension on line 17, after I calculate popularity of movies I can introduce new similarity metric.


* recommendation function --> For the recommendation, we need to calculate prediction score. I calculate prediction score which is the same as KNNBasic approach. For example User1 and User2 has a similarity score 2, and User2’s rating for movie1 is 4 that means that movie1’s score for User1 is 8. I sort them and I recommend the moves which has highest values.
It returns the highest values.

*main.py --> 

*run model function --> This function run our code.


