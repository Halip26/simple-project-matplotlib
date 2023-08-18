# Matplotlib Module

Matplotlib is powerful Python library used for visualizations and plots. It provides a range of functions and methods to create different types of graphs, charts, and plots.

To use the matplotlib module, you first need to import it using the following line of code:

```python
import matplotlib.pyplot as plt

```

Once imported, you can start creating your plots. Here's an example of creating a simple line graph using the plot() function:

```python
# x axis values
x = [1, 2, 3]
# corresponding y axis values
y = [2, 4, 1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
```

In the above example, we first define the x-axis values and the corresponding y-axis values. Then, we use the plot() function to plot the points on the graph. Next, we add labels to the x and y axes using the xlabel() and ylabel() functions. Finally, we give a title to our graph using the title() function and display the graph using the show() function.

Matplotlib offers a wide range of customization options, including changing the color, line style, marker style, gridlines, legends, and more. You can refer to the official Matplotlib documentation for more information on how to create different types of plots and customize them according to your needs.

For more information, please visit the [official Matplotlib documentation](https://matplotlib.org/stable/contents.html).

## For [matplolib3](matplotlib3.py)

  ```python
    import matplotlib.pyplot as plt
  ```

### the syntax & comments

```python
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
```

### With Explanation

Baris 1: Mengimpor modul matplotlib.pyplot dengan alias plt.

Baris 3-5: Membuat tiga list a, b, dan c yang berisi data poin untuk masing-masing plot.

Baris 7: Membuat objek figure dengan ukuran 10x10.

Baris 9-12: Membuat empat subplot pada grid 2x2. Subplot pertama akan berada di posisi (1, 1), subplot kedua di posisi (1, 2), subplot ketiga di posisi (2, 1), dan subplot keempat di posisi (2, 2).

Baris 14-15: Plotting subplot pertama dengan data poin dari list a menggunakan simbol kotak berwarna biru.

Baris 17-18: Menentukan posisi label sumbu x dan judul subplot pertama.

Baris 20-21: Plotting subplot kedua dengan data poin dari list b menggunakan simbol lingkaran berwarna merah.

Baris 23-24: Menentukan posisi label sumbu x dan judul subplot kedua.

Baris 26-27: Plotting subplot ketiga dengan data poin dari list yang dihasilkan dari fungsi list(range(0, 22, 3)) menggunakan simbol segitiga hijau.

Baris 29-30: Menentukan posisi label sumbu x dan judul subplot ketiga.

Baris 32-33: Plotting subplot keempat dengan data poin dari list c menggunakan simbol berlian berwarna magenta.

Baris 35-36: Menentukan posisi label sumbu y dan judul subplot keempat.

Baris 38: Menampilkan hasil dari semua subplot yang sudah dibuat.

Sehingga, kode di atas menciptakan subplot di dalam sebuah objek figure dengan grid 2x2, dengan setiap plot memiliki data poin dan argumen lain yang berbeda untuk jenis simbol dan label sumbu. Hasilnya adalah sebuah figure yang menampilkan keempat subplot tersebut.

## Displaying the red and white rectangle to express the 78th Indonesian Independence Day

```python
import matplotlib.pyplot as plt

import matplotlib.patches as patches

```

Displaying the red and white rectangle to express the 78th Indonesian Independence Day using Python programming language with the matplotlib module
Matplotlib is commonly used for data visualization.
Happy 78th Indonesian Independence Day! Strong and Growing Indonesia for 78 years!
Plotting the red and white rectangles of the national flag

```python
red = patches.Rectangle( (0, 3), width=6, height=2, facecolor="#FF0000", edgecolor="grey" ) 

white = patches.Rectangle( (0, 1), width=6, height=2, facecolor="#FFFFFF", edgecolor="grey" )

fig, ax = plt.subplots()

ax.add_patch(red) 
ax.add_patch(white)

plt.axis("equal") 
plt.show()
```
