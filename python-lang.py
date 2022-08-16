import os
os.chdir("python-lang")

# 1
s = "this is a string"
print(s[::-1])

# 2
with open("numbers-from-0-to-9.txt", "r") as f: numbers_in_string = f.read().split('\n')
numbers_in_int = list(map(int, numbers_in_string))
print(numbers_in_int)

# 3
import matplotlib.pyplot as plt
import pydicom
ds = pydicom.dcmread("example-dicom-image.dcm")
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()

# 4
# $ python -m http.server