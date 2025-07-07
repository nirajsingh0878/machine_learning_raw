import math



def predict_label(examples, features, k, label_key="is_intrusive"):
    nearest_k = find_k_nearest_neighbors(examples,features,k)
    labels_pred = sum([examples[pid][label_key] for pid in nearest_k])/len(nearest_k)
    return round(labels_pred)


def get_euclidean_distance(val1,val2):
    return math.sqrt(sum([(v1-v2)**2 for v1,v2 in zip(val1,val2)]))

def find_k_nearest_neighbors(examples, features, k):
    print(examples)
    distances = {}
    for pid,values in examples.items():
        e = get_euclidean_distance(examples[pid]['features'],features)
        distances[pid]=e
        # print(e)
    ans = sorted(distances.items(),key = lambda x:x[1])
    return [pid for pid, _ in ans[:k]]
   
    

'''
find k nearest neighbour
Expected Output -> ["pid_500"]
Your Code's Output -> ["pid_500"]

input(s)
{
  "features": [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593],
  "k": 1,
  "method": "find_k_nearest_neighbors"
}

# use testcaseknn for data and also check predict_label 
'''
