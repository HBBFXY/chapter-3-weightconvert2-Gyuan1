weight = float(input("请输入重量数值："))
unit = input("请输入单位（kg 表示千克，lb 表示磅）：")
if unit == "kg":
    pound = weight * 2.20462
    print(f"{weight} 千克 = {pound:.2f} 磅")
elif unit == "lb":
    kg = weight / 2.20462
    print(f"{weight} 磅 = {kg:.2f} 千克")
else:
    print("请输入有效的单位（kg 或 lb）")
