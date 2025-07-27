- 下载并安装:https://www.anaconda.com/docs/getting-started/miniconda/install
- 更新conda
```python
conda update conda
```
- 添加频道(下载源)
	- `conda config --add channels defaults`
	- `conda config --add channels bioconda`
	- `conda config -add channels conda-forge`
- 安装软件:
	- `conda install samtools`