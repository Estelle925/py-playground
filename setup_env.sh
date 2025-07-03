#!/bin/bash
# Python基础学习环境配置脚本
# 使用pyenv管理Python版本

echo "=== Python基础学习环境配置 ==="
echo

# 检查是否安装了pyenv
if ! command -v pyenv &> /dev/null; then
    echo "❌ pyenv未安装，请先安装pyenv"
    echo "macOS安装命令: brew install pyenv"
    echo "安装完成后，请将以下内容添加到你的shell配置文件（~/.zshrc 或 ~/.bash_profile）:"
    echo 'export PATH="$HOME/.pyenv/bin:$PATH"'
    echo 'eval "$(pyenv init --path)"'
    echo 'eval "$(pyenv init -)"'
    echo "然后重启终端或运行: source ~/.zshrc"
    exit 1
fi

echo "✅ pyenv已安装"
pyenv --version
echo

# 检查Python 3.11是否已安装
if pyenv versions | grep -q "3.11"; then
    echo "✅ Python 3.11已安装"
else
    echo "📦 正在安装Python 3.11..."
    pyenv install 3.11.0
fi

# 设置本地Python版本
echo "🔧 设置项目Python版本为3.11.0"
pyenv local 3.11.0

# 验证Python版本
echo "📋 当前Python版本信息:"
python --version
which python
echo

# 创建虚拟环境（可选）
read -p "是否创建虚拟环境？(y/n): " create_venv
if [[ $create_venv == "y" || $create_venv == "Y" ]]; then
    echo "🏗️  创建虚拟环境..."
    python -m venv venv
    echo "✅ 虚拟环境创建完成"
    echo "激活虚拟环境: source venv/bin/activate"
    echo "退出虚拟环境: deactivate"
fi

echo
echo "🎉 环境配置完成！"
echo
echo "📚 开始学习:"
echo "1. 查看学习大纲: cat README.md"
echo "2. 运行第一个示例: python 01_variables_and_types/examples.py"
echo "3. 完成练习题: python 01_variables_and_types/exercises.py"
echo "4. 查看答案: python 01_variables_and_types/solutions.py"
echo
echo "💡 提示:"
echo "- 每个章节都有README.md、examples.py、exercises.py和solutions.py"
echo "- 建议按顺序学习，先看README.md了解理论，再运行examples.py"
echo "- 完成exercises.py中的练习后，对比solutions.py中的答案"
echo
echo "Happy coding! 🐍"