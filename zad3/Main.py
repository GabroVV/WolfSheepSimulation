from pandas import DataFrame
import pandas as pd


paramnames=['Sex', 'Length', 'Diameter', 'Height', 'Wholeweight', 'Shuckedweight'
        , 'Visceraweight','Shellweight', 'Rings']

def loadFromCSV(filename):
    return pd.read_csv(filename,names=paramnames, delimiter=',')

if __name__ == "__main__":
    print("Hello World")
    data = loadFromCSV('abalone.data')
    pd.set_option('display.max_columns', 5000)
    #print(data.values)
    #print(data.columns)
    #print(data.index)

    lengthMedian = data.Length.median(axis=0)
    diameter_median = data.Diameter.median(axis=0)
    height_median = data.Height.median(axis=0)
    whole_height_median = data.Wholeweight.median(axis=0)
    shucked_weight_Median = data.Shuckedweight.median(axis=0)
    viscera_weight_Median = data.Visceraweight.median(axis=0)
    shell_weight_median = data.Shellweight.median(axis=0)
    rings_median = data.Rings.median(axis=0)
    print(lengthMedian)
    print(diameter_median)
    print(height_median)
    print(whole_height_median)
    print(shucked_weight_Median)
    print(viscera_weight_Median)
    print(shell_weight_median)
    print(rings_median)



