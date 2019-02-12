from surprise import KNNBasic
from surprise import Dataset
from surprise import evaluate,print_perf
from surprise import accuracy
from surprise.model_selection import train_test_split

data=Dataset.load_builtin('ml-100k')
#data=Dataset.load_builtin('ml-1m')
data.split(n_folds=5)
algo=KNNBasic(k=20,sim_options={'name':'cosine','user_based':True})
performance = evaluate(algo,data,measures=['RMSE','MAE'])
print_perf(performance)


data.split(n_folds=5)
algo=KNNBasic(k=20,sim_options={'name':'pearson','user_based':True})
performance = evaluate(algo,data,measures=['RMSE','MAE'])
print_perf(performance)


data.split(n_folds=5)
algo=KNNBasic(k=20,sim_options={'name':'pearson','user_based':False})
performance = evaluate(algo,data,measures=['RMSE','MAE'])
print_perf(performance)



data.split(n_folds=5)
algo=KNNBasic(k=20,sim_options={'name':'msd','user_based':True})
performance = evaluate(algo,data,measures=['RMSE','MAE'])
print_perf(performance)

