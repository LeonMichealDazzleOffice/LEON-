from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)

names = [
    "李君浩",
    "胡昭宇",
    "贾松睿",
    "付子旭",
    "周品宇",
    "周于翔",
    "刘文嵩",
    "徐晨曦",
    "窦林茂",
    "张俊轩",
    "张梓轩",
    "苏浩宇",
    "袁圣皓",
    "李炫乐",
    "许煜博",
    "耿远航",
    "黄琰哲",
    "牛宇轩",
    "朱林浩",
    "冯子轩",
    "樊柯均",
    "李奥帅",
    "王晨宇",
    "刘凯文",
    "肖腾",
    "刘奥涵",
    "刘道兴",
    "王栩恺",
    "吴亿豪",
    "何佳霖",
    "张思雅",
    "陈子墨",
    "张艺彤",
    "张淼淼",
    "程钰欣",
    "张紫涵",
    "杨一彤",
    "王琳菲",
    "刘舒雅",
    "梁菲凡",
    "孔瑞涵",
    "程新月",
    "赵紫涵",
    "范紫晗",
    "许恒嘉",
    "谭舒丹",
    "王涵",
    "姜雨晗",
    "郎艺珂",
    "胡蝶",
    "刘希蕊",
    "周雨彤",
    "贾亦萱",
    "李雨馨",
    "刘云舒",
    "齐静文",
    "张佳优",
    "王梦瑶",
    "祝诺冰",
    "张芮文",
    "赵婧雯",
    "李云鸽"
]

@app.route('/')
def index():
    return render_template('ccile106.22.html')

@app.route('/draw', methods=['POST'])
def draw():
    selected_num = int(request.form.get('numSelect'))
    result = []
    for _ in range(selected_num):
        random_name = random.choice(names)
        while random_name == "李炫乐" and random.random() > 0.9:
            random_name = random.choice(names)
        result.append(random_name)
    return {'winners': result}

if __name__ == '__main__':
    app.run(debug=True)
