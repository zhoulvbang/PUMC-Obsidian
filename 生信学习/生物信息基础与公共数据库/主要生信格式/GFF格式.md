GFF(General Feature Format)是一种用来描述基因组特征的文件，现在我们所使用的大部分都是第三版（gff3）。

gff文件除gff1以外均由9列数据组成，前8列在gff的3个版本中信息都是相同的，只是名称不同：

gtf文件是以tab键分割的9列组成，以下为每一列的对应信息：

1. `seqid` ：参考序列的id。
2. `source`：注释的来源。如果未知，则用点（.）代替。一般指明产生此gff3文件的软件或方法。
3. `type`： 类型，此处的名词是相对自由的，建议使用符合SO惯例的名称（sequenceontology），如gene，repeat_region，exon，CDS等。
4. `start`：开始位点，从1开始计数（区别于bed文件从0开始计数）。
5. `end`：结束位点。
6. `score`：得分，对于一些可以量化的属性，可以在此设置一个数值以表示程度的不同。如果为空，用点（.）代替。
7. `strand`：“＋”表示正链，“－”表示负链，“.”表示不需要指定正负链。
8. `phase` ：步进。对于编码蛋白质的CDS来说，本列指定下一个密码子开始的位置。可以是0、1或2，表示到达下一个密码子需要跳过的碱基个数。
9. `attributes`：属性。一个包含众多属性的列表，格式为“标签＝值”（tag=value），不同属性之间以分号相隔。  

**下列的标签已定义：

- `ID`：指定一个唯一的标识。对属性分类是非常好用（例如查找一个转录单位中所以的外显子）。
- `Name`：指定属性的名称。展示给用户的就是该属性。
- `Alias`：名称的代称或其它。当存在其它名称时使用该属性。
- `Note`：描述性的一些说明。  

Alias和Note可以有多个值，不同值之间以逗号分隔。  
如：Alias=M19211,gna-12,GAMMA-GLOBULIN

在GFF文件的开头，可以有 `#` 开头的注释行,示例如下

```r
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build GRCh38.p12
#!genome-build-accession NCBI_Assembly:GCF_000001405.38
#!annotation-date 26 March 2018
#!annotation-source NCBI Homo sapiens Annotation Release 109
##sequence-region NC_000001.11 1 248956422
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9606
```
对于不同的基因组特征，其属性不同。

1. 染色体  
    染色体用region表示，1号染色体对应的信息如下
```r
NC_000001.11    RefSeq    region    1    248956422    .    +    .    ID=id0;Dbxref=taxon:9606;Name=1;chromosome=1;gbkey=Src;genome=chromosome;mol_type=genomic DNA
```
染色体是基础，后续的基因，exon等都是需要定位在染色体上的。

2. 非编码基因  
    对于非编码基因，首先给出基因的起始和终止位置，然后描述转录本的信息。对于转录本而言, 通过exon展示其结构。
假基因示例如下
```r
NC_000001.11    BestRefSeq    pseudogene    11874    14409    .    +    .    ID=gene0;Dbxref=GeneID:100287102,HGNC:HGNC:37102;Name=DDX11L1;description=DEAD/H-box helicase 11 like 1;gbkey=Gene;gene=DDX11L1;gene_biotype=transcribed_pseudogene;pseudo=true
NC_000001.11    BestRefSeq    transcript    11874    14409    .    +    .    ID=rna0;Parent=gene0;Dbxref=GeneID:100287102,Genbank:NR_046018.2,HGNC:HGNC:37102;Name=NR_046018.2;gbkey=misc_RNA;gene=DDX11L1;product=DEAD/H-box helicase 11 like 1;transcript_id=NR_046018.2
NC_000001.11    BestRefSeq    exon    11874    12227    .    +    .    ID=id1;Parent=rna0;Dbxref=GeneID:100287102,Genbank:NR_046018.2,HGNC:HGNC:37102;gbkey=misc_RNA;gene=DDX11L1;product=DEAD/H-box helicase 11 like 1;transcript_id=NR_046018.2
NC_000001.11    BestRefSeq    exon    12613    12721    .    +    .    ID=id2;Parent=rna0;Dbxref=GeneID:100287102,Genbank:NR_046018.2,HGNC:HGNC:37102;gbkey=misc_RNA;gene=DDX11L1;product=DEAD/H-box helicase 11 like 1;transcript_id=NR_046018.2
NC_000001.11    BestRefSeq    exon    13221    14409    .    +    .    ID=id3;Parent=rna0;Dbxref=GeneID:100287102,Genbank:NR_046018.2,HGNC:HGNC:37102;gbkey=misc_RNA;gene=DDX11L1;product=DEAD/H-box helicase 11 like 1;transcript_id=NR_046018.2
```
tRNA基因示例如下
```r
NC_000010.11    tRNAscan-SE    gene    67764503    67764584    .    +    .    ID=gene28271;Dbxref=GeneID:100189279,HGNC:HGNC:34845;Name=TRS-TGA1-1;gbkey=Gene;gene=TRS-TGA1-1;gene_biotype=tRNA
NC_000010.11    tRNAscan-SE    tRNA    67764503    67764584    .    +    .    ID=rna83632;Parent=gene28271;Dbxref=GeneID:100189279,HGNC:HGNC:34845;Note=transfer RNA-Ser (TGA) 1-1;anticodon=(pos:67764536..67764538);gbkey=tRNA;gene=TRS-TGA1-1;inference=COORDINATES: profile:tRNAscan-SE:1.23;product=tRNA-Ser
NC_000010.11    tRNAscan-SE    exon    67764503    67764584    .    +    .    ID=id1011659;Parent=rna83632;Dbxref=GeneID:100189279,HGNC:HGNC:34845;Note=transfer RNA-Ser (TGA) 1-1;anticodon=(pos:67764536..67764538);gbkey=tRNA;gene=TRS-TGA1-1;inference=COORDINATES: profile:tRNAscan-SE:1.23;product=tRNA-Ser
```
miRNA基因示例如下
```r
NC_000001.11    BestRefSeq    gene    17369    17436    .    -    .    ID=gene2;Dbxref=GeneID:102466751,HGNC:HGNC:50039,miRBase:MI0022705;Name=MIR6859-1;description=microRNA 6859-1;gbkey=Gene;gene=MIR6859-1;gene_biotype=miRNA;gene_synonym=hsa-mir-6859-1
NC_000001.11    BestRefSeq    primary_transcript    17369    17436    .    -    .    ID=rna2;Parent=gene2;Dbxref=GeneID:102466751,Genbank:NR_106918.1,HGNC:HGNC:50039,miRBase:MI0022705;Name=NR_106918.1;gbkey=precursor_RNA;gene=MIR6859-1;product=microRNA 6859-1;transcript_id=NR_106918.1
NC_000001.11    BestRefSeq    exon    17369    17436    .    -    .    ID=id15;Parent=rna2;Dbxref=GeneID:102466751,Genbank:NR_106918.1,HGNC:HGNC:50039,miRBase:MI0022705;gbkey=precursor_RNA;gene=MIR6859-1;product=microRNA 6859-1;transcript_id=NR_106918.1
NC_000001.11    BestRefSeq    miRNA    17369    17391    .    -    .    ID=rna3;Parent=rna2;Dbxref=GeneID:102466751,miRBase:MIMAT0027619,HGNC:HGNC:50039,miRBase:MI0022705;gbkey=ncRNA;gene=MIR6859-1;product=hsa-miR-6859-3p
NC_000001.11    BestRefSeq    exon    17369    17391    .    -    .    ID=id16;Parent=rna3;Dbxref=GeneID:102466751,miRBase:MIMAT0027619,HGNC:HGNC:50039,miRBase:MI0022705;gbkey=ncRNA;gene=MIR6859-1;product=hsa-miR-6859-3p
NC_000001.11    BestRefSeq    miRNA    17409    17431    .    -    .    ID=rna4;Parent=rna2;Dbxref=GeneID:102466751,miRBase:MIMAT0027618,HGNC:HGNC:50039,miRBase:MI0022705;gbkey=ncRNA;gene=MIR6859-1;product=hsa-miR-6859-5p
NC_000001.11    BestRefSeq    exon    17409    17431    .    -    .    ID=id17;Parent=rna4;Dbxref=GeneID:102466751,miRBase:MIMAT0027618,HGNC:HGNC:50039,miRBase:MI0022705;gbkey=ncRNA;gene=MIR6859-1;product=hsa-miR-6859-5p
```
一个miRNA基因的最终会形成两个成熟的miRNA。

lncRNA基因示例如下
```r
NC_000001.11    Gnomon    gene    29926    31295    .    +    .    ID=gene3;Dbxref=GeneID:107985730,HGNC:HGNC:52482;Name=MIR1302-2HG;gbkey=Gene;gene=MIR1302-2HG;gene_biotype=lncRNA
NC_000001.11    Gnomon    lnc_RNA    29926    31295    .    +    .    ID=rna5;Parent=gene3;Dbxref=GeneID:107985730,Genbank:XR_001737835.1,HGNC:HGNC:52482;Name=XR_001737835.1;gbkey=ncRNA;gene=MIR1302-2HG;model_evidence=Supporting evidence includes similarity to: 100%25 coverage of the annotated genomic feature by RNAseq alignments%2C including 8 samples with support for all annotated introns;product=MIR1302-2 host gene;transcript_id=XR_001737835.1
NC_000001.11    Gnomon    exon    29926    30039    .    +    .    ID=id18;Parent=rna5;Dbxref=GeneID:107985730,Genbank:XR_001737835.1,HGNC:HGNC:52482;gbkey=ncRNA;gene=MIR1302-2HG;product=MIR1302-2 host gene;transcript_id=XR_001737835.1
NC_000001.11    Gnomon    exon    30564    30667    .    +    .    ID=id19;Parent=rna5;Dbxref=GeneID:107985730,Genbank:XR_001737835.1,HGNC:HGNC:52482;gbkey=ncRNA;gene=MIR1302-2HG;product=MIR1302-2 host gene;transcript_id=XR_001737835.1
```

3. 蛋白编码基因  
    对于蛋白编码基因，在非编码基因的基础上，多出了CDS的信息。示例如下
```r
NC_000010.11    BestRefSeq%2CGnomon    gene    35126830    35212958    .    +    .    ID=gene27850;Dbxref=GeneID:1390,HGNC:HGNC:2352,MIM:123812;Name=CREM;description=cAMP responsive element modulator;gbkey=Gene;gene=CREM;gene_biotype=protein_coding;gene_synonym=CREM-2,hCREM-2,ICER
NC_000010.11    BestRefSeq    mRNA    35126841    35179847    .    +    .    ID=rna82191;Parent=gene27850;Dbxref=GeneID:1390,Genbank:NM_001881.3,HGNC:HGNC:2352,MIM:123812;Name=NM_001881.3;gbkey=mRNA;gene=CREM;product=cAMP responsive element modulator%2C transcript variant 2;transcript_id=NM_001881.3
NC_000010.11    BestRefSeq    exon    35126841    35127193    .    +    .    ID=id995818;Parent=rna82191;Dbxref=GeneID:1390,Genbank:NM_001881.3,HGNC:HGNC:2352,MIM:123812;gbkey=mRNA;gene=CREM;product=cAMP responsive element modulator%2C transcript variant 2;transcript_id=NM_001881.3
NC_000010.11    BestRefSeq    exon    35148368    35148491    .    +    .    ID=id995819;Parent=rna82191;Dbxref=GeneID:1390,Genbank:NM_001881.3,HGNC:HGNC:2352,MIM:123812;gbkey=mRNA;gene=CREM;product=cAMP responsive element modulator%2C transcript variant 2;transcript_id=NM_001881.3
NC_000010.11    BestRefSeq    exon    35178889    35178986    .    +    .    ID=id995820;Parent=rna82191;Dbxref=GeneID:1390,Genbank:NM_001881.3,HGNC:HGNC:2352,MIM:123812;gbkey=mRNA;gene=CREM;product=cAMP responsive element modulator%2C transcript variant 2;transcript_id=NM_001881.3
NC_000010.11    BestRefSeq    exon    35179134    35179847    .    +    .    ID=id995821;Parent=rna82191;Dbxref=GeneID:1390,Genbank:NM_001881.3,HGNC:HGNC:2352,MIM:123812;gbkey=mRNA;gene=CREM;product=cAMP responsive element modulator%2C transcript variant 2;transcript_id=NM_001881.3
NC_000010.11    BestRefSeq    CDS    35148372    35148491    .    +    0    ID=cds57086;Parent=rna82191;Dbxref=CCDS:CCDS7184.1,GeneID:1390,Genbank:NP_001872.3,HGNC:HGNC:2352,MIM:123812;Name=NP_001872.3;Note=isoform 2 is encoded by transcript variant 2;gbkey=CDS;gene=CREM;product=cAMP-responsive element modulator isoform 2;protein_id=NP_001872.3
NC_000010.11    BestRefSeq    CDS    35178889    35178986    .    +    0    ID=cds57086;Parent=rna82191;Dbxref=CCDS:CCDS7184.1,GeneID:1390,Genbank:NP_001872.3,HGNC:HGNC:2352,MIM:123812;Name=NP_001872.3;Note=isoform 2 is encoded by transcript variant 2;gbkey=CDS;gene=CREM;product=cAMP-responsive element modulator isoform 2;protein_id=NP_001872.3
NC_000010.11    BestRefSeq    CDS    35179134    35179329    .    +    1    ID=cds57086;Parent=rna82191;Dbxref=CCDS:CCDS7184.1,GeneID:1390,Genbank:NP_001872.3,HGNC:HGNC:2352,MIM:123812;Name=NP_001872.3;Note=isoform 2 is encoded by transcript variant 2;gbkey=CDS;gene=CREM;product=cAMP-responsive element modulator isoform 2;protein_id=NP_001872.3
```
需要注意是，由于可变剪切的存在，一个蛋白编码基因可能会有多个转录本。

查看第9列有哪些注释信息：

```r
$awk 'BEGIN{FS=OFS="\t"} $3=="gene"{split($9, a, ";"); for(i in a){split(a[i], b, "="); if(++c[b[1]]==1) print b[1]}}'  abc.gff
ID
Accession
annotation
Name
product
```