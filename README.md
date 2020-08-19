# Full-cycle_ML_Solution project
## Evaluation of the results of financial and economic activities of enterprises of the public sector of the economy (Ukraine)

## Motivation
Create an automatic solution for evaluating the results of financial and economic
activities of public sector enterprises in Ukraine using machine learning and open
data

## Open data


The data I use is open data of the "Unified State Web Portal of Open Data of Ukraine".
Information on the evaluation of the results of financial and economic activities of 
economic entities of the public sector of the economy belonging to the sphere of 
management of the Ministry of Energy and Coal. Data for the year are published by
March 25. Data for every 3 months.    

Link - https://data.gov.ua/dataset/dfb59d73-9bf1-49c3-b9b9-2760914d2d64

<div align="center">
    <img align="center" src="https://github.com/Vitalii36/full-cycle_ML_Solution/blob/master/image_readme/Logo.png?raw=true">
</div>

<div align="center">
    <img align="center" src="https://github.com/Vitalii36/full-cycle_ML_Solution/blob/master/image_readme/Table.png?raw=true">
</div>

## Solution implementation

Data processing and SVC model from the sklearn library was used for decision making and accuracy on test sample was achieved - 0.92. The model is saved in an SVC.pickle file, which is then 
used to implement the solution. Developed web API.

## How to use
We should install pip install -r requirements.txt
    
    click==7.1.2
    Flask==1.1.2
    itsdangerous==1.1.0
    Jinja2==2.11.2
    joblib==0.16.0
    MarkupSafe==1.1.1
    numpy==1.19.1
    pandas==1.1.0
    python-dateutil==2.8.1
    pytz==2020.1
    scikit-learn==0.23.2
    scipy==1.5.2
    six==1.15.0
    sklearn==0.0
    threadpoolctl==2.1.0
    Werkzeug==1.0.1
    
To use you need to download a repo clone or docker image - 'pull vitalii36/full_cycle_ml_solution_project'.
So, we'll be able to GET predicts via API routes.   
    
We'll use the following routes method:

GET to retrieve information from the source

We'll have the following route:

/predicts:

GET: get predicts, the body can include:
all columns with data in json format

A Jupiter notebook is used to form the test data "json_convert_testdata.ipynb"
and https://jsonformatter.curiousconcept.com/#

## Start
If cloned repo, in the directory run from the terminal app.py, if the docker 
    
    sudo docker run -p 8000:8000 --network host full_cycle_ml_solution_project

## Example

<div align="center">
    <img align="center" src="https://github.com/Vitalii36/full-cycle_ML_Solution/blob/master/image_readme/Example_1.png?raw=true">
</div>


## License
Format is MIT
