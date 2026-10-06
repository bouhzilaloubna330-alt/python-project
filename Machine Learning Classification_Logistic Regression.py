from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score,recall_score,precision_score,f1_score

x= np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y= np.array([0,0,0,0,1,1,1,1])
model = LogisticRegression()
model.fit(x,y)
predictions =model.predict(x)
probabilities = model.predict_proba(x)
print(predictions)
print(probabilities)


#####  confusion matric( to see how many are tru and false TN FN
     ###                                                   FP TP
cm = confusion_matrix(y,predictions)
print("confusion matrix:")
print(cm)

### arruracy = corect pred/total predc
accuracy = accuracy_score(y,predictions)
print("accuracy",accuracy)


###### precision  (   TP/TP+FP) predicted (1) how often am rigth
precision = precision_score(y,predictions)
print("precision",precision)


## recall real 1 did i find them all
recall = recall_score(y,predictions)
print("recall",recall)
### how are precision and recall balanced
f1= f1_score(y,predictions)
print(f1)