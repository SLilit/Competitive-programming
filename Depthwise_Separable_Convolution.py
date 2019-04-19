import numpy as np 

def separable_conv2d(C, H, W, R_H, R_W, F, input_t, dweights, pweights):
    #output for depthwise_separable convolution
    out_t = np.zeros([F, H, W])
    

    #padding the input_t on all sides with zeros 
    input_t = np.pad(input_t, pad_width = ((0, 0), (R_H//2, R_H//2), (R_W//2, R_W//2)), mode = "constant", constant_values = 0) 
    
    #output for depthwise convolution
    output_t = np.zeros([C, H, W]) 
    

    # for each input channel seperately apply its corresponding filter
    for c in range(C):
    	for h in range(H):
    		for w in range(W):
    			for r_h in range(R_H):
    				for r_w in range(R_W):
    					output_t[c][h][w] += input_t[c][h+r_h][w+r_w]*dweights[c][r_h][r_w]
   					
    #mixing step for each kernel
    for f in range(F):
    	for c in range(C):  
    		for h in range(H):
    			for w in range(W):
    				out_t[f][h][w] += output_t[c][h][w]*pweights[f][c]
    
    return out_t


print (separable_conv2d(3, 4, 4, 3, 3, 2, i, dw, pw))














