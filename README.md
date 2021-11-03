# Software Engineering for Machine Learning Assignment

## API

The expected feature inputs are of the following:
- age - student's age (numeric: from 15 to 22)
- Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
- Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
- health - current health status (numeric: from 1 - very bad to 5 - very good)
- absences - number of school absences (numeric: from 0 to 93)


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
To deploy, run the following commands in the `dockerfile` directory from the command line:

```
docker build -t ml:latest .

docker run -d -p 5000:5000 ml
```
Consider using the `--no-cache` flag during build if changes do not seem to be propogating. 

After the docker container is deployed, the prediction service is available through `localhost:5000/predict` and can either be visited (with args in the url) or `curl`-ed for prediction result. An example usage could look something like this:

```
curl http://localhost:5000/predict?age=18&absences=0&health=5&Walc=1&Dalc=1
```


## Testing
