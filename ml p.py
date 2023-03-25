<html>
<head>
    <title>Hospital Registration</title>
</head>
<body>
    <form action="/submit" method="post">
        <p>请选择病症（多选请用逗号分隔）：</p>
        <input type="text" name="diseases"><br>
        <p>请添加备注：</p>
        <input type="text" name="remarks"><br><br>
        <input type="submit" value="提交">
    </form>
</body>
</html>


from flask import Flask, request
import socket

app = Flask(__name__)

# 定义可选病症列表和对应的回答列表
diseases = ['Cold', 'fever', 'cough', 'headache', 'abdominal pain']
answers = ["Please keep warm, drink plenty of water, and rest well.",
           "Please measure your body temperature and seek medical attention in a timely manner.",
           "Please pay attention to cough hygiene. If you have symptoms such as excessive phlegm and severe cough, please seek medical attention in a timely manner.", "Please avoid overusing your brain and take appropriate rest.", "Please pay attention to food hygiene, take appropriate rest, and seek medical attention in a timely manner if you have symptoms such as bloody stools or vomiting."]

@app.route('/')
def index():
    return '''<html>
<head>
    <title>医院挂号</title>
</head>
<body>
    <form action="/submit" method="post">
        <p>请选择病症（多选请用逗号分隔）：</p>
        <input type="text" name="diseases"><br>
        <p>请添加备注：</p>
        <input type="text" name="remarks"><br><br>
        <input type="submit" value="提交">
    </form>
</body>
</html>'''

@app.route('/submit', methods=['POST'])
def submit():
    selected_diseases = request.form['diseases'].split(',')
    remarks = request.form['remarks']

    # 根据病人选择的病症输出对应的回答
    responses = []
    for selected_disease in selected_diseases:
        if selected_disease in diseases:
            index = diseases.index(selected_disease)
            response = '您选择的病症是 {}，‘Doctor's recommendation’： {}'.format(selected_disease, answers[index])
            responses.append(response)
        else:
            response = '
import numpy as np
import matplotlib.pyplot as plt

# 读入医学图像
im = plt.imread('medical_image.png')

# 显示医学图像
plt.imshow(im, cmap='gray')
plt.title('Medical Image')
plt.show()

# 阈值分割
im_threshold = im > 127

# 显示阈值分割后的医学图像
plt.imshow(im_threshold, cmap='gray')
plt.title('Medical Image Segmentation')
plt.show()

# 计算医学图像的一些特征参数，如平均像素值和像素数量等
avg_pixel_value = np.mean(im)
num_pixels = np.sum(im_threshold)

# 输出特征参数
print('Average Pixel Value:', avg_pixel_value)
print('Number of Pixels:', num_pixels)
