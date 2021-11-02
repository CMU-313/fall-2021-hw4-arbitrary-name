# Software Engineering for Machine Learning Assignment

## API


## Comparing Models

The baseline model uses the following features:

1. Age
2. Health
3. Absences

and has the following performance:

- F1 Score: 0.5357
- Accuracy: 0.8683
- Precision: 0.7692
- Recall: 0.4110

Our model uses the following features instead:

1. Age
2. Health
3. Absences
4. Walc (Weekend alcohol consumption)
5. Dalc (Workday alcohol consumption)

and has the following performance.

- F1: 0.7692
- Accuracy: 0.9241
- Precision: 0.8772
- Recall: 0.6849

We note here that based for all of our metrics, our updated model which includes the student's alcohol consumption performs better than the baseline. 

NOTE: Given our limited data, we did not perform a train/test data split, and instead both train and test on the whole dataset.


## Deployment Instructions
To deploy, run the following commands in the dockerfile directory from the command line:

```
docker build -t ml:latest .

docker run -d -p 5000:5000 ml
```

## Testing
