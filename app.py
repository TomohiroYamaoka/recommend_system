import pandas as pd 
import numpy as np 
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

#kaggleからcsvファイルをインポーとする。
#https://www.kaggle.com/CooperUnion/anime-recommendations-database
#https://www.codexa.net/collaborative-filtering-k-nearest-neighbor/

ratings = pd.read_csv('rating.csv')
anime = pd.read_csv('anime.csv')


# ratingのデータフレームの最初の5行を表示
ratings.head()