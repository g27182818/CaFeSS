import numpy as np

input_temps = np.arange(1, 13)
print(input_temps)

# Initialize array
input_array = np.zeros((2, 2, 3))
# Initialize observed temperatures
obs_temps = np.zeros((4,4,3))

# Asign inputs to array
count = 0
for i in range(input_array.shape[0]):
    for j in range(input_array.shape[1]):
        for k in range(input_array.shape[2]):
            input_array[i,j,k] = input_temps[count]
            count+=1

# Make symmetric complete array
first_flip = np.flip(input_array, axis = 0)
second_flip = np.flip(input_array, axis = 1)
third_flip =  np.flip(first_flip, axis = 1)

# Assign to final obs_temps
obs_temps[:2,:2,:] = input_array
obs_temps[2:,:2,:] = first_flip
obs_temps[:2,2:,:] = second_flip
obs_temps[2:,2:,:] = third_flip
