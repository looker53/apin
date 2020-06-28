## 快速使用

步骤1：生成默认的 yaml 文件：
```
apin init
```
步骤2：运行用例, 可以不指定路径，可以指定文件夹或者文件：
```python
apin.run()
apin.run("/tests")
apin.run("/tests/test_demo.yml")
```

## unittest 集成
不和单元测试框架集成的话日志显示不好处理。 参考 httprunner 2.x

