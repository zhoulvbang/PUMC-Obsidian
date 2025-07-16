# SAS Viya简介

SAS Viya是一个支持云计算[^1]的内存分析引擎，提供快速、准确和可靠的分析见解。弹性、可扩展和容错处理解决了当今复杂的分析挑战，同时毫不费力地扩展到未来。SAS Viya作为SAS平台的一部分，它提供：

1. 更快地处理大量数据和最复杂的分析，包括机器学习、深度学习和人工智能。
2. 支持SAS和其他语言编程的标准化代码库，如Python、R、Java和Lua。
3. 支持云、现场或混合环境。它可以无缝地部署到任何基础设施或应用生态系统。

|   |   |
|---|---|
|应用名称|英文名称|
|组织和分享内容|SAS® Drive|
|查看报表|SAS® Report Viewer|
|**操作**|   |
|开发SAS代码|SAS® Studio|
|管理数据|SAS® Data Explore|
|准备数据|SAS® Data Studio|
|探索并可视化数据|SAS® Visual Analytics|
|构建模型|SAS® Model Studio|
|管理模型|SAS® Model Manager|
|管理决策|SAS® Decision Manager|
|探索追溯|SAS® Lineage Viewer|
|构建图形|SAS® Graph Builder|
|管理工作流|SAS® Workflow Manager|
|**管理**|   |
|管理环境|SAS® Environment Manager|
|管理主题|SAS® Theme Designer|

# SAS® Drive

是SAS Viya应用程序的中心，通过该应用可以从一个位置轻松查看、组织和共享内容。

相关文档： https://documentation.sas.com/?cdcId=drivecdc&cdcVersion=1.2&docsetId=drivegs&docsetTarget=drivelanding.htm&locale=zh-CN#p1twkprananq1ln1ovn3mvwvivfn

# SAS® Report Viewer

该应用即报表查看器，即该应用用于查看内容，而不生产内容，但其提供了强大的交互功能，如对部分图像上的数据对象进行排序等操作。

该应用可以查看Visual Analytics应用生成的报表。

相关文档： https://documentation.sas.com/?cdcId=vacdc&cdcVersion=8.3&docsetId=vavwr&docsetTarget=n02wiw2qye8gzwn18mfx2pyr5yp1.htm&locale=zh-CN

# SAS® Data Explore

该应用主要提供数据接入的功能。  
该功能需要SAS Data Preparation License授权。  
相关文档：  http://documentation.sas.com/?cdcId=dprepcdc&cdcVersion=2.2&docsetId=datahub&docsetTarget=titlepage.htm&locale=zh-CN

# SAS® Data Studio

主要提供了数据准备的功能，类似于APS中的数据探索功能，包括转换数据、创建计划、剖析（View Profiles）（类似于APS中的分析视图）。  
相关文档： http://documentation.sas.com/?cdcId=dprepcdc&cdcVersion=2.2&docsetId=datastudioadv&docsetTarget=p1trkl1ft8ycqtn1ht74wlgnqrbn.htm&locale=zh-CN

# SAS® Visual Analytics

SAS Visual Analytics 利用 SAS 高性能分析技术，并支持组织极快地探索海量数据以发现模式、趋势和机会，并进一步加以分析。SAS Visual Analytics 极为直观的拖放数据界面与 SAS Cloud Analytic Services (CAS) 的高速处理完美搭配，加快了分析计算速度，可帮助组织从海量数据中提取价值。组织得以信心十足地迅速攻克难题、提高绩效、预测未来绩效、降低风险，综合能力得到前所未有的增强。用户可快速设计报表或仪表板，方便地通过移动设备查看或上网浏览。  
相关文档：http://documentation.sas.com/?cdcId=vacdc&cdcVersion=8.3&docsetId=vaov&docsetTarget=home.htm&locale=zh-cn  
可视化分析得到的结果可以保存为报表并在Report View中进行查看。

# SAS® Model Studio

SAS Viya中包含的Model Studio是一个集成的可视化环境，它提供了一套分析数据挖掘工具，以促进端到端的数据挖掘分析。Model Studio中支持的数据挖掘工具旨在利用SAS Viya编程和云处理环境来交付和分发冠军模型、打分代码和结果。

Model Studio包括如下三个SAS解决方案：  
- SAS Visual Forecasting  
-  SAS Visual Data Mining and Machine Learning  
- SAS Visual Text Analytics  
相关文档：http://documentation.sas.com/?cdcId=capcdc&cdcVersion=8.3&docsetId=capov&docsetTarget=titlepage.htm&locale=zh-CN

# SAS® Model Manager

使用SAS Model Manager，可以将模型存储在公共模型存储库中，并在项目和文件夹中组织它们。还可以评估模型以选择冠军模型，监控模型的性能以及发布模型。  
Model Manager提供了多维度的模型管理功能，如下所示：  
- 存储模型：Model Manager提供了公共模型存储库，可以存储其它SAS Web应用（如Model Studio, SAS Visual Analytics, and SAS Studio）中产生的模型；  
- 组织模型：可以以项目或文件夹的形式组织模型  
- 比较模型：可以比较多个模型并选择冠军模型  
- 评估模型：在测试集上运行模型并进行评分  
- 性能监控：评分数据用于生成模型的性能结果。  
- 发布模型：将模型发布到将模型发布到CAS，Hadoop，SAS Micro Analytic Service和Teradata，以便通过外部应用程序或接口进行评分。。  
- 模型版本管理：创建并管理模型版本。  
Model Manager定位于模型管理，因此并不能直接创建模型，而只能通过导入模型文件（.sas或PMML）的方式创建模型。  

相关文档： http://documentation.sas.com/?cdcId=mdlmgrcdc&cdcVersion=15.2&docsetId=mdlmgrug&docsetTarget=n0ewga3ovt0lg4n105nevqinf9c6.htm&locale=zh-CN

# SAS® Decision Manager

SAS® Decision Manager是企业决策管理系统。它使企业能够使用他们已有的信息做出更好的决策 - 基于预测分析而非过去历史的决策。决策管理系统使决策过程自动化，尤其是日常运营决策。它们通过减少人为干预的需要，提高了日常业务流程的速度，效率和准确性。  
相关文档： https://documentation.sas.com/?cdcId=edmcdc&cdcVersion=5.2&docsetId=edmug&docsetTarget=titlepage.htm&locale=zh-CN

# SAS® Lineage Viewer

该应用用于帮助用户更好地了解Viya应用程序中对象之间的关系。这些对象包括数据，转换过程，报告和可视化。  
选择对象作为主题后，应用程序将显示网络图。此图显示您选择的主题及其所有相关对象。主题和其他对象之间的这些关系存储在关系服务中。  
相关文档： https://documentation.sas.com/?cdcId=dprepcdc&cdcVersion=2.1&docsetId=dmlinug&docsetTarget=titlepage.htm&locale=zh-CN

# SAS® Graph Builder

该应用帮助用户使用基本的图形元素创建自定义图形模板，然后可以在Visual Analytics应用中可以使用这些模板创建报表，并在Report View中查看这些报表。  
相关文档：https://documentation.sas.com/?softwareId=VAORD_graphbuilder&softwareVersion=8.3&requestor=inapp&locale=zh-cn&softwareContextId=SASGraphBuilder

# SAS® Workflow Manager

工作流是一系列任务，包括参与者和完成任务所需的逻辑。工作流可以包括事件、网关、活动和其他元素。通过SAS Workflow Manager，可以将工作流定义的可视模型创建为节点链接图。保存工作流定义时，它将保存为符合BPMN 2.0标准的业务流程模型表示法（BPMN）文件。  
相关文档： https://documentation.sas.com/?cdcId=wfscdc&cdcVersion=2.2&docsetId=wfsug&docsetTarget=titlepage.htm&locale=zh-CN

# SAS® Theme Designer

该应用帮助用户自定义各种SAS Viya应用程序的外观。SAS主题定义应用程序或报表的整体外观。它是使用颜色和图形设计的，这些颜色和图形应用于公共用户界面组件和布局容器。一个设计良好的主题可以在一个产品或一组产品中创建一个强大的视觉标识。您可以使用SAS主题设计器来创建和部署简单的、具有视觉吸引力的、定制的主题。  
相关文档： https://documentation.sas.com/?cdcId=vacdc&cdcVersion=8.3&docsetId=themedesignug&docsetTarget=home.htm&locale=zh-CN

[^1]: **云计算**是一种通过互联网提供计算资源共享池的模型，具有按需自助服务、资源池化、快速伸缩和服务可计量等特征。它通过虚拟化和分布式计算技术，将计算、存储和网络资源集中管理，使用户能够根据需要随时获取所需的资源和服务。云计算的关键技术包括虚拟化和分布式存储，服务模型涵盖IaaS、PaaS和SaaS。它不仅提高了IT资源的利用率，还为企业和个人提供了更加便捷、高效的计算服务。 
