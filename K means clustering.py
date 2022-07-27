from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

name=input("Enter file name with extention: ")
documents = open(name)
#print(documents.read())

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

k =2
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Cluster centroids: \n")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(k):
    print("Cluster %d:" % i)
    for j in order_centroids[i,:10]: #print out 10 feature terms of each cluster
        print (' %s' % terms[j])
    print('------------')