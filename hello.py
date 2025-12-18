"""
want to dos and now to dos
以EconGym为经济学平台，研究AI+Eco内容
EconGym作为Benchmark+Baseline---->提供实验场景+baseline 算法
如果形成论文，需要做的事情是：
1.讲一个好的故事---使其可以自然的使用EconGym的平台；并且用AI算法，st 可以发到AI刊物上。
2.好的故事不能凭空想出来，所以现在没有好的想法也很正常；AI算法不够了解也无法创新，所以现在不懂框架如何运行也很正常
3.一个验证明确可行的手段是：讲一个故事+提出一个框架---->最终目标是"improve"
4.现在我要：复习这个代码，看懂；其它（想故事，想框架，想一切....----都是不可能马上做完的内容，目前每天做够工作量，已经是我能做到的最好。）
5.gogogo
"""
"""
从项目的角度更新--形成一个论文/idea---->cfg不需要更新，只有这个cfg 才能证明是这个任务场景，选用了此Benchmark，则相关设置不变的
----entity可能会更新，里面有交互逻辑+参数的更新方法，对应数学建模内容；如果提出的东西以算法为主，则可能需要微调算法，如果提出的东西以框架为主，则大概不能动
----env是组合整个entity的内容，代表RL过程，大概率要更新。
----agents是基准算法，大概率要新增一个算法/框架，实现最优的性能；
直观思路：提出一个新的算法/框架，实现最优的性能----同时可以用一个很好的故事讲出来。END
"""
from pathlib import Path

IGNORE = {".git", ".idea", "__pycache__", ".pytest_cache", ".mypy_cache", ".DS_Store","document"}
MAX_DEPTH = 4

def walk(root: Path, prefix: str = "", depth: int = 0):
    if depth > MAX_DEPTH:
        return
    entries = []
    for p in root.iterdir():
        if p.name in IGNORE:
            continue
        entries.append(p)
    entries.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

    for i, p in enumerate(entries):
        last = (i == len(entries) - 1)
        connector = "└── " if last else "├── "
        print(prefix + connector + p.name)
        if p.is_dir():
            ext = "    " if last else "│   "
            walk(p, prefix + ext, depth + 1)

if __name__ == "__main__":
    root = Path(".").resolve()
    print(root.name + "/")
    walk(Path("."))
