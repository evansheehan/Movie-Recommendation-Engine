import training_and_test_set_generator as generator
import naive_bayes_log as nb_log
import numpy as np
import matplotlib.pyplot as plt

accuracy_list = []
accuracy_list_mean = []
iterations = 50
liked_training_size_ratio = 0.1
disliked_training_size_ratio = 0.9

for i in range(iterations):
    liked_training_ratio, disliked_training_ratio = generator.reset_data(liked_training_size_ratio, disliked_training_size_ratio)
    accuracy_list.append(nb_log.run_nb_log())
    accuracy_list_mean.append(np.mean(accuracy_list))
    
plt.ylim(0, 1)
plt.text(0.25, 0.05, fontsize="small", s="Iterations: " + str(iterations) + " | Ratio of liked training set: "
+ str(liked_training_size_ratio) + " | Ratio of disliked training set: " + str(disliked_training_size_ratio)
+ "\nMean accuracy: " + str(round(np.mean(accuracy_list), 3)) + " | Variance: " + str(round(np.var(accuracy_list), 3)))
plt.plot(accuracy_list, color="black", alpha=0.25)
plt.plot(accuracy_list_mean)
plt.show()
print("Variance is: " + str(np.var(accuracy_list)))
print("Total average mean is: " + str(np.mean(accuracy_list_mean)))
print("debug")