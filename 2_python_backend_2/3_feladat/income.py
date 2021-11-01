import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from flask import Flask
from flask import send_file


def read_first_line(document):
  with open(document, "r") as file:
    first_line = file.readline()
    first_line = first_line.strip()
    first_line = first_line.split(",")

  return first_line


def read_from_sec_line(document):
  data = []
  with open("income.txt", "r") as file:
    lines = file.readlines()[1:]
    for line in lines:
      line = line.strip().split(",")
      #line = line.split(",")
      line_to_data = []
      for item in line:
        line_to_data.append(int(item.replace(" ", "")))
      data.append(line_to_data)

  return data


app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
  first_line = read_first_line("income.txt")
  data_source = read_from_sec_line("income.txt")

  df = pd.DataFrame(data_source)
  df.columns = [first_line[0], first_line[1], first_line[2], first_line[3]]
  sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
  sns_plot.figure.savefig("output.png")
  plt.close()
  return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
  app.run(debug=True)
