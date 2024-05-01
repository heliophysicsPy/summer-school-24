## How does Machine Learning work?

<B>Contributing authors:</B> <BR>
Evana Gizzi, Ph.D., AI Researcher NASA GSFC</i><BR>
Richard Licata, Ph.D., Data Scientist, CACI International</i><BR>
Barbara J. Thompson, Heliophysicist, NASA GSFC</i>

### Key Elements of Machine Learning

Arthur Samuel (1959) -- Field of study that gives computers the ability to learn without being explicitly programmed.

Tom Mitchell (1998) --   A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.

- E is your input data.  It can be numbers, images, words, sounds (waveforms).
- T is your intended output.  It can be a label, a value, a boolean, a  decision, or “can this be separated into groups?” 
- P is the thing that is special about machine learning. It allows the model to decide how to solve the problem instead of having one explicitly programmed.  

Nearly all "AI Fails" can be traced to any or all of these three elements.


## Neural Networks and deep learning

Neural networks (NNs) are essentially a network of matrices and functions
Fitting process updates the values in each matrix to better fit the data
NNs can be very simple or extremely complex
Usually depends of the problem at hand
Important parameters in building a NN
Number of hidden layers
Number of neurons in each layer
Activation functions
Optimizer
Loss function



## Loss Functions

Loss functions are (objectively) the most important choice when building a NN
They define the goal of the model
Most common loss function is mean square error (MSE)
Used most commonly in regression problems (fitting a function)


Other common loss functions include:
Mean absolute error (regression)
Binary crossentropy (mostly classification)



## Optimizers 


We compute the gradientswith respect to the loss function

The optimizer is the algorithm that determines how you move through the gradient surface

Most basic approach is gradient descent



## Activation Functions

Common activation functions:
Linear
Sigmoid
Tanh
ReLU
Softmax
Other activation functions:
Softsign
Softplus
ELU
Leaky ReLU
PReLU
And many more


## Perceptron



Dataset: x, y coordinates as inputs with binary outputs for classification
Blue = 0, red = 1
Goal is to learn the relationship between petal width, stem height, and color
Need to choose learning rate, numberof epochs, activation function, and optimizer
Activation function: sigmoid (easy deriv.)
Optimizer: standard gradient descent

https://drive.google.com/file/d/1ozbESbOJTF4b9pVqd-ODCorM2y9yR9D7/view?usp=sharing

## Perceptron Exercise



Build a perceptron to solve this classification problem from scratch
Open Google Colab link on Github page



## Python ML Libraries



Two major libraries for ML in Python are TensorFlow and Pytorch
Tensorflow has Keras application program interface (API)
Keras makes building models simple
Pytorch is easier to get creative with
Complex architectures
More intricate training algorithms
Reality: you can do most things whether you use TensorFlow or Pytorch
Both libraries are commonly used in research and industry
We will use TensorFlow and Keras

