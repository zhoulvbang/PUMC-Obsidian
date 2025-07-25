---
title: R绘图笔记 | R语言绘图系统与常见绘图函数及参数-CSDN博客
source: https://blog.csdn.net/weixin_42655515/article/details/111167082
author:
  - 【云森】
published: 
created: 2025-07-25
description: 文章浏览阅读3.8k次，点赞5次，收藏62次。本文介绍了R语言中的四大绘图系统：base、grid、lattice和ggplot2，对比了它们的特点与应用场景，并详细解释了ggplot2的图形语法及其如何简化高质量图形的制作流程。
tags:
  - clippings
---
本文介绍了R语言中的四大绘图系统：base、grid、lattice和ggplot2，对比了它们的特点与应用场景，并详细解释了ggplot2的图形语法及其如何简化高质量图形的制作流程。

![](https://i-blog.csdnimg.cn/blog_migrate/2c594df7ff17bb4b6cb60e661f68a410.png)

# **一. R语言绘图系统**  

在 R 里，主要有两大底层图形系统，一是 base 图形系统，二是 [grid](https://so.csdn.net/so/search?q=grid&spm=1001.2101.3001.7020) 图形系统。lattice 包与 ggplot2包正是基于 grid 图形系统构建的，它们都有自己独特的图形语法。

```R
install.packages("shiny")

install.packages("ggsci")

install.packages("esquisse")
javascript
```

## **1.base系统**  

• 由Ross Ihaka编写  
• base图形是最古老的系统，在R的初期就存在  
• 容易上手  
• 修改方便，使用灵活  
• 不一定非常美观，需要调整参数修改  
• 使用较多  

## **2.grid系统**  
grid 图形系统可以很容易地控制图形基础单元，由Paul Murrell（2006）编写，给予编程者创作图形极大的灵活性。grid 图形系统还可以产生可编辑的图形组件，这些图形组件可以被复用和重组，并能通过 grid.layout()等函数，把图形输出到指定的位置上。但是因为 grid 包中没有提供生成统计图形及完整绘图的函数，因此很少直接采用 grid 包来分析与展示数据。  

## **3.lattice系统**  

lattice 包通过一维、二维或三维条件绘图，即所谓的栅栏（trellis）图来对多元变量关系进行直观展示。相比于 base()函数是直接在图形设备上绘图的，lattice()函数是返回 trellis 对象。在命令执行的时候，栅栏图会被自动打印，所以看起来就像是 lattice()函数直接完成了绘图。更多关于 base、grid 和 lattice 的语法可以参考 Murrell 和 Paul 所撰写的书籍 R graphics。  
## **4.ggplot2系统**  

ggplot2 包则基于一种全面的图形语法，提供了一种全新的图形创建方式，这套图形语法把绘图过程归纳为数据（data）、转换（transformation）、 度量（scale）、 坐标系（coordinate）、元素（element）、指引（guide）、显示（display）等一系列独立的步骤，通过将这些步骤搭配组合，来实现个性化的统计绘图。于是，得益于该图形语法，Hadley Wickham 所开发的 ggplot2 包是如此人性化，不同于 R base基础绘图和先前的 lattice 包那样参数繁多，而是摈弃了诸多烦琐细节，并以人性化的思维进行高质  
量作图。在 ggplot2 包中，加号（+）的引入是革命性的，这个神奇的符号完成了一系列图形语法叠加。更多 ggplot2 的使用与学习可以参考两本关于 ggplot2 的经典书籍：ggplot2 Elegant Graphicsfor Data Analysis和 R Graphics Cookbook。  
一般的绘图，base+ggplot2就已经够用了，所以，我们的课程就是以这2个系统进行绘图教学。  
ggplot2 是一个功能强大且灵活的 R 包，由 Hadley Wickham 编写，它可以生成优雅而实用的图形。ggplot2 中的 gg 表示图形语法（grammar of graphic），这是一个通过使用“语法” 来绘图的图形概念。ggplot2 主张模块间的协调与分工，整个 ggplot2 的语法框架如图 1-6-1 所示，主要包括数据绘图部分与美化细节部分。R ggplot2 图形语法的主要特点如下所示。  
（1）采用图层的设计方式，有利于结构化思维实现数据可视化。有明确的起始（ggplot()开始）与终止，图层之间的叠加是靠“+”实现的，越往后，其图层越在上方。通常一条 geom\_xxx()函数或 stat\_xxx()函数可以绘制一个图层。  
（2）将表征数据和图形细节分开，能快速将图形表现出来，使创造性的绘图更加容易实现。而且通过 stat\_xxx()函数将常见的统计变换融入绘图中。  
（3）图形美观，扩展包（extension package）丰富，有专门调整颜色（color）、字体（font）和主题（theme）等辅助包。可以帮助用户快读定制个性化的图表。  

![](https://i-blog.csdnimg.cn/blog_migrate/bdc16b532451fd63b71d8f82f60c2f80.png)

ggplot2 的绘图基本语法结构如上图所示。其中所需的图表输入信息如下所示。  
（1）ggplot()：底层绘图函数。DATA 为数据集，主要是数据框（data.frame）格式的数据集；MAPPINGS 变量的视觉通道映射，用来表示变量 x 和 y，还可以用来控制颜色（color）、大小（size）或形状（shape）等视觉通道；STAT 表示统计变换，与 stat\_xxx()相对应，默认为"identity"（无数据变换）；POSITION 表示绘图数据系列的位置调整，默认为"identity"（无位置调整）。  
（2）geom\_xxx() | stat\_xxx()：几何图层或统计变换，比如常见的 geom\_point()（散点图）、geom\_bar()（柱形图）、 geom\_histogram()（统计直方图）、 geom\_ boxplot()（箱形图）、 geom\_line()（折线图）等。我们通常使用 geom\_xxx()函数就可以绘制大部分图表，有时候通过设定 stat 参数可以先实现统计变换。  
可选的图表输入信息包括如下 5 个部分，主要是实现图表的美化与变换等。  
（1）scale\_xxx()：度量调整，调整具体的度量，包括颜色（color）、大小（size）或形状（shape）等，跟 MAPPINGS 的映射变量相对应；  
（2）coord\_xxx()：坐标变换，默认笛卡儿坐标系，还包括极坐标系、地理空间坐标系等； 
（3）facet\_xxx()：分面系统，将某个变量进行分面变换，包括按行、列和网格等形式分面绘图。  
（4）guides()：图例调整，主要包括连续型和离散型两种类型的图例。  
（5）theme()：主题设定，主要用于调整图表的细节，包括图表背景颜色、网格线的间隔与颜色等。  

![](https://i-blog.csdnimg.cn/blog_migrate/cd6e2d7eab04db9c1171acc88dee86d1.png)

# **二. R绘图常见函数与参数**  

## **1.低水平绘图函数**  

```r
lines() 添加线

curve() 添加曲线

abline() 添加给定斜率的线

points() 添加点

segments() 折线

arrows() 箭头

axis() 坐标轴

box() 外框

title() 标题

text() 文字

mtext() 图边文字
go
```

## **2.高水平绘图函数**  

```r
plot() 绘制散点图等多种图形

hist() 直方图

boxplot() 箱线图

stripchart() 点图

barplot() 条形图

dotplot() 点图

piechart() 饼图

interaction.plot()

matplot()
css
```

## **3.常用的绘图参数**  
参数用在函数内部，在没有设定值时使用默认值。  

```r
font= 字体
lty= 线类型
lwd= 线宽度
pch= 点的类型
xlab= 横坐标
ylab= 纵坐标
xlim= 横坐标范围
ylim= 纵坐标范围
pch：指定绘制点所使用的符号，取值范围[0, 24]，其中4是“差号”，20是“点”
cex：指定符号的大小。cex是一个数值，表示pch的倍数，默认是1.5倍
lty：指定线条类型。lty=1代表实线，2至6都是虚线，虚的程度不一样
lwd：指定线条宽度，默认值为lwd=1，可以适当修改1.5倍、2倍等
col：默认绘图颜色。某些函数(如lines、pie)可以接受一个含有颜色值的向量，并自动循环使用。
       例如：col=c("red", "blue")需要绘制三条线，那么三条颜色分别为red、blue、red
col.axis：坐标轴刻度文字的颜色，不是坐标轴的颜色
col.lab：坐标轴标签(名称)的颜色
col.main：标题的颜色
col.sub：副标题的颜色
fg：图形的前景色
bg：图形的背景色
cex.axis：坐标轴刻度文字的缩放倍数
cex.lab：坐标轴标签(名称)的缩放倍数
cex.main：标题的缩放倍数
cex.sub：副标题的缩放倍数
font：整数。用于指定字体样式。1常规、2粗体、3斜体、4粗斜体
pin：以英寸表示图形的宽和高
mai：以数值向量表示边界大小，顺序为"下、左、上、右"，单位为英寸
mar：以数值向量表示边界大小，顺序为"下、左、上、右"，单位为英分，默认值c(5, 4, 4, 2)+0.1
主标题可以使用函数title，格式为：title(main = " ", sub = " ", xlab = " ",  ylab = " ")
makefile
```

参考书籍：R语言数据可视化之美