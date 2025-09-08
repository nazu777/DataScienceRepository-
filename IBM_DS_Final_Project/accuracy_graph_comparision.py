import matplotlib.pyplot as plt


classifiers = ['Decision Tree', 'K Neighbors', 'Logistic Regression', 'SVM']
accuracy = [0.9035714285714287, 0.8482142857142858, 0.8333333333333334, 0.8333333333333334]

plt.figure(figsize=(8, 5))
bars = plt.bar(classifiers, accuracy, color='skyblue')
plt.title('Classifier Accuracy Comparison')
plt.xlabel('Classifier')
plt.ylabel('Accuracy')
plt.ylim(0.8, 0.95)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add accuracy values on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.002, round(yval, 4), ha='center', va='bottom')

plt.show()