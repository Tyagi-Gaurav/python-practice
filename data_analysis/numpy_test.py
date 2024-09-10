import numpy as np

my_arr = np.arange(50)
print (my_arr)

my_list = list(range(50))
print (my_list)

#Multiply each sequence by 2
my_arr2 = my_arr * 2
print (my_arr2)

my_list_2 = [x * 2 for x in my_list]
print (my_list_2)

#Multi-dimensional array
data = np.array([[1.5, -0.1, 1.3], [0, -3, 6.5]])
print (data)

print (data * 10) #Multiply all elements of array with 10
print (data + data) #Adding array to each other
print (data.shape) #Shape of data
print (data.dtype) #Data type

print (np.zeros(10)) #Creating array of zeros
print (np.zeros((3,6))) #Multi-dimensional array of zeros

print (np.array([1,2,3], np.float32)) #Creating a float type array
print (np.array([1,2,3], np.int32)) #Creating a int32 type array
print (np.array(["1","2","3"]).astype(np.int32)) #Converting a string array to int
points = np.arange(-5, 5, 0.01) # One dimensional array between -5 & 5 with diff
xs, ys = np.meshgrid(points, points)