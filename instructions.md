## Before the session: 
* You need python 3.x installed in your laptop. Click on the [Python website](https://www.python.org/downloads/) for more info based on the OS you work with.

#### Additional instructions for Windows:
```
 
* Click on Windows button.
* Right-click on the Computer, click on Properties.
* Click on Advanced system settings.
* Click on the Environment Variables button.
* Under "Systems variables", scroll down to find Path, click on it to highlight it.
* Click on Edit button.
* Hit the right arrow key on your keyboard to make sure you are at the end of the text.
* Type the following ;c:\python34
* Click "OK" to close dialogs.
```

* You also need to install the following packages: [Pandas](http://pandas.pydata.org) and [SciPy](http://www.scipy.org).
* Make sure you have ipython or [jupyter notebooks](http://jupyter.readthedocs.org/en/latest/install.html) installed.
* To install these packages you tipically use pip or anaconda: 
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

#### Alternative Windows installation

You can also download WinPython, a distribution of Python packages that contains all you need for running Python on Windows:
https://winpython.github.io/

### First thing to Do: 

* Find around 20 movies you know and rate them (1-5 scale). The first exercise will be to store those ratings in our dataset. It is important to also rate movies you don't like, so the recommender can learn about your taste better. For example, some of the movies I know:

```
The Endless Summer(1966)	5
After the Wedding (2006)	4
No (2012)	4
Submarine (2010)	4
Win Win (2011)	3
Born on the Fourth of July (1989)	2
Bowling for Columbine	(2002)	5
Amour (2012)	5
Love Actually (2003)	3
Juno (2007)	4
Zero Dark Thirty	(2012)	4
Up in the Air	 (2009)	4		
Moonrise Kingdom	(2012)	5
8 Mile	(2002)	2
Blue Jasmine	(2013)	3
The Way Way Back	(2013)	4	
Perfect Mothers	(2013)	5

```

* You can use this document to save your recommendations:
https://docs.google.com/document/d/1qKH1ZABGMegJDET0lCqXTmaMc9RoBY58Vd0oJLTDv_8/edit?usp=sharing

* Read the presentation slides and the Collaborative filtering entry on wikipedia (on [resources](### Resources))


### Getting ready to code: 
* You can either download the repository zip file, or clone the repository.
* Now that you have all the required packages, you should be ready to go!
* run the example [example.ipynb](/notebooks/example.ipynb) using ipython or jupyter notebooks on your laptop.
* If you want to take a better look at the code, you can import the project to your favourite IDE (Pycharm is mine) 
* You will need access to the internet to download the dataset.

```
if you are familiar with git
> git clone https://github.com/hcorona/wwc-recsys
> cd wwc-recsys/
> jupyter notebook notebooks/example.ipynb 
```

```
if you want to download the zipfile 
> Download https://github.com/hcorona/wwc-recsys/archive/master.zip
> unzip the file 
> go to where you unzipped the file 
> run jupyter notebook notebooks/example.ipynb 
```

### Running the example and rate your own movies:

Now that you have run the example, and downloaded the data, you can find the movies in the downloaded dataset and find the following files: 

* the ratings I created: under [/data/](/data/ratings_humberto.csv)
* the file with all movie Ids in [/data/ml-latest-small](/data/ml-latest-small/README.txt)

Find the movies you like in the movies file, and write them in the ratings_yourname.csv
