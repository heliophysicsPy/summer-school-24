## How does Machine Learning work?

### Key Elements of Machine Learning

Arthur Samuel (1959) -- Field of study that gives computers the ability to learn without being explicitly programmed.

Tom Mitchell (1998) --   A computer program is said to learn from experience **E** with respect to some task **T** and some performance measure **P**, if its performance on **T**, as measured by **P**, improves with experience **E**.

- **E** is your input data.  It can be numbers, images, words, sounds (waveforms).
- **T** is your intended output.  It can be a label, a value, a boolean, a  decision, or “can this be separated into groups?” 
- **P** is the thing that is special about machine learning. It allows the model to decide how to solve the problem instead of having one explicitly programmed.  

The second definition more clearly explains the key components of machine learning. Nearly all "AI Fails" can be traced to any or all of these three elements. 

The **first stage of ML** is collecting the input data, or **E**. It is sometimes referred to as "data prep" or "data wrangling."  

The **second stage is data exploration** - getting to know your data and understanding its behavior and basic statistics so you can determine which models may work best. Choosing a model requires careful consideration of both the data and the task (or goal, output, etc.). Sometimes you also want to expicitly consider the performance measure and other times the performance measure is inherent in the model.  

Once you have chosen a candidate model, you **train** the model to perform the task. A typical approach is called the **"train-validation-test split."** In this case, most of the data (usually 60-80%) is used to fit the model. The model creates a "hypothesis," evaluates how it performs the task on the training set, and then refines the hypothesis to improve the performance. 

It is possible that the model can perform perfectly on the training set. For example, if you have *n* values, the model can result in a polynomial of *n-1* dimensions that exactly hits every data point. However, if you add a new data point, the model may perform poorly. This is called **overfitting.**  A model performs perfectly on a discrete set of data but does not generalize to the other data that you intend to use. In contrast, a model can **underfit** the data, which usually meaning that the model is too simple to be useful. 

![Underfitting and Overfitting Diagram, by Aarthi Kasirajan https://medium.com/@minions.k/underfit-and-overfit-explained-8161559b37db 
](/aiml-tutorial/images/under_overfitting.png)

Thus, a model must strike the right balance between overfitting and underfitting. When the model is using the training set and improving according to the performance measure, it is working to reduce the *bias* in the model due to underfitting. To mitigate this tendency, a *validation* set is used to fine-tune the model. If the model has *high variance* and overfits the data, then it will not perform well on the validation set.  The validation set is used to update the **hyperparameters** of the model, which modifies the structure of the model and can be used to penalize overfitting. Thus, the interplay of the training and validation sets allow the model to work towards a robust fit of the data. Finally, the third "split" of the data, the testing set, is used to evaluate how well the model performed overall. 

## Types of models

There are a variety of machine learning models, and they are growing every day. (For a good overview, see <a href="https://medium.com/@amit.rajawat12/understanding-different-types-of-machine-learning-models-a-practical-guide-0dfee67a3605">"Understanding Different Types of Machine Learning Models: A Practical Guide"</a> from *medium.com*).

### Regression

**Linear regression** is one of the first types of models that you learn. It predicts the value of unknown data based on the input of known data.  They are particularly useful when you want to understand the relationship or correlation between different variables. 

An x vs. y least-squares-fit is a common form of linear regression, but there are many more linear regression models!  

Regression can model both continuous and and discrete variables. **Logistic regression** takes input variables and models the probability of a set of possible outcomes. A common use of logistic regression is prediction of a "yes" or "no" outcome:  Will there be a solar flare?  Will there be a geomagnetic storm?  

### Dimensionality Reduction and Clustering Models

Dimensionality reduction and clustering are common *unsupervised* approaches, meaning you are trying out different representations of the data to see if one provides insight or utility. If you have a complicated dataset and want to turn it to something more manageable, these models are very useful.  

Dimensionality reduction seeks to transform the dataset into fewer dimensions (typically 2 or 3 dimensions) without destroying the useful statistical properties.  A common dimension reduction in Heliophysics is taking *x,y,z* components of plasma velocity and magnetic field, and re-projecting them in two coordinates: normal and transverse to the prevailing magnetic field direction (*Bn* and *Bt*). 

However, if it's not clear what coordinates would serve best for a particular dataset, unsupervised ML models can determine the most information-preserving transformations.  

Clustering is useful when you want to determine whether the data can be organized into separate groups, but you're not sure how those groups are defined. There are many types of clustering models, and sometimes the best way to determine which works best for a particular dataset is to try them out and see how they do.  

<a href="https://www.kaggle.com/code/samuelcortinhas/intro-to-pca-t-sne-umap">This article by Samuel Cortinhas on kaggle.com</a> concisely describes several models and compares performance on a distribution of data. 

**<font color = red>Our first exercise will focus on data clustering using a simple K-means model.</font>**

### Decision Trees

Decision trees are models that consist of nodes that apply tests to the data resulting in final results or decision in the resulting "leaves." 

![Simple Decision Tree Diagram
](/aiml-tutorial/images/decision_tree.png)

Two common type of decision tree models are **random forests** and **gradient boosting models**.  A random forest combines the output of many individual trees to create a single result, while a gradient boosting model builds one tree at a time, with each consecutive tree, iterating to improve performance.  

A good example of decision trees in Heliophysics is "Timing of the solar wind propagation delay between L1 and Earth based on machine learning" by <a href="https://www.swsc-journal.org/articles/swsc/full_html/2021/01/swsc200105/swsc200105.html">Baumann and McCloskey (J. Space Weather Climate, v. 11, 2021)</a>. They compare performance of both random forest and gradient boosting and find results that are superior to linear regression.  

### Classifiers, Decision Boundaries, and Support Vector Machines

Another general area of machine learning models are **decision boundaries**, which divide a dataset into subsets separated by boundaries.  A common decision boundary model is called a **Support Vector Machine**, or **SVM**. SVMs create *hyperplanes* that separate an n-dimensional parameter space into different sections.

Decision boundaries are often used in forecasting, to estimate the probability of an event occurring. <a href="https://helioml.org/02/Predicting_Coronal_Mass_Ejections.html">An example of SVMs and the associated code can be found in the Helio-ML Online Textbook</a> from a paper by <a href="https://ui.adsabs.harvard.edu/abs/2016ApJ...821..127B/abstract">Bobra & Ilonidis (Astrophysical Journal, 821, 127, 2016)</a>. The model aims to determine whether a flaring region on the Sun will produce an eruption (called a coronal mass ejection). The paper also has an excellent example of using an **interpretable machine learning method** to improve the understanding of the flaring system. 

<a href="https://helioml.org/05/Scintillation_Prediction.html">McGranaghan et al. (Space Weather, V. 16, issue 11, 2018)</a> use an SVM to predict high-latitude ionospheric phase scintillation (small-scale structures in the ionosphere that can distort or impede radio signals) using Global Navigation Satellite Systems (GNSS) data. <a href="https://helioml.org/05/notebook.html">The full code and description, including an excellent analysis with data exploration and feature importance, are available in the Helio-ML Online Online Textbook.</a>  

<font color = red>Our second and third exercises focus on decision boundaries.</font>

### Neural networks

An excellent description of how neural networks work can be found in <a href="https://www.3blue1brown.com/topics/neural-networks">3Blue1Brown's video series</a>.

(NNs) are usually the most well recognized of the machine learning models. They can be relatively simple, or they can be extremely complex.

NNs are essentially a network of matrices and functions. Each set of matrices and functions forms a "layer." The fitting process updates the values in each matrix to better fit the data, and the "neural" aspect is how the outputs from one layer are passed through an **activation function** that applies a weighting factor that can increase or decrease the strength of a value. The activation functions allow the neural network to respond differently to different inputs - in some cases a value may be important while in other cases it is not. A simple activation function may return "1" if the value exceeds a threshold, and "0" otherwise. 

An excellent review of activation functions can be found at <a href="https://www.kdnuggets.com/2022/06/activation-functions-work-deep-learning.html">How Activation Functions Work in Deep Learning" on kdnuggets.com</a>. The following figure from the article shows the behavior of several activation functions.


**Common Activation Functions**:
![Common activation functions, figure adapted from kdnuggets.com https://www.kdnuggets.com/2022/06/activation-functions-work-deep-learning.html 
](/aiml-tutorial/images/activations.png)


**Neural Network Structure**:

Important parameters in building a NN:
- Number of hidden layers
- Number of neurons or perceptrons in each layer
- Activation functions
- Optimizer 
- Loss function (performance measure)

<font color = red>In our final exercise, we will build a neural network classifier model.</font>  

## Loss Functions and Performance Measures

A common performance measure is represented by a **loss function**, or **cost function**. A cost function is constructed from parameters that represent how far off the model is from "perfect" performance.  They quantify the model's output relative to the target output. It is rare to achieve perfect performance (because datasets are rarely perfect), so the objective of the model is to find a solution that minimizes the total cost.  

![Simple Decision Tree Diagram
](/aiml-tutorial/images/performance_measure.png)

**Loss functions**, or error functions, can be the most important choice when building a neural network. They define the goal of the model, provide a measure of success, and can make the difference between an effective and ineffective model.

A common loss function is mean square error (MSE).  MSE is often used in regression problems (fitting a function) - a simple least-squares-fit is an example of one.

<a href="https://www.datacamp.com/tutorial/loss-function-in-machine-learning">This article by Richmond Alake on datacamp.com describes a variety of loss functions and how they are commonly used.</a>


## Optimizers 

![Learning rate and loss function diagram, from "Optimizers in Deep Learning" https://musstafa0804.medium.com/optimizers-in-deep-learning-7bf81fed78a0 
](/aiml-tutorial/images/gradient_loss.png)

The most basic way to iterate on a solution is to compute the gradients with respect to the loss function and update the model towards the direction of decreasing loss. However, there are multiple pitfalls to simply following the gradients: loss functions can have local minima that are not the global minimum, and extremely complex models can be computationally expensive and take a long time to converge.   

An **optimizer** is an algorithm that determines how the model navigates the performance measure. In our final learning exercise, we will compare how simple gradient descent (SGD) compares to Adaptive Moment Estimation (usually referred to as Adam).  

For an excellent overview of different optimizers, see <a href="https://musstafa0804.medium.com/optimizers-in-deep-learning-7bf81fed78a0">"Optimizers in Deep Learning" on medium.com</a>.


