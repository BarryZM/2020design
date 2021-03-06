# 问题：谁是窃贼
"""
问题描述：
    警察审问4名窃贼嫌疑犯。现在已知，这4人当中仅有一名是窃贼，还知道这4个人中的每个人要么是诚实的，要么总是说谎。
这4个人给警察的回答如下：
    甲说：“乙没有偷，是丁偷的。”
    乙说：“我没有偷，是丙偷的。”
    丙说：“甲没有偷，是乙偷的。”
    丁说：“我没有偷。”
请根据这4个人的回答判断谁是窃贼？

问题分析：
    显然该题是一个逻辑推断问题。已知4个人中的每个人要么是诚实的，要么总是说谎，那么如何来判断他们到底谁是窃贼呢？
    由问题描述可知，甲、乙、丙、丁4人中仅有一名窃贼，且这4个人中每个人要么是诚实的，要么总是说谎。
分析甲、乙、丙3人所说的话可以发现，他们每人都说了两句话，即：“X没有偷，是Y偷的（其中，X、Y指代甲、乙、丙、丁中的某一个）”，
因此，不论这3人是否说谎，他们所提到的这两个人中必有一个是窃贼。而丁只说了他自己没有偷，所以无法判断其真假。
    假设用变量a、b、c、d分别代表4个人，变量的值为1代表该人是窃贼，则根据4个人的说法可列出下面的4个条件：
    甲说：“乙没有偷，是丁偷的。” —— b+d=1 ①
    乙说：“我没有偷，是丙偷的。” —— b+c=1 ②
    丙说：“甲没有偷，是乙偷的。” —— a+b=1 ③
    丁说：“我没有偷。”           —— a+b+c+d=1  ④
    由于甲、乙、丙3人的话中都提到了2个人，其中必有一人是小偷，
所以在根据他们的话列出条件表达式时，可以不关心谁说的是真话，谁说的是假话。
    由于丁的话无法判断真假，所以根据丁的话列出的表达式只反映了4人中仅有一名是窃贼的条件。

算法设计：
    该问题的关键是使用Python语言中的逻辑表达式将问题分析中得到的4个条件表达出来，逻辑表达式如下：
    b+d==1 and b+c==1 and a+b==1 ⑤
    条件④表示a、b、c、d中必有一个为1。
    在程序中可依次假定甲、乙、丙、丁分别为窃贼，带入⑤进行测试，满足条件⑤的那个人为窃贼，具体如下：
先假定甲为窃贼，即a=1，b=0，c=0，d=0，带入条件⑤测试是否成立，若成立则不再对乙、丙、丁进行测试。
    若不成立，则再假定乙为窃贼，即a=0，b=1，c=0，d=0，带入条件⑤测试是否成立，若成立则可确定乙为窃贼，不再对丙、丁进行测试。
    若不成立，再假定丙为窃贼，即a=0，b=0，c=1，d=0，带入条件⑤测试是否成立，若成立则可确定丙为窃贼，不再对丁进行测试。
    若不成立，再假定厂为窃贼，即a=0，b=0，c=0，d=1，带入条件⑤测试是否成立，若成立则确定丁为窃贼。
"""
a = 1  # 先假定甲是窃贼
b = c = d = 0
s = 4
for i in range(1, 4):
    if b + d == 1 and b + c == 1 and a + b == 1:
        s = i
        break  # 测试甲乙丙丁谁是窃贼，符合该条件的即为窃贼
    else:
        if i == 1:  # 甲不是窃贼，测试乙是否是窃贼
            a = 0
            b = 1
        if i == 2:  # 甲乙均不是窃贼，测试丙是否是窃贼
            b = 0
            c = 1
        if i == 3:  # 甲乙丙都不是窃贼，测试丁是否是窃贼
            c = 0
            d = 1
Name = ['无', "甲", "乙", "丙", "丁"]
print("判断结果：\n  {}是窃贼".format(Name[s]))

input("运行完毕，请按回车键退出...")
