#  The MIT License (MIT)
#
#  Copyright (c) 2022. Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from config42 import ConfigManager
from sc_analyzer_base import BaseSummaryDiffAnalyzer


class BranchSummaryGroupByBranchDiffAnalyzer(BaseSummaryDiffAnalyzer):
    """
    机构汇总(按机构分组)差异分析类
    """

    def __init__(self, *, config: ConfigManager, is_first_analyzer=False):
        super().__init__(config=config, is_first_analyzer=is_first_analyzer)

    def _read_config(self, *, config: ConfigManager):
        super()._read_config(config=config)
        # 选中需要处理的机构清单
        self._branch_selected_list = config.get("branch.selected_list")
        # 生成的Excel中Sheet的名称
        self._target_sheet_name = config.get("diff.branch_summary_group_by_branch.target_sheet_name")
        # Sheet名称
        self._sheet_name = config.get("diff.branch_summary_group_by_branch.sheet_name")
        # 表头行索引
        self._header_row = config.get("diff.branch_summary_group_by_branch.header_row")
        # 所属机构列名称（Excel中列名必须唯一）
        index_column_names = config.get("diff.branch_summary_group_by_branch.index_column_names")
        if index_column_names is not None and type(index_column_names) is list:
            self._index_column_names.extend(index_column_names)
        # 待分析差异列名称列表（Excel中列名必须唯一）
        diff_column_dict: dict = config.get("diff.branch_summary_group_by_branch.diff_column_list")
        if diff_column_dict is not None and type(diff_column_dict) is dict:
            self._diff_column_dict.update(diff_column_dict)

    def _filter_origin_data(self, *, data):
        column_name = self._index_column_names[0]
        # 筛选指定部门，删除合计行
        data = data[data[column_name].isin(self._branch_selected_list)]
        # 按机构排序
        data = data.sort_values(
            by=[column_name],
            ascending=True
        )
        return data
