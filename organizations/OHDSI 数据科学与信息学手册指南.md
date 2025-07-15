## 项目介绍

**OHDSI（Observational Health Data Sciences and Informatics）** 是一个全球性的开放科学协作组织，专注于通过观察性健康数据来推动医疗知识的发现。本项目《OHDSI 数据科学与信息学手册》是该社区的一个核心知识库，旨在为新老成员提供关于OHDSI社区、数据标准、工具的全面指南。它不仅阐述了OHDSI的理念与目标，还详细指导如何参与这一旅程，了解通用数据模型、标准词汇以及其在实际中的三个主要应用场景。

## 项目快速启动

### 环境准备

确保你的开发环境已安装Git、R语言环境及必要的R包管理工具。OHDSI的许多工具依赖于R语言。

首先，克隆项目到本地：

```bash
git clone https://github.com/OHDSI/TheBookOfOhdsi.git
cd TheBookOfOhdsi
```

### 构建与查看手册

接下来，如果你拥有RStudio或可以直接运行R脚本，可以使用`bookdown`包来构建这本书：

```r
install.packages("bookdown")
library(bookdown)
render_book("index.Rmd", "bookdown::pdf_book")
```

这将生成PDF版本的手册。若要在线预览或创建HTML版本，可使用相应的渲染命令。

## 应用案例与最佳实践

OHDSI社区在多个领域展示了强大的实力，从药物安全性评估到疾病预测模型的建立。例如，利用OHDSI的通用数据模型（OMOP CDM），研究者们能够标准化不同来源的医疗数据，进行大规模的回顾性研究。最佳实践中，社区推崇“Study-a-Thon”模式，这是一种集中的开放式研究活动，参与者共同探索特定的医疗问题，这种方法促进了数据科学家之间的合作，并诞生了许多重要的研究成果。

## 典型生态项目

OHDSI生态系统包含了一系列工具和服务，支持数据清洗（ETL）、分析、以及结果的可视化。其中，[Atlas](http://atlas-demo.ohdsi.org/)是一个用于交互式数据分析的web应用程序，而[Evidence Foundation](https://www.evidencefoundation.net/)提供了方法学支持和平台，帮助生成真实世界证据。此外，HADES是一套开源工具，支持数据库的标准化和查询，是OHDSI项目中不可或缺的一部分。