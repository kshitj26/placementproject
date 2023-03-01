import json
import pickle
import config
import numpy as np


class Placement():
    

    def __load_model(self):
        with open (r"D:\Velocity17Sep2022\workspace_git\Student_placement\artifacts\Logistic_Model","rb") as f:
            self.logistic_model= pickle.load(f)

        with open (r"D:\Velocity17Sep2022\workspace_git\Student_placement\artifacts\Project_data.json","r") as f:
            self.data = json.load(f)
        
        
    def get_prediction(self,gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p):
        self.__load_model()
        self.gender = gender
        self.ssc_p = ssc_p        
        self.ssc_b = ssc_b     
        self.hsc_p = hsc_p      
        self.hsc_b = hsc_b 
        self.hsc_s = hsc_s        
        self.degree_p = degree_p    
        self.degree_t = degree_t     
        self.workex = workex    
        self.etest_p = etest_p   
        self.specialisation = specialisation
        self.mba_p = mba_p
        
        arr = np.zeros(self.logistic_model.n_features_in_)
        print(arr)
        arr[0] = self.data["Gender"][self.gender]
        arr[1] = self.ssc_p
        arr[2] = self.data["SSC_B"][self.ssc_b]
        arr[3] = self.hsc_p
        arr[4] = self.data["HSC_B"][self.hsc_b]
        arr[5] = self.data["HSC_S"][self.hsc_s]
        arr[6] = self.degree_p
        arr[7] = self.data["Degree_T"][self.degree_t]
        arr[8] = self.data["WorkEx"][self.workex]
        arr[9] = self.etest_p
        arr[10] = self.data["Specialisation"][self.specialisation]
        arr[11] = self.mba_p
        print(arr)
        self.prediction = self.logistic_model.predict([arr])[0]
        return self.prediction
      