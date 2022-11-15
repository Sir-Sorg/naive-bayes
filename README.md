# naive-bayes
In this project, by using the **simple/naive Bayes** classification algorithm, we will check the gender of the samples according to 4 other factors.
which was assigned to us as the first project in the course of fundamentals of computational intelligence in the university 🏦.
# What is bayes 🤔
Naive Bayes is a simple technique for constructing classifiers: models that assign class labels to problem instances, represented as vectors of
feature values,
where the class labels are drawn from some finite set. all naive Bayes classifiers assume that the value of a particular feature is independent of
the value of
any other feature, given the class variable. For example, a fruit may be considered to be an apple if it is red, round, and about 10 cm in diameter.
A naive Bayes classifier considers each of these features to contribute independently to the probability that this fruit is an apple,
regardless of any possible correlations between the color, roundness, and diameter features.

you can read full article in [Wikipedia 📄](https://en.wikipedia.org/wiki/Naive_Bayes_classifier).
# Code 💻
In this section, I briefly explain the code and how program works.
## Reading data 👓
As it is clear from the names, by using a function called `readData`, we read the information from the `CSV file` and put it in a `list`,
according to the
missing values, this information needs to be cleaned or processed using the `cleanData` function. will be done.
## Data segmentation 🔪
In a very simple way, now we have to divide the clean information into two groups, one for training and one for testing the program
I did this in a ratio of 70% to 30% and created two lists, `trainingData` and `testingData`.
## Making a dictionary of possibilities 🎲
We almost reached the most important part of the code, as you know, now for training, we need to divide the information into
appropriate groups according to the labels.
Here, according to the existence of two groups of information, we divide it into two groups, ***male*** and ***female***.

In the next step, we have to extract the features, for this I have used the ‍‍`findFeature` function, and considering that each 
category of information is different from the other category, such as `skin color` and `education` Byder, we could make a difference
in saving them in the dictionary, for this reason, I made 4 separate dictionaries and using the nested dictionaries, I placed them
according to the Index number that is in the main list of raw data.

Now we have the number of repetitions of each feature in a specific category, and we just need to calculate its ratio to the total,
for which I have used a function called `percentageFeature`.
## Predict 🔮
At the beginning of the prediction, we should also consider the classes themselves, which I put in the dictionaries as the **5th** scholars.

Now, by using a function called ‍`findChance`, it is enough to get a list as an example and by finding the chance of its occurrences and
multiplying them together plus multiplying the prior of the class, we can find the chance of that class.

Using the `predict` function, we only calculate the chance of the existence of the sample in the two classes, and by comparing the two classes,
we output the class that had the highest chance.
## Testing 🔬
In the last step, by taking a large list of samples and running the `Predict` in `testing` function on them one by one and comparing the output with the real
label of that class, we obtain the number of correct and incorrect predictions and show the accuracy of the program as output.
## Result 🧠
Finally, the program reported about ***79% accuracy*** according to the above operations.
# last word 🧦
In the end, I am glad that you used this program and if you like, you can modify parts of the program and I will definitely accept your pull request.
