import pandas as pd
from scipy.stats.mstats import trimmed_var
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


class Analysis():
    
    def __init__(self, path = 'C:/Users/Admin 21/Downloads/Customer Segmentation/Data/SCFP2019.csv'):
        self.path = path
    
    def data_input(self):
        df = pd.read_csv(self.path)
        mask = (df["TURNFEAR"]==1) & (df["NETWORTH"]<3e6)
        df=df[mask]
        return df
        
    def var_features(self, trimvar =True, features_rtrn=True):
        df = self.data_input()
        if trimvar:
            high_var = df.apply(trimmed_var).sort_values().tail(5)
        else:
            high_var = df.var().sort_values().tail(5)
            
        if features_rtrn:
            high_var = high_var.index.to_list()
        
        return high_var
    
    def model_metrics(self, trimvar = True, k=2, metrics = False):
        features = self.var_features(trimvar=trimvar, features_rtrn = True)
        df = self.data_input()
        X = df[features]
        model = make_pipeline(StandardScaler(), KMeans(n_clusters=k, random_state=42))
        
        model.fit(X)
        
        if metrics:
            inertia = model.named_steps["kmeans"].inertia_
            silhouette = silhouette_score(X, model.named_steps["kmeans"].labels_)
            metrics =   {
                "inertia": round(inertia),
                "silhouette": round(silhouette,3)
                        }
            return metrics
        return model
            
    def pca_labels(self,trimvar=True, k=2):
        features = self.var_features(trimvar=trimvar, features_rtrn = True)
        X = self.data_input()[features]
        pca = PCA(n_components=2, random_state=42)
        Xt = pca.fit_transform(X)
        Xpca = pd.DataFrame(Xt, columns = ["PC1", "PC2"])
        
        model = self.model_metrics(trimvar = trimvar, k=k, metrics = False)
        Xpca["labels"] = model.named_steps["kmeans"].labels_.astype(str)
        Xpca.sort_values("labels", inplace=True)
        
        return Xpca
