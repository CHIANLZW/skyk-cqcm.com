# SKYK 重庆机长 · 苍茫无人机培训官网

> 独立站点，与工作室网站完全隔离  
> 正式访问地址：**https://www.skyk-cqcm.com**

## 访问地址

| 类型 | 地址 |
|------|------|
| 自定义域名（推荐） | https://www.skyk-cqcm.com |
| GitHub Pages 备用 | https://你的GitHub用户名.github.io/cqcm-skyk/ |

域名中的 **cqcm** 代表 **C**hongqing **C**ang**m**ang（重庆苍茫），与工作室主站分离。

## 推送到 GitHub（独立仓库）

在终端执行：

```bash
cd "C:\Users\28295\Desktop\重庆苍茫公司网站v2"

# 1. 登录 GitHub（首次需要）
gh auth login

# 2. 创建独立仓库并推送（仓库名含 cqcm，不与工作室混用）
gh repo create cqcm-skyk --public --source=. --remote=origin --push

# 3. 开启 GitHub Pages（自定义域名）
gh api repos/{owner}/cqcm-skyk/pages -X POST -f build_type=legacy -f source[branch]=main -f source[path]=/
```

若仓库默认分支是 `master`，将上面命令中的 `main` 改为 `master`。

## 域名解析（skyk-cqcm.com）

在域名服务商处添加：

| 记录类型 | 主机记录 | 记录值 |
|---------|---------|--------|
| CNAME | www | 你的GitHub用户名.github.io |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

然后在 GitHub 仓库 **Settings → Pages → Custom domain** 填写 `www.skyk-cqcm.com`。

## 本地预览

直接双击 `index.html`，或：

```bash
npx serve .
```

## 目录说明

```
index.html          # 首页
css/                # 样式
js/                 # 脚本
assets/             # 图片、证书 PDF、宣传册
CNAME               # GitHub Pages 自定义域名
```

原始素材文件夹 `培训点宣传材料/` 已加入 .gitignore，不上传 GitHub。
