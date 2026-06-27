# SKYK 重庆机长 · 苍茫无人机培训官网

独立站点，与工作室网站分开。  
**不买域名也可以免费上线。**

## 免费访问地址（不用买域名）

推送成功后，网站地址为：

```
https://你的GitHub用户名.github.io/cqcm-skyk/
```

例如 GitHub 用户名是 `zhangsan`，则访问：

```
https://zhangsan.github.io/cqcm-skyk/
```

仓库名里的 **cqcm** 会出现在网址中，和工作室主站完全隔离。

---

## 三步上线（全程免费）

### 第 1 步：注册 GitHub

1. 打开 https://github.com/signup
2. 注册一个免费账号（记住用户名）

### 第 2 步：登录并推送网站

在 PowerShell 中执行：

```powershell
cd "C:\Users\28295\Desktop\重庆苍茫公司网站v2"

# 安装 GitHub 命令行（若还没有）
winget install GitHub.cli

# 登录（按提示在浏览器里点确认）
gh auth login

# 创建仓库并上传（仓库名含 cqcm）
gh repo create cqcm-skyk --public --source=. --remote=origin --push
```

### 第 3 步：开启 GitHub Pages

1. 打开浏览器，进入 `https://github.com/你的用户名/cqcm-skyk`
2. 点 **Settings** → 左侧 **Pages**
3. **Build and deployment** → Branch 选 `master`，文件夹选 `/ (root)`
4. 点 **Save**
5. 等 1～3 分钟，刷新 Pages 页面，会显示绿色网址

---

## 以后想买域名再说

想买 `www.skyk-cqcm.com` 这类域名时：

1. 在阿里云/腾讯云购买域名（约几十元/年）
2. 在项目根目录新建 `CNAME` 文件，内容写：`www.skyk-cqcm.com`
3. 在 GitHub Pages 设置里填同样域名
4. 在域名商添加 DNS 解析（详见购买平台教程）

**现在不需要做任何购买。**

---

## 本地预览

双击 `index.html` 即可在浏览器里看效果。
