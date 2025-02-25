# Mammo-Find
An LLM-based Web Visualization tool for Mammogram dataset recommendations 

## To run the code, follow the instructions below

- You will need Python 3.11.7

- You will need Ollama installed in your pc and have some LLMs downloaded

### 1) Clone the git repository
git clone https://github.com/RaiyanJahangir/Mammo-Find.git

### 2) Go to the root directory of the projects
cd Mammo-Find

### 3) Create a virtual environment 

// For Windows
py -3.11 -m venv myenv  

// For Linux
python3.11 -m venv myenv 

### 4) Activate the virtual environment 

// For Windows
myenv\Scripts\activate

// For Linux
source myenv/bin/activate

### 5) Install all the necessary packages and libraries
pip install -r requirements.txt

### 6) Now run the Graph_Generator.ipynb

// For Windows
python Graph_Generator.ipynb

// For Linux
python3 Graph_Generator.ipynb

### 7) After running the notebook, check index.html to see the generated graph

### 8) Then start the Flask Server by running app.py
This code activates the flask server and connects the LLM to the web interface for chatting.

// For Windows
python app.py

// For Linux
python3 app.py
