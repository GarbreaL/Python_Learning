mGramNow=float(input("请输入贵金属当前质量（克）："))
mCost=float(input("请输入当前成本价格："))
mPrice=float(input("请输入当前价格："))
mTargetCost=float(input("请输入目标成本价格："))
mGramx=(mGramNow*mCost-mTargetCost*mGramNow)/(mTargetCost-mPrice)

print("当前价格下，要达到目标成本需要购买贵金属{0}克，需要花费{1}".format(mGramx, mGramx * mPrice))
