current_earth_weight = float(input("请输入您当前的地球体重（kg）："))
lunar_ratio = 0.165  # 月球重量是地球的16.5%
print("未来10年地球和月球体重变化：")
for year in range(1, 11):
    earth_weight = current_earth_weight + year * 0.5
    lunar_weight = earth_weight * lunar_ratio
    print(f"第{year}年：地球体重 {earth_weight:.2f}kg，月球体重 {lunar_weight:.2f}kg")
