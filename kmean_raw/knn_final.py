import random


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


def get_k_means(user_feature_map, num_features_per_user, k):
    random.seed(42)
    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

    centroids = [Centroid(user_feature_map[uid]) for uid in inital_centroid_users]

    for _ in range(10):
        for uid,val in user_feature_map.items():
            min_dist = float('inf')
            closest = uid
            for centroid in centroids:
                dist = get_manhattan_distance(centroid.location,val)
                if dist<min_dist:
                    min_dist = dist
                    closest = centroid
            closest.closest_users.add(uid)

        for centroid in centroids:
            centroid.location = get_average_centroid(user_feature_map,centroid,num_features_per_user)
            # clear the old closest user
            centroid.closest_users.clear()
        
    return [centroid.location for centroid in centroids]
    
def get_average_centroid(user_feature_map,centroid,num_features_per_user):
    average_distances = [0]* num_features_per_user
    for uid in centroid.closest_users:
        for i in range(num_features_per_user):
            average_distances[i] = average_distances[i] + user_feature_map[uid][i]

    return [d/len(centroid.closest_users) for d in average_distances]
            
    
def get_manhattan_distance(l1,l2):
    return sum([abs(i-j) for i,j in zip(l1,l2)])