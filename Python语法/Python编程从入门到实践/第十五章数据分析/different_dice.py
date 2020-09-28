from die import Die
import pygal

die1 = Die()
die2 = Die(10)

results = []

for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_side+die2.num_side

for value in range(2,max_result+1):
    frequency = results.count(value) # 返回元素在列表中出现的次数
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Result of rolling a D6 and a D10 50000 timeds"

hist.x_labels = [str(x) for x in range(2,17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('dice.svg')

