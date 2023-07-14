import pickle
import json
import numpy as np
import config

class PizzaPrice():
    def __init__(self,company,diameter,topping,variant,size,extra_sauce,extra_cheese):
        print("****** INIT Function *********")
        # self.company= company_labels
        # self.diameter = diameter
        # self.topping = topping_labels
        # self.variant = variant_labels
        # self.size = size_labels
        # self.extra_sauce = extra_sauce_labels 
        # self.extra_cheese = extra_cheese_labels

        self.company= company
        self.diameter = diameter
        self.topping = topping
        self.variant = variant
        self.size = size
        self.extra_sauce = extra_sauce 
        self.extra_cheese = extra_cheese
 
    
    def __load_saved_data(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predicted_price(self):
        self.__load_saved_data()

        # company = self.json_data['company'][self.company]
        # topping = self.json_data['topping_labels'][self.topping]
        # variant = self.json_data['variant_labels'][self.variant]
        # size = self.json_data['size_labels'][self.size]
        # extra_sauce = self.json_data['extra_sauce_labels'][self.extra_sauce]
        # extra_cheese = self.json_data['extra_cheese_labels'][self.extra_cheese_]


        company = self.json_data['company'][self.company]
        topping = self.json_data['topping'][self.topping]
        variant = self.json_data['variant'][self.variant]
        size = self.json_data['size'][self.size]
        extra_sauce = self.json_data['extra_sauce'][self.extra_sauce]
        extra_cheese = self.json_data['extra_cheese'][self.extra_cheese]
        
    
        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = company
        test_array[0,1] = self.diameter
        test_array[0,2] = topping
        test_array[0,3] = variant
        test_array[0,4] = size
        test_array[0,5] = extra_sauce
        test_array[0,6] = extra_cheese

        predicted_price = np.around(self.model.predict(test_array)[0],3)
        return predicted_price