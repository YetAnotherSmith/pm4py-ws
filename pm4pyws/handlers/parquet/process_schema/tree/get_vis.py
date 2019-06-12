from pm4py.algo.discovery.dfg.adapters.pandas import df_statistics
from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.algo.filtering.pandas.auto_filter import auto_filter
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.visualization.process_tree import factory as pt_vis_factory
from pm4py.algo.filtering.pandas.attributes import attributes_filter
from pm4py.algo.filtering.pandas.start_activities import start_activities_filter
from pm4py.algo.filtering.pandas.end_activities import end_activities_filter
from pm4py.objects.log.util import xes

from pm4pyws.util import constants


def apply(dataframe, parameters=None):
    """
    Gets the process tree using Inductive Miner Directly-Follows

    Parameters
    ------------
    dataframe
        Dataframe
    parameters
        Parameters of the algorithm

    Returns
    ------------
    base64
        Base64 of an SVG representing the model
    model
        Text representation of the model
    format
        Format of the model
    """
    if parameters is None:
        parameters = {}
    dataframe = attributes_filter.filter_df_keeping_spno_activities(dataframe,
                                                                    max_no_activities=constants.MAX_NO_ACTIVITIES)
    dataframe = auto_filter.apply_auto_filter(dataframe, parameters=parameters)

    activities_count = attributes_filter.get_attribute_values(dataframe, xes.DEFAULT_NAME_KEY)
    activities = list(activities_count.keys())
    start_activities = list(start_activities_filter.get_start_activities(dataframe, parameters=parameters).keys())
    end_activities = list(end_activities_filter.get_end_activities(dataframe, parameters=parameters).keys())

    dfg = df_statistics.get_dfg_graph(dataframe)
    tree = inductive_miner.apply_tree_dfg(dfg, parameters=parameters)
    gviz = pt_vis_factory.apply(tree, parameters={"format": "svg"})
    return get_base64_from_gviz(gviz), None, "", "parquet"
