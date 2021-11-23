# -*- coding: utf-8 -*-
import pickle

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))
               
               
msg_file = open('cache_fileMG3O7oMJixl3CPZEN4D5', 'r')
msg=msg_file.read()
msg_file.close()

data = [msg]
vect=cv.transform(data).toarray()
prediction=model.predict(vect)
#result=prediction[1]
if prediction==1:
      print('This is a spam mail')
else:
      print('This is a ham mail')

