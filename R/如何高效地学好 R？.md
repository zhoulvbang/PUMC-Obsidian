#R 
## **1. R基础入门**

学习R语言的最好方法就是在实践中学习，多多动手，多码代码，**这个最重要**。

> 纸上得来终觉浅，绝知此事要躬行。

刚开始学习R语言，可以看一些免费入门视频，可以在B站上面搜，B站有很多免费的R语言入门视频，比如**《尚学堂尹鸿的R语言速成实战》[1]**，这个视频是免费的，视频讲义素材来源于《R语言实战》的第一章到第六章，这几章可以边看书边跟着视频学习，用来入门基本够了。

另外也可以试试一个离线的交互式学习R包——**swirl[2]**包，可以在R软件中安装这个包，然后看看这个**帮助文档[3]**学习怎么用。

也可以在**datacamp[4]**网站中选择它的在线版本进行学习。

![](https://pic3.zhimg.com/80/v2-d2d26e9ca3cc4db6be0b59dffa6d5bde_720w.webp)

如果不想看视频，可以先阅读一些R语言入门的小手册，比如说**[CRAN](https://zhida.zhihu.com/search?content_id=624886800&content_type=Answer&match_order=1&q=CRAN&zhida_source=entity)[5]**上的R介绍手册，对R语言有一个初步了解。

![](https://pica.zhimg.com/80/v2-e9dbd3dc4da326b227965efe00651994_720w.webp)

或者阅读几本不错的R语言入门书籍，比如说**《R语言实战》[6]**、**《R数据科学》[7]**等。对于初学者，建议看中文版即可。

  

![](https://picx.zhimg.com/80/v2-c43ff05455c8a55208fac0c9c4f710ab_720w.webp)

  

英语不错的可以直接看英文原版，比如说**《R for Data Science》[8]**，英文原版有时候更容易理解，有的中文版直译后没有那种味道了。  

## **2. 安装R和[RStudio](https://zhida.zhihu.com/search?content_id=624886800&content_type=Answer&match_order=1&q=RStudio&zhida_source=entity)**

可以从**R官网[9]**中下载和安装R软件，安装不复杂，要是实在不会，就网上百度一下，有很多教程。

安装好R后，可以选择一个R集成开发环境(IDE)，这里强烈推荐安装**RStudio[10]**，RStudio是目前最受欢迎的R集成开发环境，体验效果极佳。

并且RStudio上也提供了很多R学习资源，可以点击菜单栏查看免费获取。

![](https://pic2.zhimg.com/80/v2-10bb1b527cbc09b52cc247c6dc075dff_720w.webp)

## **3. 安装R包**

R包是R函数、数据、预编译代码以一种定义完善的格式组成的集合。

在安装R软件时，R会自动安装一些**基础R包[11]**，这些基础包提供了种类繁多的默认函数和数据集，其他大多数R包都需要自己手动安装，比如说**ggplot2[12]**包、**tidyverse[13]**包。

安装R包主要有三条途径。

### **3.1 CRAN**

大多数R包都可以从CRAN上安装，只需要在命令行中直接输入代码

```text
install.packages("R包名")
```

即可自动安装，建议在Rstudio中将镜像地址改为离你最近的地址。

![](https://picx.zhimg.com/80/v2-08215d168f43f614404e0c67af1fab53_720w.webp)

在CRAN上，R官方专门维护了41个**Task Views[14]**，专门将一些功能相近、同一领域的包罗列在一起，比如说**Survival[15]**系列，从这里你可以快速找到你需要的一组R包。

![](https://pic4.zhimg.com/80/v2-0d4e3c07c34f49796518aa96ced4febd_720w.webp)

### **3.2 bioconductor**

除了CRAN，还可以从**bioconductor[16]**上安装R包，这个数据库专门存储一些生物信息学领域的R包。

![](https://pic3.zhimg.com/80/v2-fbfdeb5d68c62f86720e8e6a2223cfe6_720w.webp)

Bioconductor上的R包安装可以参考官方网站的**安装方法[17]**，与CRAN类似。

  

![](https://pic2.zhimg.com/80/v2-c7713bcb8cf27a5ef265578693f65ac1_720w.webp)

  

```text
install.packages("BiocManager")
BiocManager::install(c("GenomicFeatures", "AnnotationDbi"))
```

### **3.3 github**

另外还可以从**github[18]**上安装R包，有的R包作者没有将自己的代码上传到以上平台，选择存储在github上，我们可以使用**devtools[19]**包从github上安装R包。

对于github上的R包，可以在github上面检索这个R包，找到这个包的官方地址，一般R包作者会在里面说明安装方式，比如说**ggExtra[20]**包。

  

![](https://pic1.zhimg.com/80/v2-1bd9fe2a8e90e6e8ae5453655af4fa70_720w.webp)

  

```text
install.packages("devtools")
devtools::install_github("daattali/ggExtra")
```

### **3.4 本地安装**

如果存在一些怪里怪气的R包，你上面三种方式都安装不了，可以考虑使用本地离线安装，先下载到这个R包的压缩包，再在RStudio中安装，R包的压缩包可以在上面三个平台找。

如果这些方式都安装不了，那大概率说明这个包存在问题。

![](https://pic3.zhimg.com/80/v2-87b107e0e57dd7a508dec03579ad8bf6_720w.webp)

### **3.5 查找需要R包**

R包目前有1万多个，想要快速查找一个自己需要的包有时比较麻烦，我们可以使用**Rdocumentation[21]**、**inside-R[22]**等网站从CRAN、github和bioconductor上快速查找需要的R包。

![](https://picx.zhimg.com/80/v2-655f2283cfe77300900ef1c51439b6d5_720w.webp)

## **4. R与数据导入**

R支持各种数据格式的导入，如下图，R可从键盘、文本、Excel和Access、统计软件、特殊格式文件、数据库管理系统、专业数据库、网站和在线服务中导入数据。

  

![](https://pic2.zhimg.com/80/v2-c52c7611d979cabe9baae22f7ee7b775_720w.webp)

  

来自《R语言实战》

不同的数据格式，需要不同的R包来导入。

### **4.1 文本文件**

文本格式文件可以使用utils包的**read.table()[23]**函数和**read.csv()[24]**函数导入，还有**readr[25]**包和data.table包的**fread()[26]**函数也可以快速导入数据。

### **4.2 Excel文件**

如果是Excel格式文件，可以使用**readxl[27]**包导入，另外**gdata[28]**包和**XLConnect[29]**包也可以导入Excel数据。更多Excel文件导入到R中可以参考**《Reading and Importing Excel Files into R》[30]**这篇文章。

### **4.3 SAS、STATA和SPSS文件**

SAS、STATA和SPSS软件生成的三类数据格式文件可以使用Hadley的**haven[31]**包导入，也可以使用**foreign[32]**包导入，foreign包不但可以导入这三个数据格式文件，还可以导入其他格式文件，比如Systat和Weka格式，同时也可以再次将数据以各种格式从R中导出。

### **4.4 数据库文件**

如果需要导入数据库中的数据文件，不同的数据库所要求的包不同，比如说MySQL数据库，可以使用**MySQL[33]**包读取，**RpostgreSQL[34]**包和**ROracle[35]**包也可以。

另外也可以使用**DBI[36]**包中的函数去指定获取不同的数据库数据。

### **4.5 网络数据**

如果是想使用R来获取网络上的数据，可以使用API或者**rvest[37]**包来抓取数据。网络数据获取入门可以查看Rolf Fredheim的**博客[38]**，这里有很多资源可以获取。

## **5. R与数据处理**

大多数直接导入R中的数据是不能直接用来统计分析和绘图的，需要进行一定的数据处理。

将"脏"数据清洗成"干净"数据对于后续的统计分析和数据可视化非常重要。

R语言内置了很多基础函数来处理数据，但是这些函数数据处理效率一般般，并且也不是那么好用，这里推荐一些不错的数据处理R包和函数。

### **5.1 tidyr包**

**tidyr[39]**包可以用来整理数据，一个好的数据集应该是一行代表一个观测对象，一列代表一个变量，这样的数据集才方便我们使用。要了解有关tidyr包的更多信息，可以查看tidyr包的**帮助文件[40]**。

### **5.2 stringr包**

如果数据集中需要进行字符串操作，可以使用**stringr[41]**包，可以学习这个stringr包的**帮助文件[42]**，这里面包含许多有用的示例帮助快速入门。

### **5.3 dplyr包**

dplyr包是专门用于数据分析的一个R包，也是tidyverse数据科学系列包中的核心R包，在进行常用的数据分析操作时，比如说行筛选、行排列、选择列、创建列等操作，可以优先使用dplyr包，简单、方便、效率高。要了解有关dplyr包的更多信息，可以学习RStudio上的这个**小手册[43]**。

### **5.4 data.table包**

当数据集数据量非常大时，可以使用**data.table[44]**包。要了解更多data.table包的信息，可以学习包的**帮助文件[45]**，也可以阅读黄天元的**《R语言数据高效处理指南》[46]**，这本书专门介绍了R语言中的数据处理，作者也公开了书籍中的**源代码[47]**。

### **5.5 lubridate包**

如果需要处理日期时间类型数据，可以使用**lubridate[48]**包。要了解有关lubridate包的更多信息，可以学习包的**帮助文件[49]**

### **5.6 zoo、xts和quantmod包**

基础包处理时间序列数据的能力有限，可以使用**zoo[50]**、**xts[51]**和**quantmod[52]**包来处理，也可以学习Springer出版的**《Time Series Analysis and Its Applications》[53]**。

如果想全面学习R的高效数据处理，可以阅读《R数据科学》、**《Data Manipulation with R》[54]**或**《Data Wrangling with R》[55]**这几本书，也可以学习RStudio出的**《Data Wrangling with R》[56]**视频。如果您在处理数据时遇到问题，可以查看这**15种解决方案[57]**，也许就能帮到你。

## **6. 数据可视化**

R语言最出色的功能之一就是数据可视化啦。

### **6.1 ggplot2包**

ggplot2包是目前最受欢迎的可视化R包，你可以在**ggplot2官网[58]**学习怎么使用ggplot2包，也可以查看RStudio出品的**cheatsheet手册[59]**或者阅读这本即将出版的**《ggplot2: Elegant Graphics for Data Analysis》[60]**，当然**《R数据可视化手册》[61]**也是一本绝佳的可视化学习书籍。

### **6.2 交互式绘图包**

除了ggplot2包外，学习一些交互式R包也是很有必要的，比如**ggvis[62]**、**googleVis[63]**、**Plotly[64]**。

另外可以在这个**task view[65]**上查看其他的数据可视化R包。

如果绘图时存在问题，可以查看这篇**博客文章[66]**，也许可以帮到你。

### **6.3 空间地理图形**

在R的task view中，有专门的主题用来处理**空间数据[67]**，教你绘制漂亮的地理图形。

首先可以学习下**ggmap[68]**包中的示例，这个包可以让你在静态地图上显示来自Google地图和开放式街道地图等来源的空间数据和模型。另外还可以学习下**maptools[69]**包、**choroplethr[70]**包和**tmap[71]**包。

如果你需要一些更详细的教程，可以查看这篇**帮助文档[72]**以及一些R可视化的博客，如**FlowingData[73]**。

### **6.4 可视化小工具**

目前R中最新的可视化小工具是**HTML widgets[74]**，HTML widgets的工作方式与R相同，但它创建了交互式Web可视化效果，如动态地图 (**leaflet[75]**)、时间序列数据图表(**dygraphs[76]**)和交互式表(**DataTables[77]**)。有一些非常不错的HTML widgets**示例[78]**，以及如何创建自己的HTML widgets的**文档[79]**，有兴趣的可以查看阅读。

### **6.5 配色方案**

R语言绘制出来的图形色彩优美，除了R本身的功劳外，也得益于一些出色的配色R包，比如说**RColorBrewer[80]**包和**ggsci[81]**包，还有一些主题包也不错，比如说**ggthemr[82]**包、**tvthemes[83]**。

### **6.6 图形排版**

图形排版是可视化好图形后遗留的一个小问题了，R中可以进行排版的包有好几个。

**patchwork[84]**包应该是最赞的一个排版包了，这个包排版自定义程度很高，能满足各种排版需要。还有一些包排版也不错，比如说**cowplot[85]**、**Rmisc[86]**、**ggpubr[87]**。

## **7. 机器学习**

机器学习一些常用的包有**caret[88]**、**rpart[89]**和**randomForest[90]**，这些包也有一些不错的学习资源。如果只是入门学习，可以看看这本**指导手册[91]**，也许会有帮助。

另外，也可以读读**《Mastering Machine Learning with R》[92]**和**《Machine Learning with R》[93]**、**《Practical Data Science With R》[94]**、**《A Survival Guide to Data Science with R》[95]**这几本书。

如果你需要一些手把手的教程，可以看看**Kaggle机器学习课程[96]**和Wiekvoet的**博客[97]**。

## **8. RMarkdown与[Shiny](https://zhida.zhihu.com/search?content_id=624886800&content_type=Answer&match_order=1&q=Shiny&zhida_source=entity)**

R Markdown为数据科学提供了一种统一的写作框架，可以集成代码、输出结果和文本注释。R Markdown文档是完全可重用的，并支持多种输出形式，包括PDF、Word、幻灯片等。

R Markdown常见的学习资料包括R Markdown速查表、R Markdown用户指南，在RStudio中可以找到。

![](https://pic3.zhimg.com/80/v2-a31a609b9d15b72e1670442f36b270c2_720w.webp)

除了R markdown，还可以学习下**Shiny[98]**。Shiny让R构建交互式Web应用程序变得很简单，我们可以将分析变成交互式Web应用程序，而不需要了解HTML、CSS或Javascript等。

RStudio是一个很棒的R学习网站，上面有很多很棒的的Shiny**学习资源[99]**，可帮助快速入门Shiny，包括一些**视频教程合集[100]**以及一些高级主题和大量**示例[101]**。

翻译自一篇博客，具体链接点击阅读原文。

### **参考资料**

[1]

R语言速成实战: _[https://www.http://bilibili.com/video/BV1tW411x7rW?p=1](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1tW411x7rW%3Fp%3D1)_

[2]

swirl: _[https://http://swirlstats.com/](https://link.zhihu.com/?target=https%3A//swirlstats.com/)_

[3]

swirl文档: _[https://http://swirlstats.com/students.html](https://link.zhihu.com/?target=https%3A//swirlstats.com/students.html)_

[4]

datacamp: _[https://www.http://datacamp.com/courses/r-programming-with-swirl](https://link.zhihu.com/?target=https%3A//www.datacamp.com/courses/r-programming-with-swirl)_

[5]

CRAN: _[https://http://cran.r-project.org/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/)_

[6]

R语言实战: _[https://http://book.douban.com/subject/26785199/](https://link.zhihu.com/?target=https%3A//book.douban.com/subject/26785199/)_

[7]

R数据科学: _[https://http://book.douban.com/subject/30277904/](https://link.zhihu.com/?target=https%3A//book.douban.com/subject/30277904/)_

[8]

R for Data Science: _[https://r4ds.had.co.nz/index.html](https://link.zhihu.com/?target=https%3A//r4ds.had.co.nz/index.html)_

[9]

R: _[https://http://cran.r-project.org/index.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/index.html)_

[10]

RStudio: _[https://http://rstudio.com/](https://link.zhihu.com/?target=https%3A//rstudio.com/)_

[11]

Base Package: _[https://www.http://rdocumentation.org/packages/base/versions/3.6.2](https://link.zhihu.com/?target=https%3A//www.rdocumentation.org/packages/base/versions/3.6.2)_

[12]

ggplot2: _[https://http://github.com/tidyverse/ggplot2/](https://link.zhihu.com/?target=https%3A//github.com/tidyverse/ggplot2/)_

[13]

tidyverse: _[https://www.http://tidyverse.org/](https://link.zhihu.com/?target=https%3A//www.tidyverse.org/)_

[14]

Task Views: _[https://http://cran.r-project.org/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/)_

[15]

Survival topic: _[https://http://cran.r-project.org/web/views/Survival.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/views/Survival.html)_

[16]

bioconductor: _[https://http://bioconductor.org/](https://link.zhihu.com/?target=https%3A//bioconductor.org/)_

[17]

Install Bioconductor Packages: _[https://http://bioconductor.org/install/#install-bioconductor-packages](https://link.zhihu.com/?target=https%3A//bioconductor.org/install/%23install-bioconductor-packages)_

[18]

github: _[https://http://github.com/](https://link.zhihu.com/?target=https%3A//github.com/)_

[19]

devtools: _[https://http://cran.r-project.org/web/packages/devtools/index.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/devtools/index.html)_

[20]

ggExtra: _[https://http://github.com/daattali/ggExtra](https://link.zhihu.com/?target=https%3A//github.com/daattali/ggExtra)_

[21]

Rdocumentation: _[https://www.http://rdocumentation.org/](https://link.zhihu.com/?target=https%3A//www.rdocumentation.org/)_

[22]

MRAN: _[https://http://mran.microsoft.com/](https://link.zhihu.com/?target=https%3A//mran.microsoft.com/)_

[23]

read.table: _[https://www.http://rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table](https://link.zhihu.com/?target=https%3A//www.rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table)_

[24]

read.csv: _[https://www.http://rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table](https://link.zhihu.com/?target=https%3A//www.rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table)_

[25]

readr: _[https://http://github.com/tidyverse/readr](https://link.zhihu.com/?target=https%3A//github.com/tidyverse/readr)_

[26]

fread: _[https://www.http://rdocumentation.org/packages/data.table/versions/1.13.6/topics/fread](https://link.zhihu.com/?target=https%3A//www.rdocumentation.org/packages/data.table/versions/1.13.6/topics/fread)_

[27]

readxl: _[https://http://github.com/tidyverse/readxl](https://link.zhihu.com/?target=https%3A//github.com/tidyverse/readxl)_

[28]

gdata: _[https://http://cran.r-project.org/web/packages/gdata/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/gdata/)_

[29]

XLConnect: _[https://http://cran.r-project.org/web/packages/XLConnect/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/XLConnect/)_

[30]

Reading and Importing Excel Files into R: _[https://www.http://datacamp.com/community/tutorials/r-tutorial-read-excel-into-r](https://link.zhihu.com/?target=https%3A//www.datacamp.com/community/tutorials/r-tutorial-read-excel-into-r)_

[31]

haven: _[https://http://github.com/tidyverse/haven](https://link.zhihu.com/?target=https%3A//github.com/tidyverse/haven)_

[32]

foreign: _[https://http://cran.r-project.org/web/packages/foreign/index.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/foreign/index.html)_

[33]

MySQL: _[https://http://cran.r-project.org/web/packages/RMySQL/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/RMySQL/)_

[34]

RpostgreSQL: _[https://http://cran.r-project.org/web/packages/RPostgreSQL](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/RPostgreSQL)_

[35]

ROracle: _[https://http://cran.r-project.org/web/packages/ROracle/index.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/ROracle/index.html)_

[36]

DBI: _[https://http://cran.r-project.org/web/packages/DBI](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/DBI)_

[37]

rvest: _[https://http://cran.r-project.org/web/packages/rvest/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/rvest/)_

[38]

Rolf Fredheim: _[http://http://blog.rolffredheim.com/2014/02/web-scraping-basics.html](https://link.zhihu.com/?target=http%3A//blog.rolffredheim.com/2014/02/web-scraping-basics.html)_

[39]

tidyr: _[https://http://cran.r-project.org/web/packages/tidyr/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/tidyr/)_

[40]

tidy-data: _[https://http://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html)_

[41]

stringr: _[https://http://cran.r-project.org/web/packages/stringr](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/stringr)_

[42]

stringr vignette: _[https://http://cran.r-project.org/web/packages/stringr/stringr.pdf](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/stringr/stringr.pdf)_

[43]

dplyr cheatsheet: _[https://http://rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf](https://link.zhihu.com/?target=https%3A//rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf)_

[44]

data.table: _[https://http://cran.r-project.org/web/packages/data.table/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/data.table/)_

[45]

data.table 介绍: _[https://http://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html)_

[46]

R语言数据高效处理指南: _[https://http://zhuanlan.zhihu.com/p/82480894](https://zhuanlan.zhihu.com/p/82480894)_

[47]

书籍源代码: _后台回复20210112即可获取_

[48]

lubridate: _[https://http://cran.r-project.org/web/packages/lubridate/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/lubridate/)_

[49]

lubridate vignettes: _[https://http://cran.r-project.org/web/packages/lubridate/vignettes/lubridate.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/lubridate/vignettes/lubridate.html)_

[50]

zoo: _[https://http://cran.r-project.org/web/packages/zoo](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/zoo)_

[51]

xts: _[https://http://cran.r-project.org/web/packages/xts](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/xts)_

[52]

quantmod: _[https://http://cran.r-project.org/web/packages/quantmod](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/quantmod)_

[53]

时间序列分析及应用: _[https://www.http://springer.com/gp/book/9783319524511](https://link.zhihu.com/?target=https%3A//www.springer.com/gp/book/9783319524511)_

[54]

Data Manipulation with R: _[https://www.http://springer.com/gp/book/9780387747309](https://link.zhihu.com/?target=https%3A//www.springer.com/gp/book/9780387747309)_

[55]

Data Wrangling with R: _[https://www.http://springer.com/gp/book/9783319455983](https://link.zhihu.com/?target=https%3A//www.springer.com/gp/book/9783319455983)_

[56]

Data Wrangling with R: _[https://http://rstudio.com/resources/webinars/data-wrangling-with-r-and-rstudio/](https://link.zhihu.com/?target=https%3A//rstudio.com/resources/webinars/data-wrangling-with-r-and-rstudio/)_

[57]

15 solutions: _[https://www.http://datacamp.com/community/tutorials/15-easy-solutions-data-frame-problems-r](https://link.zhihu.com/?target=https%3A//www.datacamp.com/community/tutorials/15-easy-solutions-data-frame-problems-r)_

[58]

ggplot2官网: _[http://http://ggplot2.org/](https://link.zhihu.com/?target=http%3A//ggplot2.org/)_

[59]

ggplot2 cheatsheet: _[https://http://rstudio.com/resources/cheatsheets/](https://link.zhihu.com/?target=https%3A//rstudio.com/resources/cheatsheets/)_

[60]

ggplot2-book: _[https://http://ggplot2-book.org/](https://link.zhihu.com/?target=https%3A//ggplot2-book.org/)_

[61]

R Graphics Cookbook: _[https://http://book.douban.com/subject/25873705/](https://link.zhihu.com/?target=https%3A//book.douban.com/subject/25873705/)_

[62]

ggvis: _[https://http://ggvis.rstudio.com/](https://link.zhihu.com/?target=https%3A//ggvis.rstudio.com/)_

[63]

googleVis: _[https://http://github.com/mages/googleVis](https://link.zhihu.com/?target=https%3A//github.com/mages/googleVis)_

[64]

Plotly: _[https://http://plotly.com/r/](https://link.zhihu.com/?target=https%3A//plotly.com/r/)_

[65]

Graphics view: _[https://http://cran.r-project.org/web/views/Graphics.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/views/Graphics.html)_

[66]

R绘图的15个常见问题: _[https://www.http://datacamp.com/community/tutorials/15-questions-about-r-plots](https://link.zhihu.com/?target=https%3A//www.datacamp.com/community/tutorials/15-questions-about-r-plots)_

[67]

空间数据: _[https://http://cran.r-project.org/web/views/Spatial.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/views/Spatial.html)_

[68]

ggmap: _[https://http://cran.r-project.org/web/packages/ggmap/index.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/ggmap/index.html)_

[69]

maptools: _[http://http://maptools.r-forge.r-project.org/](https://link.zhihu.com/?target=http%3A//maptools.r-forge.r-project.org/)_

[70]

choroplethr: _[https://http://cran.r-project.org/web/packages/choroplethr/index.html](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/choroplethr/index.html)_

[71]

tmap: _[https://http://github.com/mtennekes/tmap](https://link.zhihu.com/?target=https%3A//github.com/mtennekes/tmap)_

[72]

空间数据可视化文档: _后台回复20210112即可获取_

[73]

FlowingData: _[https://http://flowingdata.com/](https://link.zhihu.com/?target=https%3A//flowingdata.com/)_

[74]

HTML widgets: _[http://www.http://htmlwidgets.org/](https://link.zhihu.com/?target=http%3A//www.htmlwidgets.org/)_

[75]

leaflet: _[https://http://rstudio.github.io/leaflet/](https://link.zhihu.com/?target=https%3A//rstudio.github.io/leaflet/)_

[76]

dygraphs: _[https://http://rstudio.github.io/dygraphs/](https://link.zhihu.com/?target=https%3A//rstudio.github.io/dygraphs/)_

[77]

DataTables: _[https://http://rstudio.github.io/DT/](https://link.zhihu.com/?target=https%3A//rstudio.github.io/DT/)_

[78]

showcase: _[http://www.http://htmlwidgets.org/showcase_leaflet.html](https://link.zhihu.com/?target=http%3A//www.htmlwidgets.org/showcase_leaflet.html)_

[79]

documentation: _[http://www.http://htmlwidgets.org/develop_intro.html](https://link.zhihu.com/?target=http%3A//www.htmlwidgets.org/develop_intro.html)_

[80]

RColorBrewer: _[https://http://cran.r-project.org/web/packages/RColorBrewer/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/RColorBrewer/)_

[81]

ggsci: _[https://http://github.com/nanxstats/ggsci](https://link.zhihu.com/?target=https%3A//github.com/nanxstats/ggsci)_

[82]

ggthemr: _[https://http://github.com/Mikata-Project/ggthemr](https://link.zhihu.com/?target=https%3A//github.com/Mikata-Project/ggthemr)_

[83]

tvthemes: _[https://http://github.com/Ryo-N7/tvthemes](https://link.zhihu.com/?target=https%3A//github.com/Ryo-N7/tvthemes)_

[84]

patchwork: _[https://http://patchwork.data-imaginist.com/index.html](https://link.zhihu.com/?target=https%3A//patchwork.data-imaginist.com/index.html)_

[85]

cowplot: _[https://http://github.com/wilkelab/cowplot](https://link.zhihu.com/?target=https%3A//github.com/wilkelab/cowplot)_

[86]

Rmisc: _[https://http://cran.r-project.org/package=Rmisc](https://link.zhihu.com/?target=https%3A//cran.r-project.org/package%3DRmisc)_

[87]

ggpubr: _[https://http://github.com/kassambara/ggpubr](https://link.zhihu.com/?target=https%3A//github.com/kassambara/ggpubr)_

[88]

caret: _[https://http://cran.r-project.org/web/packages/caret/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/caret/)_

[89]

rpart: _[https://http://cran.r-project.org/web/packages/rpart/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/rpart/)_

[90]

randomForest: _[https://http://cran.r-project.org/web/packages/randomForest/](https://link.zhihu.com/?target=https%3A//cran.r-project.org/web/packages/randomForest/)_

[91]

机器学习指导手册: _[https://http://machinelearningmastery.com/](https://link.zhihu.com/?target=https%3A//machinelearningmastery.com/)_

[92]

Mastering Machine Learning with R: _[https://www.http://oreilly.com/library/view/mastering-machine-learning/9781789618006/](https://link.zhihu.com/?target=https%3A//www.oreilly.com/library/view/mastering-machine-learning/9781789618006/)_

[93]

Machine Learning with R: _[https://www.http://oreilly.com/library/view/machine-learning-with/9781617296574/](https://link.zhihu.com/?target=https%3A//www.oreilly.com/library/view/machine-learning-with/9781617296574/)_

[94]

Practical Data Science with R: _[https://www.http://manning.com/books/practical-data-science-with-r](https://link.zhihu.com/?target=https%3A//www.manning.com/books/practical-data-science-with-r)_

[95]

A Survival Guide to Data Science with R: _[https://http://togaware.com/onepager/](https://link.zhihu.com/?target=https%3A//togaware.com/onepager/)_

[96]

Kaggle Machine Learning course: _[https://www.http://datacamp.com/courses/kaggle-tutorial-on-machine-learing-the-sinking-of-the-titanic?tap_a=5644-dce66f&tap_s=10907-287229](https://link.zhihu.com/?target=https%3A//www.datacamp.com/courses/kaggle-tutorial-on-machine-learing-the-sinking-of-the-titanic%3Ftap_a%3D5644-dce66f%26tap_s%3D10907-287229)_

[97]

Wiekvoet博客: _[https://wiekvoet.blogspot.be/](https://link.zhihu.com/?target=https%3A//wiekvoet.blogspot.be/)_

[98]

Shiny: _[https://http://shiny.rstudio.com/](https://link.zhihu.com/?target=https%3A//shiny.rstudio.com/)_

[99]

Shiny资源: _[https://http://shiny.rstudio.com/tutorial/](https://link.zhihu.com/?target=https%3A//shiny.rstudio.com/tutorial/)_

[100]

Shiny视频: _[https://http://shiny.rstudio.com/articles/](https://link.zhihu.com/?target=https%3A//shiny.rstudio.com/articles/)_

[101]

Shiny示例: _[https://http://shiny.rstudio.com/gallery/](https://link.zhihu.com/?target=https%3A//shiny.rstudio.com/gallery/)_