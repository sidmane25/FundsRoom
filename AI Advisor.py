import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense, Concatenate

# Assume you have a dataset with user-item interactions
# For simplicity, we'll create dummy data
users = [0, 1, 2, 3]
items = [0, 1, 2, 3]
ratings = [5, 4, 3, 2]

# Define the user and item inputs
user_input = Input(shape=(1,))
item_input = Input(shape=(1,))

# Create embedding layers for users and items
user_embedding = Embedding(input_dim=len(users), output_dim=10)(user_input)
item_embedding = Embedding(input_dim=len(items), output_dim=10)(item_input)

# Flatten the embeddings
user_flat = Flatten()(user_embedding)
item_flat = Flatten()(item_embedding)

# Concatenate user and item embeddings
concatenated = Concatenate()([user_flat, item_flat])

# Fully connected layer
fc_layer = Dense(10, activation='relu')(concatenated)

# Output layer with sigmoid activation (for binary classification)
output = Dense(1, activation='sigmoid')(fc_layer)

# Model creation
model = Model(inputs=[user_input, item_input], outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Dummy data
user_array = tf.constant(users, dtype=tf.int32)
item_array = tf.constant(items, dtype=tf.int32)
rating_array = tf.constant(ratings, dtype=tf.float32)

# Training the model (using dummy data)
model.fit([user_array, item_array], rating_array, epochs=10)

# Now, you can use this model to predict ratings or generate recommendations.
