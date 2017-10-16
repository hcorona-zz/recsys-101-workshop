## Before the session: 

### Exporting your IMDb ratings 
1. Go to [IMDb](http://imdb.com) and make an account if you don't have one
2. If you have no ratings in your account, rate at least 10 movies you liked and 10 movies you didn't like.  ***(It is important to also rate movies you don't like, so the recommender can learn about your taste better)***
2. Go to your account (top right) and click on "your Ratings"
3. Go to the bottom of the page, next to the "next" button, you will find an "Export this list" button. It will export your ratings to your Downloads folder. 
4. Move the file inside your /data folder in this repo

### Installing and configuring Python

* You need python 3.x installed in your laptop. Click on the [Python website](https://www.python.org/downloads/) for more info based on the OS you work with. (if you have Windows, check out the additional instructions at the end of the document)

#### Alternative Windows installation

You can also download WinPython, a distribution of Python packages that contains all you need for running Python on Windows:
https://winpython.github.io/

Once you have Python installed, make sure you follow this instructions: 

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

### Downloading the code 
* You can either download the repository zip file, or clone the repository.
* Now that you have all the required packages, you should be ready to go!
* Finally, if you want to take a better look at the code, you can open the project into with IDE (like [Pycharm](https://www.jetbrains.com/pycharm/)) 

```
if you are familiar with git
> git clone https://github.com/hcorona/recsys-101-workshop
> cd recsys-101-workshop/
> jupyter notebook --ip="*" notebooks/notebook-0-data-gathering.ipynb
```

```
if you want to download the zipfile 
> Download https://github.com/hcorona/recsys-101-workshop/archive/master.zip
> unzip the file 
> go to where you unzipped the file 
> run jupyter notebook notebooks/notebook-0-data-gathering.ipynb
```

### Installing the packages 

* You Also need to install a few [python packages](https://pypi.python.org/pypi) such as Pandas, SciPy and Jupyter: 

```
if you use pip: 
> pip3 install -r requirements.txt
	
if you use anaconda
> conda install pandas=1.0.0
> conda install scipy=0.20.3
> conda install jupyter=0.19.1
> conda install matplotlib=2.1.0
```

### Running the example and rate your own movies:
Now that you have run the example, and downloaded the data, you can run the first notebook to make sure everything went OK.

1. run the first notebook [notebook-1-data-gathering](https://github.com/hcorona/recsys-101-workshop/blob/master/notebooks/notebook-0-data-gathering.ipynb) using jupyter notebooks (***Note: You will need access to the internet to download the dataset.***)
2. run the recommendations notebook  [notebook-4-recommendations](https://github.com/hcorona/recsys-101-workshop/blob/master/notebooks/notebook-4-recommendations.ipynb) to make sure everything runs (be patient, this might take a while) 
3. You are all set to start coding!

