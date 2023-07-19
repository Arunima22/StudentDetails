from jinja2 import Template
import csv
import os
import matplotlib 
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
import numpy as np
from flask import Flask
from flask import render_template
from flask import request



#getting data
dicheads = ["Student id", "Course id", "Marks"]
datalist = []
file = open('static/data.csv', mode = 'r')
content = file.read().split("\n")
line_count = 0
for each in content:
    if line_count == 0:
        line_count += 1
    else:
        l = each.split(",")
        dic = {}
        n = 0
        for word in l:
            dic[dicheads[n]] = int(word)
            n = n + 1
        datalist.append(dic)
file.close()



#building an app
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def main():
    if request.method == "GET":
        return render_template('main.html')
    if request.method == "POST":
        c1 = request.form["ID"]
        c2 = request.form["id_value"]
        

        #if user selects student id
        if c1 == "student_id":
            final = []
            Total_Marks = 0
            for each in datalist:
                if each["Student id"] == int(c2):
                    final.append(each)
                    Total_Marks = Total_Marks + int(each["Marks"])
            if final: 
                return render_template('student_details.html', final = final, Total_Marks = Total_Marks)
            else:
                return render_template('default.html')

        #if user selects course id
        elif c1 == "course_id":
            final = []
            Total_Marks = 0
            for each in datalist:
                if each["Course id"] == int(c2):
                    final.append(each["Marks"])
                    Total_Marks = Total_Marks + each["Marks"]
            if final: 
                Average_Marks = Total_Marks/len(final)
                Maximum_Marks = max(final)

                static_folder = 'static'
                save_path = os.path.join(static_folder,'my_plot.png')

                plt.hist(np.array(final))
                plt.xlabel("Marks")
                plt.ylabel("Frequency")
                plt.savefig(save_path)
                plt.close()

                return render_template('course_details.html', Average_Marks = Average_Marks, Maximum_Marks = Maximum_Marks)
            else:
                return render_template('default.html')

        #if something goes wrong
        else:
            return render_template('default.html')

if __name__ == "__main__":
    main()




    



    
    


