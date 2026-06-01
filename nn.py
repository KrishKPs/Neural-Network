import numpy as np 

test =[1,2,3]
test1= [2,3,4]

ans = np.dot(test,test1)

print(ans)

inputs = [2,3,4.8,7]




weights = [
    [0.12, -0.45, 0.78, 0.33],
    [-0.91, 0.24, -0.36, 0.67],
    [0.55, -0.18, 0.09, -0.72]
]
biases =[2,4,3.8]

output= np.dot(weights, inputs) +biases 

print(output)




output_check =[]

for neuron_weight , neuron_bias in zip(weights, biases):
    neuron_output=0
     
    for neuron_input , weight in zip(inputs, neuron_weight):
        neuron_output += neuron_input*weight
    
    neuron_output += neuron_bias 
    output_check.append(neuron_output)
    
    
print(output_check)
    

        
        
        
    


