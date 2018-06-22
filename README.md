### NLTK 

1. 基于百万评论数据
2. 监督学习
3. 抓取评论源码[https://github.com/renxinqiang/SpiderComment](https://github.com/renxinqiang/SpiderComment)
    * 广度优先抓取
    * 存储介质mysql
    * Python3

### 结巴分词
* 分词create_comment_list.py
    * 权重添加
        * ```jieba.add_word('脑子瓦塔',freq=20000)```
        * ```jieba.add_word('玛吉亚巴库内',freq=20000)```
    * 使用停用词stop_words.py 主要过滤口水词
        * ```还是```
        * ```怎么```
        * ```那么```
        * 等等
* 抽取语句标签
    * ```jieba_res = jieba.analyse.extract_tags(comm)```
* 分文件存储
    * comment*.py -> ci
* matplotlib画图工具 matplotlib_test.py
    * 评论数量对应等级用户饼图
        * ![饼状图](/graphics/user_level_cake.png "饼状图")
        * ![柱状图](/graphics/user_level_column.png "柱状图")
            * 从图上看,ZOL用户最高等级是Lv15,而且只有一个人,但是不清楚这哥们在ZOL呆了多长时间
              评论了多少数据才达到这个等级,我去zol查了下,这个用户已经不存在了,可惜
            * 再看呢,100W+评论数主要来源是Lv1-Lv5和没有等级None用户贡献,可以看得出None用户应该是水军,而且被ZOL管理员干掉了查不到等级
              剩下Lv6-Lv15的用户是ZOL真爱
    * 全评论分词Top50热词折线图
        * ![折线图](/graphics/Top50.png "折线图")
            * 可以看出,ZOL的村友们对手机的关注度最高
    * 抽取语句标签并过滤口水词Top50
        * ![折线图](/graphics/Top50_precise.png "折线图")
        * 这样可以看出用户在炮村对手机的关注和评论占很大比重,其次是电脑
          其中,`苹果`,`小米`,`华为`,`三星` 四大品牌名列前茅
          `价格`,`屏幕`,`配置`,`性能`,`内存`,`电池`都是用户关注热点
      