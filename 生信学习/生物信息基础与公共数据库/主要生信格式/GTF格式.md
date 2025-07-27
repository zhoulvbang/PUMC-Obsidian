GTF全称为gene transfer format，主要是用来对基因进行注释，当前所广泛使用的gtf格式为第二版（gtf2）。以下均基于gtf2叙述。

gtf同gff3很相似，也是9列内容，其内容如下：

1. `seqname`: 序列的名字。通常格式染色体ID或是contig ID。
2. `source`：注释的来源。通常是预测软件名或是公共数据库。
3. `feature`：基因结构。CDS，start_codon，stop_codon是一定要含有的类型。
4. `start`：开始位点，从1开始计数。
5. `end`：结束位点。
6. `score` ：这一列的值表示对该类型存在性和其坐标的可信度，不是必须的，可以用点“.”代替。
7. `strand`：链的正向与负向，分别用加号+和减号-表示。
8. `frame`：密码子偏移，可以是0、1或2。
9. `attributes`：必须要有以下两个值：  
    　　`gene_id value`; 表示转录本在基因组上的基因座的唯一的ID。gene_id与value值用空格分开，如果值为空，则表示没有对应的基因。  
    　　`transcript_id value`; 预测的转录本的唯一ID。transcript_id与value值用空格分开，空表示没有转录本。

例子：

```r
YL_Chr01    EVM transcript  6582    7082    .   +   .   transcript_id "YL_Chr01G000010.1"; gene_id "YL_Chr01G000010";
YL_Chr01    EVM exon        6582    6648    .   +   .   transcript_id "YL_Chr01G000010.1"; gene_id "YL_Chr01G000010";
YL_Chr01    EVM exon        6829    7082    .   +   .   transcript_id "YL_Chr01G000010.1"; gene_id "YL_Chr01G000010";
YL_Chr01    EVM CDS         6582    6648    .   +   0   transcript_id "YL_Chr01G000010.1"; gene_id "YL_Chr01G000010";
YL_Chr01    EVM CDS         6829    7082    .   +   2   transcript_id "YL_Chr01G000010.1"; gene_id "YL_Chr01G000010";
YL_Chr01    EVM transcript  24963   25235   .   +   .   transcript_id "YL_Chr01G000020.1"; gene_id "YL_Chr01G000020";
YL_Chr01    EVM exon        24963   25235   .   +   .   transcript_id "YL_Chr01G000020.1"; gene_id "YL_Chr01G000020";
YL_Chr01    EVM CDS         24963   25235   .   +   0   transcript_id "YL_Chr01G000020.1"; gene_id "YL_Chr01G000020";
YL_Chr01    EVM transcript  147350  157709  .   -   .   transcript_id "YL_Chr01G000030.1"; gene_id "YL_Chr01G000030";
YL_Chr01    EVM exon        147350  147511  .   -   .   transcript_id "YL_Chr01G000030.1"; gene_id "YL_Chr01G000030";
```

## GTF与GFF比较

`GFF`全称为general feature format，这种格式主要是用来`注释基因组`。  
`GTF`全称为gene transfer format，主要是用来对`基因`进行注释。

GTF 的第九列，通常为：

```r
gene _ id "At1ge0001"; transcript _ id "At1g0ee01.1";
```

而 GFF 的第九列，通常为：

```r
ID =mrnae01; Name = abc 
ID =exon1; Parent =mrnae01
ID =exon2; Parent =mrnae01
```

目前两种文件可以方便的**相互转化**:使用`gffread`

```r
gffread  YL.gff -T -o li.gtf
```


from: [# 基因组注释文件（二）| gff 和 gtf文件格式说明](https://www.jianshu.com/p/04bbbdcf9f81)