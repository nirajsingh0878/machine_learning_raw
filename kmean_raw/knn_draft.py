#%%
import json
import ast


# data is process_id with four pca reduced feature set 

def load_data(file):
    try:        
        with open(file,'r') as file:
            data = file.read()
            data = data.strip()
            data_dt = ast.literal_eval(data)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return data_dt

file = 'testcase1.json'
data = load_data(file)

#%%
import random

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()
        

random.seed(42)
k = 3
inital_centroid_users = random.sample(sorted(list(data.keys())), k)
def manhattan_dist(centroid,uid1):
    print(data[uid1])
    return sum([abs(i-j) for i,j in zip(centroid,data[uid1])])

centroids = [Centroid(data[loc]) for loc in inital_centroid_users]
num_features_per_user = 4
#%%

def get_kmeans_cluster():
    for _ in range(10):
        for k in data.keys():
            print(f'user_id-{k}')
            closest = None
            min_dist = float('inf')
        
            for centroid in centroids:
                print(f"Centroid location : {centroid.location}")
                distance = manhattan_dist(centroid.location, k)
                if distance<min_dist:
                    min_dist = distance
                    closest = centroid
            closest.closest_users.add(k)    
        for centroid in centroids:
            centroid_average = [0]*num_features_per_user
            for user in centroid.closest_users:
                for i in range(num_features_per_user):
                    centroid_average[i] = centroid_average[i]+data[user][i]
            
            centroid.location = [d/len(centroid.closest_users) for d in centroid_average]
            centroid.closest_users.clear()
            
    return [centroid.location for centroid in centroids]
                    
         
