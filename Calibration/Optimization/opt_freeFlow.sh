#!/bin/bash

p3 optimize_free_flow.py 20 1.5
p3 plot_errors.py
rm data/error.csv

p3 optimize_free_flow.py 20 2.0
p3 plot_errors.py
rm data/error.csv

p3 optimize_free_flow.py 20 2.5
p3 plot_errors.py
rm data/error.csv

p3 optimize_free_flow.py 20 3
p3 plot_errors.py
rm data/error.csv

p3 optimize_free_flow.py 7.5 1
p3 plot_errors.py
rm data/error.csv


p3 optimize_free_flow.py 15 1
p3 plot_errors.py
rm data/error.csv


p3 optimize_free_flow.py 22.5 1
p3 plot_errors.py
rm data/error.csv


p3 optimize_free_flow.py 30 1
p3 plot_errors.py
rm data/error.csv
