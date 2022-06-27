#from contextlib import nullcontext
from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.pin import *
import csv
import pandas as pd
from datetime import datetime
name=''
config(title="Karkasi", description="和朋友一起记账！",theme="sketchy")
def main():  # PyWebIO application function
    global name
    img=open("./images/head.jpg", 'rb').read()
    [put_image(img, width='150px') for _ in range(3)]

    
    user = ["qiu","chen"]
    name = input("what's your name")

    if name in user:

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
        put_input( name='date',label='日期', type=DATE),
        put_input(name='item',label='项目', type=TEXT),
        put_input( name='price',label='金额',type=FLOAT),
        put_select(name='currency', label='币种',value='JPY',options=['JPY', 'CNY']),
        put_input(name='web',label='网址', type=TEXT),
        put_select(name='status', label='状态',value='申请中',options=['申请中', '已通过', '已结清']),
        put_buttons(['确定','关闭'], onclick=[lambda : _save(-1,pin.date,pin.item,pin.price,pin.currency,pin.web,pin.status,datetime.now()),lambda : close_popup()])
])

#修改记录
def _edit():
    option,df=getData()
    popup('选择要修改的修改记录', [
        put_select(name="edit",label="选择",options=option),
        put_buttons(['确定','关闭'], onclick=[lambda : _edit2(int(pin.edit.split('ー')[0]),df),lambda : close_popup()])
    ])
def _edit2(num,df):
    close_popup()
    
    #NaN不显示
    df=df.fillna('')
    
    popup('修改记录', [
        put_column([
            put_input( name='date',label='日期',value=df.loc[num]['date'],type=DATE),
            put_input(name='item',label='项目', value=df.loc[num]['item'],type=TEXT),
            put_input( name='price',label='金额',value=float(df.loc[num]['price']),type=FLOAT),
            put_select(name='currency', label='币种',value=df.loc[num]['currency'],options=['JPY', 'CNY']),
            put_input(name='web',label='网址',value=df.loc[num]['web'], type=TEXT),
            put_select(name='status', label='状态',value=df.loc[num]['status'],options=['申请中', '已通过', '已结清']),
            ]),
        put_buttons(['确定','关闭'], onclick=[lambda : _save(num,pin.date,pin.item,pin.price,pin.currency,pin.web,pin.status,datetime.now()),lambda : close_popup()])

    ])
    

#删除记录
def _delete():

    option,df=getData()
    
    popup('选择要删除的修改记录', [
        put_select(name="edit",label="选择",options=option),
        put_buttons(['确定','关闭'], onclick=[lambda : _delete2(int(pin.edit.split('ー')[0]),df),lambda : close_popup()])
    ])

def _delete2(num,df):
    close_popup()

    df=df.drop(df.index[[num]])
    df.to_csv('Ledger.csv',index=False)
    
    _update()
    return df

#显示
def _update():
    df = pd.read_csv('Ledger.csv')

    # 追加合计
    total= df['price'].sum() 
    df.loc['合计',:] = ''
    df.loc['合计']['price'] =total
    
    # 修改显示的列名
    df.columns=['日期','项目','金额','币种','网址','状态','更新时间','最后操作人']
    df=df.drop(columns=['网址'])
    #NaN不显示
    df=df.fillna('')

    df1=df.loc[df['状态']=='申请中']
    df1=df1.drop(columns=['状态'])
    total= df1['金额'].sum() 
    df1.loc['合计',:] = ''
    df1.loc['合计']['金额'] =total

    df2=df.loc[df['状态']=='已通过']
    df2=df2.drop(columns=['状态'])
    total= df2['金额'].sum() 
    df2.loc['合计',:] = ''
    df2.loc['合计']['金额'] =total


    df3=df.loc[df['状态']=='已结清']    
    df3=df3.drop(columns=['状态'])
    total= df3['金额'].sum() 
    df3.loc['合计',:] = ''
    df3.loc['合计']['金额'] =total

    # 输出csv
    with use_scope('scope2', clear=True):
        #put_html(df.to_html(border=0))
        put_tabs([
            {'title': '总表', 'content': put_html(df.to_html(border=0))},
            {'title': '申请中', 'content': put_html(df1.to_html(border=0))},
            {'title': '已通过', 'content': put_html(df2.to_html(border=0))},
            {'title': '已结清', 'content': put_html(df3.to_html(border=0))},
        ])
        
    print("update ok")

#写入csv
def _save(index,date,item,price,currency,web,status,time):
    global name

    #print(date)
    data=[date,item,price,currency,web,status,time,name]
    df = pd.read_csv('Ledger.csv')

    # 新增记录
    if index == -1:
        df=df.append(pd.Series(data, index=df.columns),ignore_index=True)
    # 修改记录
    else:
        df=_delete2(index,df)
        df=df.append(pd.Series(data, index=df.columns,name=index))
    df=df.sort_values('date')
    df.to_csv('Ledger.csv',index=False)
    close_popup()
    _update()

# 获取csv里的记录的文字信息
def getData():
    temp=[]
    df = pd.read_csv('Ledger.csv')
    #NaN不显示
    df=df.fillna('')
    for index,row in df.iterrows():
        # 序号ー日期 项目 金额 币种
        temp.append(str(index)+"ー"+row['date']+" "+row['item']+" "+str(row['price'])+" "+row['currency'])
    return temp,df

def test():
    print(1)

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
