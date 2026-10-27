import tensorflow as tf

# scalar tensor (0D tensor)
scalar_tensor = tf.constant(11)
print("Scalar Tensor : ",scalar_tensor)

# 1D tensor (Vector)
vector_tensor = tf.constant([11,21,51,101])
print("Vector tensor : ",vector_tensor)

# 2D tensor (Matrix)
matrix_tensor = tf.constant([[10,20,30],[40,50,60]])
print("Matrix tensor : ",matrix_tensor)

# 3D tensor
tensor_3d = tf.constant([
    [[1,2],[3,4]],
    [[5,5],[6,6]],
    [[7,8],[9,10]]
])

print("3D tensor : ",tensor_3d)