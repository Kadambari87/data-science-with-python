from scipy.io import arff
import pandas as pd
import matplotlib.pyplot as plt

data = arff.loadarff("\cc_fraud_detection.arff")

df = pd.DataFrame(data[0])
plt.subplot(1,2,1);


plt.plot(df['cc_age'],df['purpose'], color='red') 
plt.plot(df['cc_age'], df['personal_status'], color='blue')

plt.xlabel('Age of person');
plt.ylabel('Purpose of each male/female');

plt.xlim('30-60');
plt.title('Purpose and gender of people at differnt ages(30-60)')

plt.show()
