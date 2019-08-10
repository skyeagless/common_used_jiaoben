import pandas as pd
df_ori = pd.read_excel("./cepcdata/unit/booster/booster.xlsx").iloc[:,0:7]
df = pd.read_excel("./cepcdata/unit/booster/booster.xlsx").iloc[:,0:7]
# group = df.groupby(['TYPENAME','L[m]'])

df['L[m]'] = df['L[m]'].map(lambda x: round(x,4))

#先建立一个分类汇总数量总统计表
total = pd.DataFrame()

a = []
for k1, group1 in df.groupby(['TYPENAME']):
    for k2,group2 in group1.groupby(['L[m]']):
        a.append(group2)
        total = total.append({'TYPE': "{0}_{1}m".format(group2.iloc[0].loc['TYPENAME'],group2.iloc[0].loc['L[m]']),'COUNT':group2.shape[0]}, ignore_index=True)
order = ["TYPE", "COUNT"]
total = total[order]
total.to_excel("./cepcdata/1.xls",encoding="gbk", index=False)

for item in a:
    row = 0
    res = []
    res = pd.DataFrame(res)
    while( row+1 <= item.shape[0] ):
        res = res.append(item.iloc[row])
        index = item.iloc[row].loc['#NO.']
        #同时如果item的No有连号，那也不需要再从df_ori中取No+1值了,直接跳出本次循环
        if (row+1 != item.shape[0] and item.iloc[row + 1].loc['#NO.'] == index + 1):
            row = row + 1
            continue
        # 再判断一下，如果item正好是原表的最后一项，就可以直接跳出循环了，否则可能df_ori会索引溢出
        if(index != df_ori.shape[0]):
            res = res.append(df_ori.iloc[index])
            row = row+1
        else:
            break

    #true_res是仅含GX[m],GY[m]的值，res是生成的所有值
    true_res = res[["GX[m]","GY[m]"]]
    true_res['GZ[mm]'] = 800
    true_res.rename(columns={true_res.columns[0]: "GX[mm]"}, inplace=True)
    true_res.rename(columns={true_res.columns[1]: "GY[mm]"}, inplace=True)
    # true_res.rename(columns={true_res.columns[2]: "GZ[mm]"}, inplace=True)

    true_res['GX[mm]'] = true_res['GX[mm]'].map(lambda x: x * 1000)
    true_res['GY[mm]'] = true_res['GY[mm]'].map(lambda x: x * 1000)
    # true_res['GZ[mm]'] = true_res['GZ[mm]'].map(lambda x: x * 1000)

    order = ["#NO.", "NAME", "TYPENAME","S[m]","L[m]", "GX[m]","GY[m]"] # "ANGLE[rad]",
    res = res[order]

    writer = pd.ExcelWriter("./cepcdata/1/booster_{0}_{1}m.xls".format(res.iloc[0].loc['TYPENAME'],res.iloc[0].loc['L[m]']))
    true_res.to_excel(writer, 'Sheet1',encoding="gbk", index=False)
    res.to_excel(writer, 'Sheet2',encoding="gbk", index=False)
    writer.save()








