from jinja2 import Template
import csv
from matplotlib import pyplot as plt
import numpy as np
import pyhtml as h


#getting data

dicheads = ["Student id", "Course id", "Marks"]
datalist = []
file = open('data.csv', mode = 'r')
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


#rendering HTML CODE

def render_html(content):
    output_file = open('output.html', 'w')
    output_file.write(content)
    output_file.close()


#constructing default HTML CODE

def default_html():
    t = h.html(
        h.head(
            h.title('Something went wrong')),
        h.body(
            h.h1('Wrong Inputs'),
            h.p('Something went wrong'))
        )
    outputcontent = t.render()
    return str(outputcontent)

#constructing main HTML CODE

def main():
    p1 = input("Course or Student?")
    final = []
    Total_Marks = 0
    htmlcode = default_html()

    #Case 1 of choosing Student
    
    if p1 == '-s':
        studentid = int(input("Enter the student id: "))
        for each in datalist:
            if each["Student id"] == studentid:
                final.append(each)
                Total_Marks = Total_Marks + int(each["Marks"])
        if final: 
            file3 = open('studeets.html.jinja2', mode = 'r')
            t1 = file3.read()
            file3.close()
            obj1 = Template(t1)
            htmlcode = obj1.render(final = final, Total_Marks = Total_Marks)

    #Case 2 of choosing Course
            
    elif p1 == '-c':
        courseid = int(input("Enter the course id: "))
        for each in datalist:
            if each["Course id"] == courseid:
                final.append(each["Marks"])
                Total_Marks = Total_Marks + each["Marks"]
        if final: 
            Average_Marks = Total_Marks/len(final)
            Maximum_Marks = max(final)
            plt.hist(np.array(final))
            plt.xlabel("Marks")
            plt.ylabel("Frequency")
            plt.savefig('my_plot.png')
            plt.close()

            # reading the template
            file4 = open('cdeets.html.jinja2', mode = 'r')
            t2 = file4.read()
            file4.close()

            # constructing th HT=ML code
            obj2 = Template(t2)
            htmlcode = obj2.render(Average_Marks = Average_Marks, Maximum_Marks = Maximum_Marks)

    render_html(htmlcode)

if __name__ == "__main__":
    main()
    
    


