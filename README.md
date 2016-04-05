This is the repo I prepared for the WWC recommender systems interactive session / hacknight.
Here you will find all the relevant resources, as well as the code that will be used.
The goal of the hacknight is to introduce people to recommender sytems, build your own recommender system and evaluate it
by generating recommendations for you and other attendees. 

This will be a relaxed and interactive environments, with people helping you to go through the examples. If you want, you can join a friend and code together.

### hacknight
* 6:00 - 6:30 networking and food
* 6:30 - 6:50 presentation (introduction to Recommender Systems)
* 6:50 - 8:20 hacking! :collision:
* 8:20 - 8:45 wrap up, questions, show and tell 

### Before the session: 
* You need python 3.x installed in your laptop. Click on the [Python website](https://www.python.org/downloads/) for more info
* Access to the internet will be provided (we need this to download the datasets)
* Read the presentation slides and the Collaborative filtering entry on wikipedia (on resources)
* Make sure you have ipython or [jupyter notebooks](http://jupyter.readthedocs.org/en/latest/install.html) installed 
* Find 20 movies you know and rate them (1-5 scale). The first exercise will be to store those ratings in our dataset. 
It is important to also rate movies you don't like, so the recommender can learn about your taste better.


### Getting ready to code: 
* Clone or download the repository 
* Install the required packages if you don't have them (pandas and scipy)
* run the test example (using ipython or jupyter notebooks). If it works you are ready to go! 
* If you want to take a look at the code, you can import the project to your favourite IDE (Pycharm is mine) 

```
if you are familiar with git
> git clone https://github.com/hcorona/WWC-recsys
> cd WWC-recsys/
> jupyter notebook notebooks/example_similarity.ipynb 
```

```
if you want to download the zipfile 
> Download https://github.com/hcorona/wwc-recsys/archive/master.zip
> unzip the file 
> go to where you unzipped the file 
> run jupyter notebook notebooks/example_similarity.ipynb 
```

### Examples of things you can do or questions that are interesting? 

* It looks like some of the recommendations are from items we just rated. However, you want people to discover new movies.
How do you make sure you never get recommendations for items you have rated? 

* Are scores important? Should we filter the recommendations to only show the ones we are really sure people will like? 

* What do we know about the dataset? Start an ipython notebook and plot some basic statistics, it will help you understand 
many things about. For example, how many ratings does each movie gets? What are the most popular movies? what is the rating distribution?

* See who are your neighbours, see what they have rated. This is a non-automated way to discover movies, and it also helps to 
understand how the U-KNN algorithm works. 

* Play with the parameters. For example, are your neighbours better when you use 'pearson correlation' or when you use 'cosine similarity'? 

* Make recommendations for one of your colleagues. Do they like them? Is their perception on quality the same as yours? 

* How long will it take for each algorithm to generate recommendations for all users? Is it scalable? Which one is better? 

* Are the recommendations good? Which algorithm makes better recommendations?

* Implement the matrix factorization algorithm. It works very well, and it is very similar to the ones used in real-world recommender systems!

### Resources
* Collective Intelligence book : [Programming Collective Intelligence book] (http://www.amazon.com/gp/product/0596529325/ref=as_li_qf_sp_asin_il?ie=UTF8&camp=1789&creative=9325&creativeASIN=0596529325&linkCode=as2&tag=tasktoy-20) 
* Collective Intelligence (book code): [Programming Collective Intelligence code](https://github.com/cataska/programming-collective-intelligence-code)
* [Collaborative Filtering on Wikipedia](https://en.wikipedia.org/wiki/Collaborative_filtering)
* An introduction to RS from Humberto's talk at #unit conference: [slides](unit2016-HumbertoCorona-RecommenderSystems.pdf)

### Additional resources 
* [Recommendations with Apache Spark](https://www.codementor.io/spark/tutorial/building-a-recommender-with-apache-spark-python-example-app-part1)
* [The Movielens dataset website](http://grouplens.org/datasets/movielens/)
* [ACM Recommender Systems Wiki](http://www.recsyswiki.com/wiki/)

