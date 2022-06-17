from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.pin import *
import csv
import pandas as pd
import datetime

config(title="Karkasi", description="和朋友一起记账！",theme="sketchy")
def main():  # PyWebIO application function
    img=open("./logo.jpg", 'rb').read()
    put_image(img, width='150px')
    put_image(img, width='150px')
    put_image(img, width='150px')
    
    user = ["qiu","chen"]
    name = input("what's your name")

    if name in user:
        #put_image("./logo.jpg")
        put_markdown('# 和朋友一起来记账！'),
        put_text("hello", name),
        put_markdown('---'),
        put_column([put_buttons(['新增','修改','删除','更新'],onclick=[lambda: _new(),lambda: _edit(),lambda: _delete(),lambda: _update()])])
        _update()
        

    else:
        put_text("输出错误 or 没有使用权限：", name)
 
#新增记录
def _new():
    popup('新增记录', [
        put_input( name='date',label='日期',type=DATE),
        put_input(name='item',label='项目', type=TEXT),
        put_input( name='price',label='金额',type=FLOAT),
        put_select(name='currency', label='币种',value='JPY',options=['JPY', 'CNY']),
        put_input(name='web',label='网址', type=TEXT),
        put_select(name='status', label='状态',value='申请中',options=['申请中', '已通过', '已结清']),
        put_buttons(['确定','关闭'], onclick=[lambda : _save(pin.date,pin.item,pin.price,pin.currency,pin.web,pin.status,datetime.datetime.today()),lambda : close_popup()])
])

#修改记录
def _edit():
    put_text("修改功能未加入")

#删除记录
def _delete():
    put_text("删除功能未加入")

#显示
def _update():
    df = pd.read_csv('Ledger.csv')
    #print(df.to_string())
    with use_scope('scope2', clear=True):
        put_html(df.to_html(border=0))
    print("update ok")

#写入csv
def _save(date,item,price,currency,web,status,time):
    data=[date,item,price,currency,web,status,time]
#    for _ in data:
#        print(_)
    with open('Ledger.csv', 'a', newline='',encoding="utf-8") as f:
        cw = csv.writer(f)
        cw.writerows([data])
    close_popup()
    _update()


def test():
    print(1)

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
