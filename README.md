# AOI
# Area Of Interest - Recommendation System

## Datasets

### Researchers Dataset
#### Faculty of Automatic Control and Computer Science, Polytechnic University of Bucharest Professors
Individually collected from:
https://www.brainmap.ro/
and
https://www.webofscience.com/
Contains information about researchers in the field of computer science at our uni, including their researcher ids, names, expertise, and appreciation.

### Computer Science Research Papers Dataset
https://github.com/MikeGu721/CS_arxiv_everyweek/tree/main
Contains computer science articles with details such as ID, URL, title, authors, and subjects.
The dataset is up to date to 14th november 2023.


## Recommendation System Based on Interests

### Interests Weighting
Researchers' expertise lists are processed into weighted interests.
The first interest in the list is assigned the highest weight of 0.9 and the following interests each receives a weight
of 20% less than the one before.

### Matching Algorithm
Each article is analyzed based on its subjects and the relevance is computed as a sum of the weighted interests of each researcher.

### Relevance Score Calculation
The relevance score is calculated by comparing article subjects with the researcher's weighted interests.
When a subject matches an interest, the corresponding weight is added to the relevance score.
