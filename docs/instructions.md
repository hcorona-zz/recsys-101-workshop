## Before the session: 

### Exporting your IMDb ratings 
1. Go to [IMDb](http://imdb.com) and make an account if you don't have one
2. If you have no ratings in your account, rate at least 10 movies you liked and 10 movies you didn't like.  ***(It is important to also rate movies you don't like, so the recommender can learn about your taste better)***
2. Go to your account (top right) and click on "your Ratings"
3. Go to the bottom of the page, next to the "next" button, you will find an "Export this list" button. It will export your ratings to your Downloads folder. 
4. Move the file inside your /data folder in this repo



### Installing and configuring Python

* You need python 3.x installed in your laptop. Click on the [Python website](https://www.python.org/downloads/) for more info based on the OS you work with.

* You Also need to install a few [python packages](https://pypi.python.org/pypi) such as Pandas, SciPy and Jupyter: 

```
if you use pip: 
> pip3 install pandas
> pip3 install scipy
> pip3 install jupyter
	
if you use anaconda
> conda install pandas
> conda install scipy
> conda install jupyter
```


### Getting ready to code
* You can either download the repository zip file, or clone the repository.
* Now that you have all the required packages, you should be ready to go!
* Finally, if you want to take a better look at the code, you can open the project into with IDE (like [Pycharm](https://www.jetbrains.com/pycharm/)) 

```
if you are familiar with git
> git clone https://github.com/hcorona/recsys-101-
> cd recsys-101-workshop/
> jupyter notebook notebooks/example.ipynb 
```

```
if you want to download the zipfile 
> Download https://github.com/hcorona/recsys-101-workshop/archive/master.zip
> unzip the file 
> go to where you unzipped the file 
> run jupyter notebook notebooks/example.ipynb 
```

### Running the example and rate your own movies:

Now that you have run the example, and downloaded the data, you can run the first notebook to make sure everything went OK.

* run the first notebook [notebook-1-data-gathering](https://github.com/hcorona/recsys-101-workshop/blob/master/notebooks/notebook-1-data-gathering.ipynb) using jupyter notebooks (***Note: You will need access to the internet to download the dataset.***)
