import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ["Lung cancer include a lump, abnormal bleeding",
             "prolonged cough",
             "unexplained weight loss and a change in bowel movements",
             "may indicate cancer",
             "they may have other causes",
             "or screening tests",
             "Main article: Cancer signs and symptoms Symptoms of cancer metastasis depend on the location of the tumor",
             "appear as the mass grows or ulcerates,are specific",
             "Local symptoms may occur due to the mass of the tumor or its ulceration",
             "General symptoms occur due to effects that are not related to direct or metastatic spread",
             "termed paraneoplastic syndrome of metastatic cancers depend on the tumor location and can include enlarged lymph nodes (which can be felt or sometimes seen under the skin and are typically hard)",
             "enlarged liver or enlarged spleen",
             "which can be felt in the abdomen",
             "pain or fracture of affected bones and neurological symptoms",
             "or through screening and medical signs",
             "cancer screening involves efforts to detect cancer after it has formed",
            " but before any noticeable symptoms appear",
             "such as pain or to reduce the size of an inoperable tumor in the hope that surgery will become possible in the future",
             "or who need help coping with their illness",
             "are commonly assumed to be a normal discomfort associated with pregnancy"]
##stemmer = SnowballStemmer()
##stop_words = text.ENGLISH_STOP_WORDS
##tokenizer = RegexpTokenizer(r'[a-zA-Z\']+')
##def tokenize(text):
##   return [stemmer.stem(word) for word in tokenizer.tokenize(text.lower())]
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 4
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")

Y = vectorizer.transform(["chrome browser to open."])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(["My cat is hungry."])
prediction = model.predict(Y)
print(prediction)
