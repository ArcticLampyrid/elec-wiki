***Only Chinese version is available.***

# Elec Wiki
## 项目说明
Elec Wiki 致力于成为一个免费开放且持续更新的电子工程知识库，旨在帮助电子设计竞赛考生和电子爱好者学习电子相关知识。

## 部署指南
> [!TIP]  
> 为了确保构建系统能够成功从 Git Commits 中获取作者信息等元数据，请拉取全部历史记录。（如只用于预览结果，可忽略此要求。）

### 使用 Docker 部署
```bash
docker buildx build -t elec-wiki .
docker run --rm -p 40000:80 elec-wiki
```

### 自定义部署
首先，确保您已安装 Git、Python 3、Poetry。对于 Arch Linux 用户，可以使用以下命令安装：
```bash
sudo pacman -S git python python-poetry
```

然后，在本项目根目录下执行以下命令：
```bash
poetry install
poetry run mkdocs build
```

即可生成纯静态的站点文件，将 `site/` 目录下的文件部署到您的 Web 服务器即可。

> [!TIP]  
> 如果仅需要预览效果，可以使用 `poetry run mkdocs serve` 命令启动本地预览服务器。（该服务器性能较差，不建议用于生产环境。）



## 工程结构
对于文档：
- 每个文档应放置在一个单独的目录中，目录名即为文档名。
- 每个文档目录下应包含一个 `index.md` 文件，作为文档内容。
- 目录下同时也可以包含其他的图片、代码等资源文件，以供引用。
- 每个文档目录还应该包含一个 `.pages` 文件，并设置内容为 `collapse: true`。
- 每个文档应该具有唯一的 `# H1` 标题，并位于文件首部。其内容将作为文档的标题。

对于分类：
- 所有文档应放置在 `docs/` 目录下，以 `docs/分类/子分类/.../文档名/` 的形式组织。
- 在每个分类目录下，应包含一个 `.pages` 文件，设置分类的名称和分类下属内容的导航栏顺序，如：
  ```yaml
  title: 示波器
  nav:
  - overview
  - basic_usage
  - ... # 指代所有未指定的文档
  ```

## 参与贡献
### 提交文档
1. Fork 本仓库。
2. 在本地克隆您 Fork 的仓库。
3. 根据上述结构，创建或修改文档。
4. 根据部署一节，预览效果。
5. 提交（Commit）更改并推送（Push）到您的 Fork。
6. 发起 Pull Request。
7. 等待审核。

## 联系我们
您可以直接通过 GitHub Issues 联系我们，或者加入 QQ 群 [948281997](https://h5.qun.qq.com/h5/qun-share-page/?_wv=1027&k=vbIf3zeOmaP8sI6bN1RQB02CzLQRMsDY&authKey=mSBNdIxwjtycOQCpJ5ScTYYlHufmKCb0nYAIcqgvBaO5KMDTijoWHXrDUP2vSHkn&market_channel_source=948281997_1&noverify=0&group_code=948281997)（上电冒烟俱乐部）。

![QQ 群二维码](./docs/introduce/about/qq_group_qr_code.svg)

## 特别鸣谢
本项目受到 [OI Wiki](https://oi-wiki.org/) 启发，特此感谢。
