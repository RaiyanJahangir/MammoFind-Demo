# Mammo-Find
An LLM-based Web Visualization tool for Mammogram dataset recommendations 

## To run the code, follow the instructions below

- Install [Git](https://git-scm.com/downloads) 

- Install [Python 3.11.7](https://www.python.org/downloads/release/python-3117/) 

- Install [Ollama](https://ollama.com/) and pull some models you would like to use.

### Clone the git repository
```
git clone https://github.com/RaiyanJahangir/Mammo-Find.git
```

### Go to the root directory of the projects
```
cd MammoFind-Demo
```

### Create a virtual environment 

For Windows
```
py -3.11 -m venv myenv  
```

For Linux
```
python3.11 -m venv myenv 
```

### Activate the virtual environment 

For Windows
```
myenv\Scripts\activate
```

For Linux
```
source myenv/bin/activate
```

### Install all the necessary packages and libraries
```
pip install -r requirements.txt
```

### Now run the Graph_Generator.ipynb

For Windows
```
jupyter nbconvert --to notebook --execute --inplace Graph_Generator.ipynb

```

For Linux
```
jupyter nbconvert --to notebook --execute --inplace Graph_Generator.ipynb
```

### After running the notebook, check index.html to see the generated graph

### Then start the Flask Server by running app.py
This code activates the Flask server and connects the LLM to the web interface for chatting.
Make sure you change the model name you would like to use in app.py

For Windows
```
python app.py
```

For Linux
```
python3 app.py
```
