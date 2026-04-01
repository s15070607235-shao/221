# 简易订单计价服务

这是一个可运行的最小业务示例：**订单计价**。

## 业务规则
- 小计 = `unit_price * quantity`
- 会员折扣：
  - regular: 0%
  - silver: 5%
  - gold: 10%
- 最终总价 = `小计 - 会员折扣 - coupon`
- 最终价格不会低于 0。

## 运行示例
```bash
python3 main.py
```

## 运行测试
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```
