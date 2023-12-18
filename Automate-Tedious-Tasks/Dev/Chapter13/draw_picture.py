import openpyxl
import openpyxl.chart

wb = openpyxl.Workbook()  # 创建一个Workbook对象
sheet = wb.active  # 选择活动的工作表

# 假设我们在工作表中填充了一些数据，例如在A1到A10的单元格中
for i in range(1, 11):
    sheet['A' + str(i)] = i

# 创建一个Reference对象，指定数据范围为A1到A10
refObj = openpyxl.chart.Reference(
    sheet,
    min_col=1, min_row=1,
    max_col=1, max_row=10
)

seriesObj = openpyxl.chart.Series(refObj, title='First series')

chartObj = openpyxl.chart.BarChart()  # 创建一个BarChart对象
chartObj.title = 'My Chart'
chartObj.append(seriesObj)
sheet.add_chart(chartObj, 'C5')
wb.save('sampleChart.xlsx')
