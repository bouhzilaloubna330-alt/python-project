import numpy as np
from  sklearn.linear_model import LogisticRegression 
from sklearn.metrics import roc_curve,roc_auc_score
import matplotlib.pyplot as plt 

x= [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y = [0,0,0,0,0,1,1,1,1,1]

#trai the model 
model =LogisticRegression()
model.fit(x,y)

#get propa of class 1 
probabilities = model.predict_proba(x)[:,1]
print ("probabilities")
print(probabilities)

# calcule ROC piont 
fpr,tpr,thresholds = roc_curve(y,probabilities)
print("FPR",fpr)
print("tpr",tpr)
print("theresholds",thresholds)

# calcul AUC
auc = roc_auc_score(y,probabilities)
print("auc",auc)

#plot curve ROC 
plt.plot(fpr,tpr,label=f"ROC curve(AUC={auc:.2f})")
plt.plot([0,1],[0,1],"--")
plt.xlabel("false positive rate")
plt.ylabel("tru positive rate")
plt.legend()
plt.show()
