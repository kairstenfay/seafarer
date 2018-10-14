# Seafarer package
### An additional layer of abstraction for `seaborn` and `matplotlib`.

## How to navigate this repo:
The real logic for the structure of this program (i.e. the source code) lies in 
`seafarer/seafarer`. See the Jupyter Notebook `code-tester.ipynb` for examples
of how the client would run the code. `plots.py` can be ignored -- it only 
served as an initial inspiration for seeking redundancies in the themes of plots
I wanted to instantiate. 

## TODOs:
* Upload to the [PyPI](https://packaging.python.org/tutorials/packaging-projects/) 
* Add fontsize arguments or defaults  
* Add xlim/ylim functions
* implement seaborn color palettes, maybe colorbrewer, too 
  
## Known issues:  
* Prints many empty plots before printing the plot with data.
* The kwargs hack for an optional y axis is not robust to mistyped parameters