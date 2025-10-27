from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class Modeling:
    def __init__(self):
        pass

    # model pipeline
    def model_pip(self, k):
        return make_pipeline(
            StandardScaler(),
            KMeans(n_clusters=k, random_state=42)
        )

    # tuning function
    def model_tuning(self, data, k_max):
        k_range = range(2, k_max)
        inertia_errors = []
        silhouette_scores = []

        for k in k_range:
            model = self.model_pip(k=k)
            model.fit(data)

            inertia = model.named_steps["kmeans"].inertia_
            silhouette = silhouette_score(data, model.named_steps["kmeans"].labels_)

            inertia_errors.append(inertia)
            silhouette_scores.append(silhouette)

        return silhouette_scores, inertia_errors


    
