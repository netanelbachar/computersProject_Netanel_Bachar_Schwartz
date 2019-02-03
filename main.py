# #### This code was written by Netanel Bachar Schwartz

# Welcome to Linear Fit.
# This program will open a text file with variables (x,y) and their corresponding numbers to create
# a linear plot graph with its corresponding uncertainties (dx,dy). Using the Chi Squared test, the most adequate
# plot will be drawn.
# ###
# This code is divided into 6 Parts:
#   Part 1 - Opening the text and deciding if it is a row or column parameters in the text file.
#            The functions here will check if all the data rows / columns have the same length
#            and that all the uncertainties are bigger than zero (dy​i​, dx​i​>0).
#   Part 2 - If the text file is a column design file it will create a dictionary of the
#            four variables (x,y,dx,dy) and their corresponding numbers.
#   Part 3 - If the text file is a row design file it will create a dictionary of the
#            four variables (x,y,dx,dy) and their corresponding numbers.
#   Part 4 - Chi Squared calculations and finding a,da,b,db parameters corresponding to the linear
#             formula y = a*x + b
#   Part 5 - Plot the results from part 4 on a graph. For this, the matplotlib.PyPlot package will
#            be used.
#   Part 6 - The main code calling all functions from parts 1-5.


# ###################### PART - Open and Uncertainties #######################

def opening_a_txt (text_file):
    sample_file = open(text_file, 'r')
    read_first_line = sample_file.readline()
    inside_txt_file = sample_file.read()
    sample_file.close()
    return inside_txt_file, read_first_line

def string_to_list (str_to_list):
    list_from_str = str_to_list.split()
    return list_from_str

def column_or_row (list_from_str):
    test_list = ["x", "y", "dx", "dy", "X", "Y", "DX", "DY", "dX", "dY", "Dx", "Dy"]
    # for variables in list_from_str:
    if list_from_str[1] in test_list:
        return 1
        # This corresponds for a column text
    else:
        return 0
        # This corresponds for a row text

# This function will will check if all the data rows / columns have the same length
def same_length_variables(var1f, var2f, var3f, var4f):
    if len(var1f) == len(var2f) and len(var3f) == len(var4f) and len(var3f) == len(var4f):
        return 1
    else:
        raise Exception("Input file error: Data lists are not the same length.")

# The functions here will check that all the uncertainties are bigger than zero (dy​i​, dx​i​>0).
def positive_uncert(dictionary_of_variables):
    for number in dictionary_of_variables["dx"]:
        if number < 0:
            raise Exception("Input file error: Not all uncertainties are positive.")
    for number in dictionary_of_variables["dy"]:
        if number < 0:
            raise Exception("Input file error: Not all uncertainties are positive.")

# ###################### PART 2 - Column #######################

def opening_a_txt_col(name_of_txt):
    sample_file = open(name_of_txt, 'r')
    read_first_line = sample_file.readline()
    inside_txt_file = sample_file.read()
    sample_file.close()
    return inside_txt_file, read_first_line

def lower_case_col(read_first_line):
    lc_first_line = read_first_line.lower()
    return lc_first_line

def string_to_list_col(str_to_list):
    list_from_str = str_to_list.split()
    return list_from_str

def make_list_col(text):
    lines = text.split("\n")
    lines_without_spaces = []
    for i in lines:
        if i != "":
             lines_without_spaces.append(i)
    var1 = []
    var2 = []
    var3 = []
    var4 = []
    y_axis_label = lines_without_spaces[-1]   # from here the y axis label will be extracted
    x_axis_label = lines_without_spaces[-2]   # from here the x axis label will be extracted

    for i in range(0, len(lines_without_spaces) - 2):
        line = lines_without_spaces[i]
        list_each_line = (line.split())
        if len(list_each_line) == 4:
            var1.append(float(list_each_line[0]))
            var2.append(float(list_each_line[1]))
            var3.append(float(list_each_line[2]))
            var4.append(float(list_each_line[3]))
            # All the numbers will now correspond to their variables in a form of a list.
        else:
            raise Exception("Input file error: Data lists are not the same length.")
    return var1, var2, var3, var4, y_axis_label, x_axis_label

# This function creates a dictionary with a variable (x,y,dx,dy) with their corresponding
# numbers inside a list.
def dictionary_of_variables_col(lc_first_line, var1, var2, var3, var4):
    list_first_line = lc_first_line.split()
    dicti_var = {list_first_line[0]: var1, list_first_line[1]: var2, list_first_line[2]: var3,
                 list_first_line[3]: var4}
    return dicti_var

# ###################### PART 3 - Row #######################

def opening_a_txt_row(name_of_txt):
    sample_file = open(name_of_txt, 'r')
    inside_txt_file = sample_file.read()
    sample_file.close()
    return inside_txt_file

def make_list_row(text_file):
    lines = text_file.split("\n")
    lines_without_spaces = []
    for i in lines:
        if i != "":
            lines_without_spaces.append(i)
    var2d = []
    y_axis_label = lines_without_spaces[-1]     # from here the y axis label will be extracted
    x_axis_label = lines_without_spaces[-2]     # from here the x axis label will be extracted

    for i in range(0, len(lines_without_spaces) - 2):
        line = lines_without_spaces[i]
        list_each_line = (line.split())
        var2d.append(list_each_line)
    var1 = var2d[0]
    var2 = var2d[1]
    var3 = var2d[2]
    var4 = var2d[3]
    var10 = var1.pop(0).lower()   # Pop the x,y,dx,dy and setting them into another variable.
    var20 = var2.pop(0).lower()
    var30 = var3.pop(0).lower()
    var40 = var4.pop(0).lower()
    return var1, var2, var3, var4, var10, var20, var30, var40, y_axis_label, x_axis_label


# This function will convert the string numbers into floats.
def var_from_str_float_row(var1, var2, var3, var4):
    var1f = []
    var2f = []
    var3f = []
    var4f = []
    for num1 in var1:
        var1f.append(float(num1))
    for num2 in var2:
        var2f.append(float(num2))
    for num3 in var3:
        var3f.append(float(num3))
    for num4 in var4:
        var4f.append(float(num4))
    return var1f, var2f, var3f, var4f

# This function creates a dictionary with a variable (x,y,dx,dy) with their corresponding
# numbers inside a list.
def dictionary_of_variables_row(var1f, var10, var2f, var20, var3f,var30, var4f, var40):
    dicti_var = {var10: var1f, var20: var2f, var30: var3f, var40: var4f}
    return dicti_var


# ###################### PART 4 - Chi Squared #######################

import math

def hat(z,dy):
    sum_hat = 0
    sum_dy = 0
    for i in range(0, len(z)):
        sum_hat = (z[i]/dy[i]**2) + sum_hat
        sum_dy = (1/dy[i]**2) + sum_dy

    return (sum_hat/sum_dy)

def squared_var(var):
    var_squared = []
    for squared in var:
        var_squared.append(squared**2)

    return var_squared

def var_times_var(var1,var2):
    var1_time_var2 = []
    for i in range(0, len(var1)):
        var1_time_var2.append(var1[i]*var2[i])

    return (var1_time_var2)

def chi_calc(x,y,a,b,dy):
    count = 0
    for i in range(0, len(x)):
        count = (((y[i]) - (a * x[i] + b)) / dy[i])**2 + count

    return (count)

def chi_calc_red(chi,N):
    chi_red = chi / (N - 2)

    return chi_red

# This function will return all parameters for a linear fit including their values and the
# values of the Chi Squared and the Chi Squared reduced test.
def calc_parameters(dicti):
    x_hat = hat(dicti["x"], dicti["dy"])
    y_hat = hat(dicti["y"], dicti["dy"])
    x_squared = hat(squared_var(dicti["x"]), dicti["dy"])
    xy_hat = hat(var_times_var(dicti["x"], dicti["y"]), dicti["dy"])
    dy_squared = hat(squared_var(dicti["dy"]), dicti["dy"])
    N_len = len(dicti["x"])

    a = (xy_hat - x_hat * y_hat) / (x_squared - x_hat ** 2)
    b = y_hat - a * x_hat
    da = math.sqrt(dy_squared / (N_len * (x_squared - x_hat ** 2)))
    db = math.sqrt((dy_squared * x_squared) / (N_len * (x_squared - x_hat ** 2)))

    chi_squared = chi_calc(dicti["x"], dicti["y"], a, b, dicti["dy"])
    chi_red = chi_calc_red(chi_squared, N_len)

    return a, da, b, db, chi_squared, chi_red

# ###################### PART 5 - Plot #######################

import matplotlib.pyplot as plt

def make_linear_min_chi2_plot(data, a, b, x_axis, y_axis):
    y_list = []
    for x_var in data ["x"]:
        y_function = a * x_var + b
        y_list.append(y_function)
    plt.plot(data['x'], y_list, 'r')
    plt.errorbar(data['x'], data['y'], xerr=data['dx'], yerr=data['dy'], fmt='b,')
    plt.title("Linear Plot Min Chi^2 ")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.savefig("linear_fit.svg".format())
    #plt.show()                                                   # If you run the program without the "#" you can see the plot.
# ###################### PART 6 - main code #######################

def fit_linear (input):
    inside_txt_file, read_first_line = opening_a_txt(input)
    list_from_str = string_to_list(read_first_line)
    try:
        if column_or_row(list_from_str) == 1:    # 1 means that it is a column text
            inside_txt_file, read_first_line = opening_a_txt_col(input)
            lc_first_line = lower_case_col(read_first_line)
            list_from_str = string_to_list_col(lc_first_line)
            list_txt = inside_txt_file.split()
            var1, var2, var3, var4, y_axis_label, x_axis_label = make_list_col(inside_txt_file)
            same_length_variables(var1, var2, var3, var4)
            dicti_var = dictionary_of_variables_col(lc_first_line, var1, var2, var3, var4)
            positive_uncert(dicti_var)
            a, da, b, db, chi_squared, chi_red = calc_parameters(dicti_var)
            print("a =", a, "+-", da)
            print("b =", b, "+-", db)
            print("chi2 =", chi_squared)
            print("chi2_reduced =", chi_red)
            make_linear_min_chi2_plot(dicti_var, a, b, x_axis_label, y_axis_label)

        else:
            inside_txt_file = opening_a_txt_row(input)
            var1, var2, var3, var4, var10, var20, var30, var40, y_axis_label, x_axis_label = make_list_row(inside_txt_file)
            var1f, var2f, var3f, var4f = var_from_str_float_row(var1, var2, var3, var4)
            same_length_variables(var1f, var2f, var3f, var4f)
            dicti_var = dictionary_of_variables_row(var1f, var10, var2f, var20, var3f, var30, var4f, var40)
            positive_uncert(dicti_var)
            a, da, b, db, chi_squared, chi_red = calc_parameters(dicti_var)
            print("a =", a, "+-", da)
            print("b =", b, "+-", db)
            print("chi2 =", chi_squared)
            print("chi2_reduced =", chi_red)
            make_linear_min_chi2_plot(dicti_var, a, b, x_axis_label, y_axis_label)

    except Exception as ex:
        print(ex)


# fit_linear("input.txt")     #Input text file in this function
