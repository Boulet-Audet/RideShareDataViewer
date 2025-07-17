This Repo is Maxime's Udacity project to filter ride share csv data files.
It will allow reading CSV files from ridesharing and loading them into a Panda dataframe.
It displays filtered values to the user using a terminal interface and plots histograms using matplotlib.

Bikeshare Data Viewer
Overview
A Python application to explore US bikeshare data from CSV files.
It provides interactive filtering and visual/statistical analysis of trip data.

Features
    Lists available CSV files in the current directory
    Filters data by city, month, and day of week
    Displays statistics on travel times, stations, trip durations, and user demographics
    Generates histograms and bar charts using matplotlib
Requirements
    Python 3.x
    pandas
    numpy
    matplotlib
Installation
    Clone or download this repository.
    Place your bikeshare CSV files in the project directory.
    Install dependencies:
    Usage
    Run the program in your terminal:

Follow the prompts to select a CSV file and filter options.

File Structure
bikeshare.py: Main application script
CSV files: Bikeshare data files (must be in the same directory)
Notes
The program expects CSV files with columns like Start Time, End Station, Trip Duration, User Type, Gender, and Birth Year.
Interactive input is required; run in a terminal that supports input.
License
MIT License

Copyright (c) 2025 Maxime Boulet-Audet

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
