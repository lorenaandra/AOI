# Area Of Interest (AOI) - Recommendation System

## Recommendation Systems in Digital Libraries - Leveraging arXiv
### Introduction to Recommendation Systems in Research Libraries
Recommendation systems play a crucial role in enhancing user experiences within digital libraries, 
such as [arXiv](https://arxiv.org/), a prominent repository for scholarly articles in various fields of science and technology.
Arxiv contains a vast volume of academic content, aspect which makes it perfect for our project in Big Data.

### Role of Recommendations in arXiv
Within arXiv, recommendation systems leverage various algorithms and data processing techniques to suggest 
articles tailored to users' interests, preferences, and historical interactions. 
These systems aid researchers, academics, and enthusiasts in efficiently navigating through the extensive 
collection of papers, enabling them to discover pertinent research in their fields of interest.

### Purpose of this Repository
The objective of this repository is to explore, implement, and enhance recommendation systems within the context of arXiv 
in the domain of computer science. It includes notebooks, datasets, and scripts aimed at developing robust and efficient 
recommendation systems tailored to the needs of researchers and academics navigating the vast expanse of scholarly articles in arXiv.
We created two types of recommendation systems: [content-based filtering](#content-based-filtering-recommendation-system) and a [hybrid approach of collaborative filtering and content-based filtering](#hybrid-recommendation---recommendation-system-based-on-collaborative-and-content-based).



## Usage Instructions
### Create Environment
`python -m venv .venv`

### Activate Environment
`.\.venv\Scripts\Activate`

### Install requirements
`pip install -r requirements.txt`

### Create database
Create AOI database in pgAdmin. <br>
Replace connection details in import_data_to_postgres.py and in second cell of SimpleRecom.ipynb.

### Run script
`python import_data_to_postgres.py`

### Run whole notebooks
Profiles.ipynb <br>
Preprocessing.ipynb <br>
ContentBasedRecom.ipynb


## Datasets
### Researchers Dataset
#### Faculty of Automatic Control and Computer Science, Polytechnic University of Bucharest Professors
Individually collected from:
[Brainmap](https://www.brainmap.ro/)
and
[Web of Science](https://www.webofscience.com/).<br>
Contains information about researchers in the field of computer science at our uni, including their researcher ids, names, expertise, and a list of previously appreciated articles ids.

### Computer Science Research Papers Dataset
[CS_arxiv_everyweek](https://github.com/MikeGu721/CS_arxiv_everyweek/tree/main) <br>
A dataset kept up to date and updated weekly that contains computer science articles with details such as ID, URL, title, authors, and subjects. <br>
Our dataset is last updated on 14th november 2023.


## Content-Based Filtering Recommendation System
### When to Use:
#### Effective with Detailed Content Information
Content-based filtering works well with datasets that contain rich details about research papers, such as keywords, authors, or abstracts.
#### Inferring User Preferences
It is preferred when the goal is to create recommendations based on users' preferences; for instance, if users 
consistently prefer papers with specific keywords or topics, with more interest in some subjects than in others, 
content-based filtering can effectively leverage this information to provide tailored recommendations.

### Interests Weighting
Researchers' expertise lists are processed into weighted interests.
The first interest in the list is assigned the highest weight of 0.9 and the following interests each receives a weight
of 20% less than the one before.

### Matching Algorithm
Each article is analyzed based on its subjects and the relevance is computed as a sum of the weighted interests of each researcher.

### Relevance Score Calculation
The relevance score is calculated by comparing article subjects with the researcher's weighted interests.
When a subject matches an interest, the corresponding weight is added to the relevance score.


## Hybrid Recommendation - Recommendation System Based on Collaborative and Content-Based
### When to Use:
#### Enhanced Recommendation Precision
Hybrid recommendation systems excel in scenarios where both user-item interactions (collaborative filtering) and 
detailed content information (content-based filtering) can be leveraged. 
By combining these approaches, the system can provide more precise recommendations compared to singular methods.

#### Addressing Data Sparsity and Cold Start Problems
Hybrid models offer solutions to common recommendation challenges, such as data sparsity and cold start issues. 
Collaborative filtering can handle sparse user-item matrices, while content-based filtering can address 
the cold start problem by providing recommendations based on item features.
