class actInfo():
    def getFields(n):
        #PA 1 fields
        if n == 1:
            x = [0.625, 0.7933,0.625, 0.4567, 0.625, 0.9617, 0.8631, 0.625, 0.3869,
                 0.2883,0.3869, 0.625, 0.8631, 1.13, 1.0623, 0.8775, 0.625, 0.3725, 
                 0.1877, 0.12, 0.1877, 0.3725, 0.625, 0.8775, 1.0623]
            y = [0.48, 0.48, 0.6483, 0.48, 0.3117, 0.48,  0.7181, 0.8167, 0.7181,
                 0.48, 0.2419, 0.1433, 0.2419,  0.48, 0.7325, 0.9173, 0.985, 0.9173, 
                 0.7325,  0.48, 0.2275, 0.0427, -0.025, 0.0427, 0.227]
            
  
        if n == 2: 
            x = [-0.625000, -0.456667, -0.625000, -0.79333, -0.625000, -0.288333,
                 -0.386941,-0.625000, -0.863059, -0.961667, -0.863059, -0.625000, 
                 -0.386941, -0.120000,-0.187657, -0.372500, -0.625000, -0.877500, 
                 -1.06234, -1.13000,-1.06234, -0.877500, -0.625000, -0.372500, 
                 -0.187657]
            y = [0.480000, 0.480000, 0.648333, 0.480000, 0.311667, 0.480000, 0.718059, 
                 0.816667, 0.718059, 0.480000,0.241941,  0.143333, 0.241941, 0.480000, 
                 0.732500, 0.917343, 0.985000, 0.917343, 0.732500, 0.480000, 0.227500, 
                 0.0426571, -0.0250000, 0.0426571, 0.227500]
        if n == 3:
            x = [0, 0.156667, -6.84812e-009, -0.156667, 1.86823e-009, 0.313333, 
                 0.22156, -1.36962e-008, -0.22156, -0.313333, -0.22156, 3.73646e-009, 
                 0.22156, 0.47, 0.407032, 0.235, -2.05444e-008, -0.235,-0.407032, 
                 -0.47, -0.407032, -0.235, 5.60469e-009, 0.235, 0.407032]
            y = [-0.75, -0.75, -0.570333, -0.75, -0.929667, -0.75, -0.495913, 
                 -0.390667, -0.495913, -0.75, -1.00409, -1.10933, -1.00409,
                 -0.75, -0.4805, -0.283212, -0.211, -0.283212, -0.4805, -0.75, 
                 -1.0195, -1.21679, -1.289, -1.21679, -1.0195]
            
        return x, y
    def getMirrorSurfaces():
        return [4, 5]
