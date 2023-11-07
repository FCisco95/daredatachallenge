### Solution Description

#### Problem Statement

In this Dare Data Challenge, the goal was to build a machine learning model from an unknonw dataset. The challenge included setting up a containerized database server using Docker, developing a predictive model, deploying the model via an API, and creating unit tests. 

#### Technologies Used

The solution leveraged the following technologies:

- PostgreSQL for data storage.
- Python, including libraries like pandas, scikit-learn, and Flask.
- FLASK and REST API
- Amazon EC2.
- Docker for containerization.
- Git for version control.
- Unittest


#### Prerequisites and Steps

Ensure that you have the following prerequisites installed on your system:

Docker: Download and install Docker from its official website: https://www.docker.com/products/docker-desktop/

**Step 1**: Clone the Dare Data Challenge repository to your local machine using the following command:
git clone https://github.com/FCisco95/daredatachallenge

Navigate to the cloned repository directory:
cd DareDataChallenge

**Step 2**: Build the Docker image using the following command in the repository directory:
docker build -t joaovieira-challenge-postgres -f modules/de/docker/Dockerfile .

**Step 3**: Launch the Docker container for the PostgreSQL database using the following command:
docker run --name daredata-postgres-container -p 5432:5432 -d joaovieira-challenge-postgres

**Step 4**: Use the psql command to connect to the PostgreSQL database server running in the Docker container:
docker exec -it daredata-postgres-container psql -U admin -d daredatachallenge

**Step 5**: Install Dependencies. Navigate to the ds folder within the repository directory.
Execute the following commands to install the required dependencies:
python setup.py sdist bdist_wheel
pip install .

**Step 6**: Install Deployment Requirements
Navigate to the deployment folder within the repository directory.
Install the deployment requirements using the following command:
pip install -r requirements.txt

**Step 7**: Train the Model
From the deployment folder, run the following command to train the predictive model and generate the model.pkl file:
python train_model.py

**Step 8**: Deploy the API
From the deployment folder, execute the following command to start the API:
python app.py

**Step 9**: Access the API

Open your web browser and navigate to the following URL to interact with the deployed API:
http://ec2-174-129-115-238.compute-1.amazonaws.com:5001
This should display the API's index page, similar to the one provided in the tutorial.



### Implementation Timeline

Here's a breakdown of the implementation timeline and key milestones:

- **Database Setup (3 hours):** Setting up the PostgreSQL database using Docker, including initialization scripts and data loading. 

Had several dificulties managing to start the container, moving the initialization and loading scripts to the container due to path problems. Also had one small problem that got solved by tweaking the BIOS, something  with assisted virtualization(i love Windows), which didnt let me inicialize docker desktop.
I used a psql command to connect to the PostgreSQL database server and the program DBeaver to connect to the container and query the databset.

Commands used:
    cd /path/to/Dare Data Challenge
    docker build -t joaovieira-challenge-postgres -f modules/de/docker/Dockerfile .
    docker run --name daredata-postgres-container -p 5432:5432 -d joaovieira-challenge-postgres
    docker exec -it daredata-postgres-container psql -U admin -d daredatachallenge



- **Model Development (4 hours):** Data exploration, dataset selection (from Padel player rankings to Titanic dataset), model development, and evaluation. 

I initially spent 1-2 hours working with the Titanic dataset, believing it was permissible as I acquired it from a source other than Kaggle, which was listed as a restricted dataset. However, to ensure compliance, I switched to the World Padel Tour dataset from 2020. This dataset proved to be challenging due to its relatively small size and the effort required to extract meaningful insights. I spent an hour searching for the most suitable dataset before settling on this one. Subsequently, I invested 3 hours in creating additional columns, primarily to demonstrate my approach to dataset analysis and summarizing key characteristics. Additionally, I encountered initial schema and encoding mismatches within the dataset. While I considered more advanced models, I ultimately chose linear regression due to time constraints and the desired level of model accuracy. In this case, prioritizing project deadlines took precedence over extensive model refinement. A model with an R-squared of 0.8462 was deemed acceptable given the circumstances.

- **API Deployment (3 hours):** Following a tutorial and using Flask, the model was deployed as an API on an Amazon EC2 instance. 

I have to be honest,  the instructions regarding the folder structure and file placement in the IMPLEMENTATION.MD and READ.ME files were somewhat unclear. I struggled to determine the appropriate locations for notebooks, Python scripts, and other project files. This resulted in a less-than-ideal file organization.
I couldnt read the provided tutorial "Intro to ML APIs with Flask" and maybe thats why I felt problems on how to create model.pkl in order to use the model on my API.
To overcome these challenges, I utilized the index.html file from the tutorial as a starting point and adapted it to enhance the user interface for testing the predictive model.

Here's a summary of the commands I used from the ds folder:

    python setup.py sdist bdist_wheel
    pip install .
    navigate to deployment folder and run "pip install -r requirements.txt"
    from deployment folder run "python train_model.py " to create model.pkl

you can either run "python app.py" and go to localhost:5001 or open browser with this adress : http://ec2-174-129-115-238.compute-1.amazonaws.com:5001/ should be able to see the model running on a amazon EC2 instance (check the provided screenshots in the screenshots folder)


- **Unit Tests (1 hour):** Unit tests were created to ensure the API's components function correctly.  ´

I only created 2 basic ones, to get an idea how they work.
from deployment folder run :

    python -m unittest test_prediction 
    python -m unittest test_error_handling


- **Documentation (1 hour):** Step-by-step documentation was added, including this SOLUTION.md file.


### Summary

This was a challenging yet rewarding task that enhanced my understanding of the entire machine learning pipeline, from data preparation and model development to deployment and testing. The provided tutorials and materials were really helpful guiding me through the process.

The challenge was well-structured and provided an appropriate level of difficulty, allowing me to apply my existing knowledge while expanding my skillset. The hands-on experience gained from tackling the various aspects of the challenge has increased confidence in my ability to independently create and deploy machine learning models.

I am truly grateful for the opportunity to participate in this challenge and would like to express my sincere appreciation to the organizers for their efforts in providing such a valuable learning experience. 

