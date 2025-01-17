# ruff: noqa: E501
# fmt: off
from evidently.future.metric_types import BoundTest
from evidently.future.metric_types import Metric
from evidently.future.metric_types import MetricTest
from evidently.pydantic_utils import register_type_alias

register_type_alias(Metric, "evidently.future.backport.TestsConfig", "evidently:metric_v2:TestsConfig")
register_type_alias(Metric, "evidently.future.metric_types.ByLabelMetric", "evidently:metric_v2:ByLabelMetric")
register_type_alias(Metric, "evidently.future.metric_types.CountMetric", "evidently:metric_v2:CountMetric")
register_type_alias(Metric, "evidently.future.metric_types.SingleValueMetric", "evidently:metric_v2:SingleValueMetric")
register_type_alias(Metric, "evidently.future.metrics.classification.Accuracy", "evidently:metric_v2:Accuracy")
register_type_alias(Metric, "evidently.future.metrics.classification.ClassificationQuality", "evidently:metric_v2:ClassificationQuality")
register_type_alias(Metric, "evidently.future.metrics.classification.ClassificationQualityByLabel", "evidently:metric_v2:ClassificationQualityByLabel")
register_type_alias(Metric, "evidently.future.metrics.classification.F1ByLabel", "evidently:metric_v2:F1ByLabel")
register_type_alias(Metric, "evidently.future.metrics.classification.F1Score", "evidently:metric_v2:F1Score")
register_type_alias(Metric, "evidently.future.metrics.classification.FNR", "evidently:metric_v2:FNR")
register_type_alias(Metric, "evidently.future.metrics.classification.FPR", "evidently:metric_v2:FPR")
register_type_alias(Metric, "evidently.future.metrics.classification.Precision", "evidently:metric_v2:Precision")
register_type_alias(Metric, "evidently.future.metrics.classification.PrecisionByLabel", "evidently:metric_v2:PrecisionByLabel")
register_type_alias(Metric, "evidently.future.metrics.classification.Recall", "evidently:metric_v2:Recall")
register_type_alias(Metric, "evidently.future.metrics.classification.RecallByLabel", "evidently:metric_v2:RecallByLabel")
register_type_alias(Metric, "evidently.future.metrics.classification.RocAucByLabel", "evidently:metric_v2:RocAucByLabel")
register_type_alias(Metric, "evidently.future.metrics.classification.TNR", "evidently:metric_v2:TNR")
register_type_alias(Metric, "evidently.future.metrics.classification.TPR", "evidently:metric_v2:TPR")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.CategoryCount", "evidently:metric_v2:CategoryCount")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.InListValueCount", "evidently:metric_v2:InListValueCount")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.InRangeValueCount", "evidently:metric_v2:InRangeValueCount")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.MaxValue", "evidently:metric_v2:MaxValue")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.MeanValue", "evidently:metric_v2:MeanValue")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.MedianValue", "evidently:metric_v2:MedianValue")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.MinValue", "evidently:metric_v2:MinValue")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.MissingValueCount", "evidently:metric_v2:MissingValueCount")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.OutListValueCount", "evidently:metric_v2:OutListValueCount")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.OutRangeValueCount", "evidently:metric_v2:OutRangeValueCount")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.QuantileValue", "evidently:metric_v2:QuantileValue")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.StatisticsMetric", "evidently:metric_v2:StatisticsMetric")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.StdValue", "evidently:metric_v2:StdValue")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.ValueDrift", "evidently:metric_v2:ValueDrift")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.AlmostConstantColumnsCount", "evidently:metric_v2:AlmostConstantColumnsCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.AlmostDuplicatedColumnsCount", "evidently:metric_v2:AlmostDuplicatedColumnsCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.ColumnCount", "evidently:metric_v2:ColumnCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.ConstantColumnsCount", "evidently:metric_v2:ConstantColumnsCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.DatasetMissingValueCount", "evidently:metric_v2:DatasetMissingValueCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.DuplicatedColumnsCount", "evidently:metric_v2:DuplicatedColumnsCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.DuplicatedRowCount", "evidently:metric_v2:DuplicatedRowCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.EmptyColumnsCount", "evidently:metric_v2:EmptyColumnsCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.EmptyRowsCount", "evidently:metric_v2:EmptyRowsCount")
register_type_alias(Metric, "evidently.future.metrics.dataset_statistics.RowCount", "evidently:metric_v2:RowCount")
register_type_alias(Metric, "evidently.future.metrics.group_by.GroupByMetric", "evidently:metric_v2:GroupByMetric")
register_type_alias(MetricTest, "evidently.future.tests.categorical_tests.IsInMetricTest", "evidently:test_config:IsInMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.categorical_tests.NotInMetricTest", "evidently:test_config:NotInMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.ComparisonTest", "evidently:test_config:ComparisonTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.EqualMetricTest", "evidently:test_config:EqualMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.GreaterOrEqualMetricTest", "evidently:test_config:GreaterOrEqualMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.GreaterThanMetricTest", "evidently:test_config:GreaterThanMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.LessOrEqualMetricTest", "evidently:test_config:LessOrEqualMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.LessThanMetricTest", "evidently:test_config:LessThanMetricTest")

register_type_alias(Metric, "evidently.future.metric_types.MeanStdMetric", "evidently:metric_v2:MeanStdMetric")
register_type_alias(Metric, "evidently.future.metrics.classification.DummyF1Score", "evidently:metric_v2:DummyF1Score")
register_type_alias(Metric, "evidently.future.metrics.classification.DummyPrecision", "evidently:metric_v2:DummyPrecision")
register_type_alias(Metric, "evidently.future.metrics.classification.DummyRecall", "evidently:metric_v2:DummyRecall")
register_type_alias(Metric, "evidently.future.metrics.classification.LogLoss", "evidently:metric_v2:LogLoss")
register_type_alias(Metric, "evidently.future.metrics.classification.RocAuc", "evidently:metric_v2:RocAuc")
register_type_alias(Metric, "evidently.future.metrics.regression.AbsMaxError", "evidently:metric_v2:AbsMaxError")
register_type_alias(Metric, "evidently.future.metrics.regression.MAE", "evidently:metric_v2:MAE")
register_type_alias(Metric, "evidently.future.metrics.regression.MAPE", "evidently:metric_v2:MAPE")
register_type_alias(Metric, "evidently.future.metrics.regression.MeanError", "evidently:metric_v2:MeanError")
register_type_alias(Metric, "evidently.future.metrics.regression.R2Score", "evidently:metric_v2:R2Score")
register_type_alias(Metric, "evidently.future.metrics.regression.RMSE", "evidently:metric_v2:RMSE")
register_type_alias(MetricTest, "evidently.future.tests.categorical_tests.IsInMetricTest", "evidently:test_v2:IsInMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.categorical_tests.NotInMetricTest", "evidently:test_v2:NotInMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.ComparisonTest", "evidently:test_v2:ComparisonTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.EqualMetricTest", "evidently:test_v2:EqualMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.GreaterOrEqualMetricTest", "evidently:test_v2:GreaterOrEqualMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.GreaterThanMetricTest", "evidently:test_v2:GreaterThanMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.LessOrEqualMetricTest", "evidently:test_v2:LessOrEqualMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.LessThanMetricTest", "evidently:test_v2:LessThanMetricTest")
register_type_alias(BoundTest, "evidently.future.metric_types.ByLabelBoundTest", "evidently:bound_test:ByLabelBoundTest")
register_type_alias(BoundTest, "evidently.future.metric_types.CountBoundTest", "evidently:bound_test:CountBoundTest")
register_type_alias(BoundTest, "evidently.future.metric_types.MeanStdBoundTest", "evidently:bound_test:MeanStdBoundTest")
register_type_alias(BoundTest, "evidently.future.metric_types.SingleValueBoundTest", "evidently:bound_test:SingleValueBoundTest")

register_type_alias(Metric, "evidently.future.metrics.column_statistics.DriftedColumnsCount", "evidently:metric_v2:DriftedColumnsCount")
register_type_alias(Metric, "evidently.future.metrics.column_statistics.UniqueValueCount", "evidently:metric_v2:UniqueValueCount")
register_type_alias(Metric, "evidently.future.metrics.regression.DummyMAE", "evidently:metric_v2:DummyMAE")
register_type_alias(Metric, "evidently.future.metrics.regression.DummyMAPE", "evidently:metric_v2:DummyMAPE")
register_type_alias(Metric, "evidently.future.metrics.regression.DummyRMSE", "evidently:metric_v2:DummyRMSE")

register_type_alias(Metric, "evidently.future.metrics.recsys.FBetaTopK", "evidently:metric_v2:FBetaTopK")
register_type_alias(Metric, "evidently.future.metrics.recsys.HitRate", "evidently:metric_v2:HitRate")
register_type_alias(Metric, "evidently.future.metrics.recsys.MAP", "evidently:metric_v2:MAP")
register_type_alias(Metric, "evidently.future.metrics.recsys.MRR", "evidently:metric_v2:MRR")
register_type_alias(Metric, "evidently.future.metrics.recsys.NDCG", "evidently:metric_v2:NDCG")
register_type_alias(Metric, "evidently.future.metrics.recsys.PrecisionTopK", "evidently:metric_v2:PrecisionTopK")
register_type_alias(Metric, "evidently.future.metrics.recsys.RecallTopK", "evidently:metric_v2:RecallTopK")
register_type_alias(Metric, "evidently.future.metrics.recsys.ScoreDistribution", "evidently:metric_v2:ScoreDistribution")
register_type_alias(Metric, "evidently.future.metrics.recsys.TopKBase", "evidently:metric_v2:TopKBase")

register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.NotEqualMetricTest", "evidently:test_v2:NotEqualMetricTest")
register_type_alias(MetricTest, "evidently.future.tests.numerical_tests.EqualMetricTestBase", "evidently:test_v2:EqualMetricTestBase")

register_type_alias(MetricTest, "evidently.future.metrics.column_statistics.ValueDriftTest", "evidently:test_v2:ValueDriftTest")
