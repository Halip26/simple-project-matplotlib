import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]  # Creating a list of data points for the 1st plot
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]  # Creating a list of data points for the 2nd plot
c = [4, 2, 6, 8, 3, 20, 13, 15]  # Creating a list of data points for the 3rd plot

fig = plt.figure(figsize=(10, 10))  # Creating a figure object with a specified size

sub1 = plt.subplot(2, 2, 1)  # Creating the 1st subplot
sub2 = plt.subplot(2, 2, 2)  # Creating the 2nd subplot
sub3 = plt.subplot(2, 2, 3)  # Creating the 3rd subplot
sub4 = plt.subplot(2, 2, 4)  # Creating the 4th subplot

sub1.plot(a, "sb")  # Plotting the 1st plot with blue squares

sub1.set_xticks(list(range(0, 10, 1)))  # Setting the x-axis ticks for the 1st plot
sub1.set_title("1st Rep")  # Setting the title for the 1st plot

sub2.plot(b, "or")  # Plotting the 2nd plot with red circles

sub2.set_xticks(list(range(0, 10, 2)))  # Setting the x-axis ticks for the 2nd plot
sub2.set_title("2nd Rep")  # Setting the title for the 2nd plot

sub3.plot(list(range(0, 22, 3)), "vg")  # Plotting the 3rd plot with green triangles
sub3.set_xticks(list(range(0, 10, 1)))  # Setting the x-axis ticks for the 3rd plot
sub3.set_title("3rd Rep")  # Setting the title for the 3rd plot

sub4.plot(c, "Dm")  # Plotting the 4th plot with magenta diamonds

sub4.set_yticks(list(range(0, 24, 2)))  # Setting the y-axis ticks for the 4th plot
sub4.set_title("4th Rep")  # Setting the title for the 4th plot

plt.show()  # Displaying the figure with all the subplots
