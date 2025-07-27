
## [SAM文件](https://zhida.zhihu.com/search?content_id=191364122&content_type=Article&match_order=1&q=SAM%E6%96%87%E4%BB%B6&zhida_source=entity)格式介绍

SAM（The Sequence Alignment / Map format）格式，即序列比对文件的格式，详细介绍文档：[http://samtools.github.io/hts-specs/SAMv1.pdf](https://link.zhihu.com/?target=http%3A//samtools.github.io/hts-specs/SAMv1.pdf)

SAM文件由两部分组成，头部区和主体区，都以tab分列。

头部区：以 `@` 开始，体现了比对的一些总体信息。比如比对的SAM格式版本，比对的参考序列，比对使用的软件等。

主体区：比对结果，每一个比对结果是一行，有11个主列和一个可选列。

## 头部区简要介绍

1. `@HD VN:1.0 SO:unsorted` （排序类型）

头部区第一行：`VN` 是格式版本；`SO` 表示比对排序的类型，有 `unknown (default)`，`unsorted`，`queryname` 和 `coordinate` 几种。`samtools` 软件在进行行排序后不能自动更新[bam文件](https://zhida.zhihu.com/search?content_id=191364122&content_type=Article&match_order=1&q=bam%E6%96%87%E4%BB%B6&zhida_source=entity)的SO值，而 `picard` 却可以。

2. `@SQ SN:contig1 LN:9401` （序列ID及长度）

参考序列名，这些参考序列决定了比对结果sort的顺序，SN是参考序列名；LN是参考序列长度；每个参考序列为一行。

例如：`@SQ SN:NC_000067.6 LN:195471971` 

3. `@RG ID:sample01` （样品基本信息）

4. `Read Group` 1个sample的测序结果为1个 Read Group；该 `sample` 可以有多个 `library` 的测序结果，可以利用[bwa](https://zhida.zhihu.com/search?content_id=191364122&content_type=Article&match_order=1&q=bwa&zhida_source=entity) mem -R 加上去这些信息。

例如：`@RG ID:ZX1_ID SM:ZX1 LB:PE400 PU:Illumina PL:Miseq` 

5. `ID`：样品的ID号 
6. `SM`：样品名 
7. `LB`：文库名 
8. `PU`：测序以 
9. `PL`：测序平台

这些信息可以在形成sam文件时加入，ID是必须要有的后面是否添加看分析要求

10. `@PG ID:bowtie2 PN:bowtie2 VN:2.0.0-beta7` （比对所使用的软件及版本）

例如：

```bash
@PG ID:bwa PN:bwa VN:0.7.12-r1039 CL:bwa sampe -a 400 -f ZX1.sam -r @RG ID:ZX1_ID SM:ZX1 LB:PE400 PU:Illumina PL:Miseq …/0_Reference/Reference_Sequence.fa ZX_HQ_clean_R1.fq.sai ZX_HQ_clean_R2.fq.sai …/2_HQData/ZX_HQ_clean_R1.fq …/2_HQData/ZX_HQ_clean_R2.fq
```

这里的ID是bwa，PN是bwa，VN是0.7.12-r1039版本。CL可以认为是运行程序@RG是上面RG表示的内容，后面是程序内容，这里的@GR内容是可以自己在运行程序是加入的

## 主体部分介绍

主体部分有11个主列和1个可选列

QNAME 比对的序列名称 例如：M04650:84:000000000-B837R:1:1101:22699:1759（一条测序reads的名称）

FLAG Bwise FLAG（表明比对类型：paring，strand，mate strand等） 例如：99

RENAME 比对上的参考序列名 例如：NC_000075.6

POS 1-Based的比对上的最左边的定位 例如：124057649

MAPQ 比对质量 例如：60

CIGAR Extended [CIGAR string](https://zhida.zhihu.com/search?content_id=191364122&content_type=Article&match_order=1&q=CIGAR+string&zhida_source=entity)（操作符：MIDNSHP）比对结果信息；匹配碱基数，可变剪接等 例如：87M

MRNM 相匹配的另外一条序列，比对上的参考序列名 例如：=

MPOS 1-Based leftmost Mate Position （相比于MRNM列来讲意思和POS差不多） 例如：124057667

ISIZE 插入片段长度 例如：200

SEQ 和参考序列在同一个链上比对的序列（若比对结果在负义链上，则序列是其反向重复序列，反向互补序列） 例如：ATTACTTGGCTGCT

QUAL 比对序列的质量（ASCII-33=Phred base quality）reads碱基质量值 例如：-8CCCGFCCCF7@E-

可选的列 以TAG：TYPE：VALUE的形式提供额外的信息

## 对于每一列内容的详细注解

（如果某一列为“0”或“*”表示这一列没有信息）

第一列：QNAME

进行reads比对时通常表示reads的名字，如果这条reads比对到多条序列或比对到这条序列的多个位置，相同名字会出现多次。如果是pair-end reads，相同名字会出现2次，分别表示来自于R1文件的reads和R2文件的reads，如果其matepair reads也比对2个位置，也会出现2次，则相同名字共出现4次，如果一条reads也比对2个位置，则其matepair比对1个位置，则共出现3次，如果其matepair reads没有比对上序列也会出现1次（第三列显示“*”），所以pair-end测序，R1文件和R2文件同时mapping，相同reads的id最少出现2次。

第二列：FLAG

数值结果如下：

1（1）该read是成对的paired reads中的一个

2（10）paired reads中每个都正确比对到参考序列上

4（100）该read没比对到参考序列上

8（1000）与该read成对的matepair read没有比对到参考序列上

16（10000）该read其反向互补序列能够比对到参考序列

32（100000）与该read成对的matepair read其反向互补序列能够比对到参考序列

64（1000000）在paired reads中，该read是与参考序列比对的第一条

128（10000000）在paired reads中，该read是与参考序列比对的第二条

256（100000000）该read是次优的比对结果

512（1000000000）该read没有通过质量控制

1024（10000000000）由于PCR或测序错误产生的重复reads

2048（100000000000）补充匹配的read

具体的flag值的解释，可以参考samtools软件提供的结果

samtools（Version: 1.3.1）

其中的samtools flags用法可提供flag值的查找结果

About: Convert between textual and numeric flag representation

Usage: samtools flags INT|STR[,...]

例如：

samtools flags 10

0xa 10 PROPER_PAIR,MUNMAP（10=2+8）

samtools flags 12

0xc 12 UNMAP,MUNMAP（12=4+8）

具体的flag值的解释，也可参考如下网站：[Explain SAM Flags](https://link.zhihu.com/?target=https%3A//broadinstitute.github.io/picard/explain-flags.html)

或者在必应当中搜索flag sam点击Explain SAM Flags-GitHub Pages进入该网页，也可以输入组合flag数值会出现所存在的意思

  

SAM、VCF等格式文档的说明(可以直接下载pdf形式的文档)：[GitHub - samtools/hts-specs: Specifications of SAM/BAM and related high-throughput sequencing file formats](https://link.zhihu.com/?target=https%3A//github.com/samtools/hts-specs)

通过python查找想要的read信息的方法：

如果想要得到MREVERSE,READ1这样的read，则需要根据flag值进行筛选，筛选的方法不能够是sam文件中read的flag值是96，应该用如下方法：

![](https://pic1.zhimg.com/v2-7e14380bf41c4aa3ed21164174dcebc2_1440w.jpg)

  

而是要满足read的flag值当中存在MREVERSE,READ1这样的read，即满足mate reverse strand则flag值十进制是32，十六进制是0X20，满足first in pair则flag值十进制是64，十六进制0X40。

通过python的方法提取想要flag值的read可参考如下方法：

int(flag) & 0x20 == 32 and int(flag) & 0x40 == 64，这样能够满足得到十进制是96的read，或者int(flag) & 0x60 == 96，因为十六进制0x20加0x40等于0x60，十进制32加64等于96

下面的方法都可以实现

113 & 0x20 == 32 and 113 & 0x40 == 64

113 & 0x60 == 96

113 & 0x60 == 0x60

  

samtools解释不同十进制和和十六进制的数值的flag值意义

samtools flags 96

0x60 96 MREVERSE,READ1

samtools flags 0x20

0x20 32 MREVERSE

samtools flags 0x40

0x40 64 READ1

第三列：RNAME

  

表示read比对的那条序列的序列名称（名称与头部的@SQ相对应），如果这列是“*”，可以认为这条read没有比对上的序列，则这一行的第四，五，八，九 列是“0”，第六，七列与该列是相同的表示方法

第四列：POS

  

表示read比对到RNAME这条序列的最左边的位置，如果该read能够完全比对到这条序列（CIGAR string为M）则这个位置是read的第一个碱基比对的位置，如果该read的反向互补序列比对到这条序列，则这个位置是read的反向互补序列的第一个碱基比对的位置，所以无论该read是正向比对到该序列，或是其反向互补序列比对到该序列，比对结果均是最左端的比对位置

第五列：MAPQ

  

表示为mapping的质量值，mapping Quality, It equals -10log10Pr{mapping position is wrong}, rounded to the nearest integer, A value 255 indicates that the mapping quality is not available. 该值的计算方法是mapping的错误率的-10log10值，之后四舍五入得到的整数，如果值为255表示mapping值是不可用的，如果是unmapped read则MAPQ为0，一般在使用bwa mem或bwa aln（bwa 0.7.12-r1039版本）生成的sam文件，第五列为60表示mapping率最高，一般结果是这一列的数值是从0到60，且0和60这两个数字出现次数最多

第六列：CIGAR

  

CIGAR string，可以理解为reads mapping到第三列序列的mapping状态，

对于mapping状态可分为以下几类：

M：alignment match (can be a sequence match or mismatch)

表示read可mapping到第三列的序列上，则read的碱基序列与第三列的序列碱基相同，表示正常的mapping结果，M表示完全匹配，但是无论reads与序列的正确匹配或是错误匹配该位置都显示为M

I：insertion to the reference

表示read的碱基序列相对于第三列的RNAME序列，有碱基的插入

D：deletion from the reference

表示read的碱基序列相对于第三列的RNAME序列，有碱基的删除

N：skipped region from the reference

表示可变剪接位置

P：padding (silent deletion from padded reference)

S：soft clipping (clipped sequences present in SEQ)

H：hard clipping (clipped sequences NOT present in SEQ)

clipped均表示一条read的序列被分开，之所以被分开，是因为read的一部分序列能匹配到第三列的RNAME序列上，而被分开的那部分不能匹配到RNAME序列上。

"="表示正确匹配到序列上

"X"表示错误匹配到序列上

而H只出现在一条read的前端或末端，但不会出现在中间，S一般会和H成对出现，当有H出现时，一定会有一个与之对应的S出现

例如：

162M89S

162H89M

149M102S

149H102M

40S211M

20M1D20M211H

S可以单独出现，而H必须有与之对应的S出现时才可能出现，不可在相同第一列的情况下单独出现

N：如果是mRNA-to-genome，N出现的位置代表内含子，其它比对形式出现N时则没有具体解释

M/I/S/=/X：这些数值的加和等于第10列SEQ的长度

第七列：MRNM

  

这条reads第二次比对的位置，在利用bwa mem产生sam文件时，如果该列是“”而

第3列RNAME不是“”则表示该reads比对到第3列显示序列名的序列上，而没有比对到其他位置，在利用bwa aln及bwa sampe比对生成的sam文件，如果和上述情况相同，则第7列为“=”，上述情况均表示该reads只比对到这一个位置

如果第3列RNAME和第7列MRNM都为“*”，则说明这条reads没有匹配上的序列，如果这条reads匹配两个序列，则第一个序列的名称出现在第3列，而第二个序列的名称出现在第7列

第八列：MPOS

  

该列表示与该reads对应的mate pair reads的比对位置，如果这对pair-end reads比对到同一条reference序列上，在sam文件中reads的id出现2次，Read1比对的第4列等于Read2比对的第8列。同样Read1比对的第8列等于Read2比对的第4列。例如：

第1列（Read id）····第4列（Read1比对位置）····第8列（mate-pair reads比对位置）

22699:1759····124057649····124057667

22699:1759····124057667····124057649

相同的reads id一个来自Read1文件，一个来自Read2文件，第4列和第8列是对应的

第九列：ISIZE

  

TLEN：signed observed Template LENgth （可以理解为文库插入片段长度）

如果R1端的read和R2端的read能够mapping到同一条Reference序列上（即第三列RNAME相同），则该列的值表示第8列减去第4列加上第6列的值，R1端和R2端相同id的reads其第九列值相同，但该值为一正一负，R1文件的reads和R2文件的reads，相同id的reads要相对来看。在进行该第列值的计算时，如果取第6列的数值，一定要取出现M的值，S或H的值不能取。

the unisgned observed template length equals the number of base from the leftmost mapped base to the rightmost mappedbase. Theleftmost segment has a plus sign and the rightmost has a minus sign

### 处理bam文件的主要生信软件

主要有bwa，bowtie2，samtools，[bedtools](https://zhida.zhihu.com/search?content_id=191364122&content_type=Article&match_order=1&q=bedtools&zhida_source=entity)等可以看mapping等多方面结果和统计，bedtools工具中genomeCoverageBed的功能是：Compute the coverage of a feature file among a genome

from：[# ！！！生信：sam格式文件解读](https://zhuanlan.zhihu.com/p/464549768)