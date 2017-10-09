No, we’re not reading your mind!

Ever notice how so much of your online experience is curated to you - recommended outfits on Zalando, suggested songs or books. In this interactive workshop, we will introduce and practice the most important concepts about recommender systems, the force behind the personalized experience.

By the end of the workshop, you will be able to build and evaluate your own recommender system and discuss the outcomes with the help of our mentors, all in a very informal and interactive way. If you’ve got basic Python knowledge, you’re a great fit for this workshop. Bring along a friend and code together!

### Hack/wokrshop suggested times 
* 30 mins: presentation (introduction to Recommender Systems)  
* 1h 30 mins: hacking! :collision: 
* 30 mins:  wrap up, questions, show and tell 


### Before the session: 
Before the session, please read and follow all the steps detailed in the [instructions file](docs/instructions.md). If you have problems following it, you can ask questions in the meetup event forum, or using github issues. 


### Examples of things you can do or questions that are interesting? 

1. Make sure you have everything ready, including taking a closer look at the code and the data. You can work in pairs if you like to.

2. What do we know about the data? Start a jupyter notebook and plot some basic statistics, it will help you understand  many things about the problem. For example, how many ratings does each movie gets? What are the most popular movies? What is the rating distribution?

3. Play with the parameters. For example, are your neighbours better when you use 'pearson correlation' or when you use 'cosine similarity'? Discuss your findings with your neighbours.

3. Make recommendations for one of your colleagues (by getting their list of rated items). Do they like them? Is their perception on quality the same as yours? 

4. Are scores important? Should we filter the recommendations to only show the ones we are really sure people will like? 

5. It looks like some of the recommendations are from items we just rated. However, you want people to discover new movies. How do you make sure you never get recommendations for movies you have already rated?

6. See who are your "neighbours", see what they have rated. This is a non-automated way to discover movies, and it also helps to understand how the *U-KNN* algorithm works. 

7. Are the recommendations good? Which algorithm makes better recommendations?  Everyone has different opinions, try different combinations of algorithms and parameters and discuss your findings with other people.  

* Extra: Implement the matrix factorization algorithm. It works very well, and it is very similar to the ones used in real-world recommender systems! [Simon Funk's SVD](http://sifter.org/~simon/journal/20061211.html)

## Resources
* Collective Intelligence book : [Programming Collective Intelligence book](http://www.amazon.com/gp/product/0596529325/ref=as_li_qf_sp_asin_il?ie=UTF8&camp=1789&creative=9325&creativeASIN=0596529325&linkCode=as2&tag=tasktoy-20) 
* Collective Intelligence (book code): [Programming Collective Intelligence code](https://github.com/arthur-e/Programming-Collective-Intelligence)
* [Collaborative Filtering on Wikipedia](https://en.wikipedia.org/wiki/Collaborative_filtering)
* An introduction to RS by Humberto: [slides](https://github.com/hcorona/recsys-101-workshop/blob/master/docs/toa-2017.pdf)

## Additional resources 
* [Recommendations with Apache Spark](https://www.codementor.io/spark/tutorial/building-a-recommender-with-apache-spark-python-example-app-part1)
* [The Movielens dataset website](http://grouplens.org/datasets/movielens/)
* [ACM Recommender Systems Wiki](http://www.recsyswiki.com/wiki/)
