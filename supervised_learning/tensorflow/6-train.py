#!/usr/bin/env python3
"""
    function def train(X_train, Y_train, X_valid, Y_valid,
    layer_sizes, activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    that builds, trains, and saves a neural network classifier:
"""


import tensorflow as tf
create_placeholders = __import__('0-create_placeholders').create_placeholders
forward_prop = __import__('2-forward_prop').forward_prop
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_train_op = __import__('5-create_train_op').create_train_op

def train(
    X_train,
    Y_train,
    X_valid,
    Y_valid,
    layer_sizes,
    activations,
    alpha,
    iterations,
    save_path="/tmp/model.ckpt",
):
    tf.reset_default_graph()

    # Create placeholders
    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])

    # Build the forward propagation graph
    y_pred = forward_prop(x, layer_sizes, activations)

    # Calculate loss and accuracy
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)

    # Create the training operation
    train_op = create_train_op(loss, alpha)

    # Add variables to collections
    tf.add_to_collection("x", x)
    tf.add_to_collection("y", y)
    tf.add_to_collection("y_pred", y_pred)
    tf.add_to_collection("loss", loss)
    tf.add_to_collection("accuracy", accuracy)
    tf.add_to_collection("train_op", train_op)

    # Initialize all variables
    init = tf.global_variables_initializer()

    # Create a saver object
    saver = tf.train.Saver()

    # Start a TensorFlow session
    with tf.Session() as sess:
        sess.run(init)

        for i in range(iterations + 1):
            # Train the model
            sess.run(train_op, feed_dict={x: X_train, y: Y_train})

            # Print metrics every 100 iterations and at the last iteration
            if i % 100 == 0 or i == iterations:
                train_cost = sess.run(loss, feed_dict={x: X_train, y: Y_train})
                train_accuracy = sess.run(
                    accuracy, feed_dict={x: X_train, y: Y_train}
                    )
                valid_cost = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
                valid_accuracy = sess.run(
                    accuracy, feed_dict={x: X_valid, y: Y_valid}
                    )

                print("After {} iterations:".format(i))
                print("\tTraining Cost: {}".format(train_cost))
                print("\tTraining Accuracy: {}".format(train_accuracy))
                print("\tValidation Cost: {}".format(valid_cost))
                print("\tValidation Accuracy: {}".format(valid_accuracy))

        # Save the model
        save_path = saver.save(sess, save_path)

    return save_path
