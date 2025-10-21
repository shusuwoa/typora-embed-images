# Typora 图片内嵌脚本 / Typora Embed Images Script

## 使用方法/How to Use
1.  **下载脚本**
    将 `embed_images.py` 脚本下载到你的电脑任意固定位置。

2.  **配置 Typora**
    -   打开 Typora，进入 `偏好设置` -> `导出` -> `HTML`。
    -   在 “导出后运行自定义命令” 一栏中，填入以下命令。
    -   **注意：** 请务必将 `/path/to/your/embed_images.py` 修改为你自己存放脚本的 **绝对路径**。

    ```bash
    cd /path/to/your/typora-embed-images && uv run ./embed_images.py "${outputPath}"  "${currentFolder}"
    ```
---
1.  **Download the Script**
    Download the `embed_images.py` script to a permanent location on your computer.

2.  **Configure Typora**
    -   In Typora, go to `Preferences...` -> `Export` -> `HTML`.
    -   In the "Run custom command after export" field, paste the command below.
    -   **Important:** You must replace `/path/to/your/embed_images.py` with the **absolute path** to where you saved the script.

    ```bash
    uv run --with beautifulsoup4 lxml python /path/to/your/embed_images.py "${outputPath}" "${fileDir}"
    ```


## TODO
- [ ] 打包成一个独立的CLI工具/ Package the script into a standalone Command-Line Interface (CLI).