"""
Liam Bailey
17/06/2023
This files includes functions to plot the below plots. These plots are part of
SkillCorners analysis team's standard workflow.

SkillCorner Bar Plot
The plot_bar_chart function is used to generate a bar chart based on the given data.
It accepts various parameters such as the DataFrame (df) containing the metric data,
the column to plot on the x-axis (x_value), labels for the x-axis (x_label) and the
unit of measurement (x_unit), groups of players to highlight (primary_highlight_group
and secondary_highlight_group), colors for highlighting (primary_highlight and
secondary_highlight_color), and other optional customization parameters.

SkillCorner Scatter Plot
The plot_scatter function takes a DataFrame (df) and various parameters to plot
a scatter plot. It allows customization of the x-axis (x_value), y-axis (y_value),
and optional z-axis (z_value) values. Additional parameters control labels,
annotations, units, highlighting, colors, and plot aesthetics. The function returns
the Matplotlib figure and axis objects for further manipulation or display.

SkillCorner Swarm & Violin Plots
This code defines a function plot_swarm_violin that plots a swarm/violin plot
using the seaborn and matplotlib libraries. The function takes several parameters
including the DataFrame (`df`), the columns to plot on the x-axis (`x_metric`)
and y-axis (`y_metric`), the categorical values to include on the y-axis
(`y_groups`), and other optional parameters such as labels, colors, and
highlighting specific data points.
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.ticker import EngFormatter
import matplotlib.patheffects as pe
from adjustText import adjust_text
import seaborn as sns
from pkg_resources import resource_filename

fonts = ['resources/Roboto/Roboto-Black.ttf',
         'resources/Roboto/Roboto-BlackItalic.ttf',
         'resources/Roboto/Roboto-Bold.ttf',
         'resources/Roboto/Roboto-BoldItalic.ttf',
         'resources/Roboto/Roboto-Italic.ttf',
         'resources/Roboto/Roboto-Light.ttf',
         'resources/Roboto/Roboto-LightItalic.ttf',
         'resources/Roboto/Roboto-Medium.ttf',
         'resources/Roboto/Roboto-MediumItalic.ttf',
         'resources/Roboto/Roboto-Regular.ttf',
         'resources/Roboto/Roboto-Thin.ttf',
         'resources/Roboto/Roboto-ThinItalic.ttf']

for f in fonts:
    filepath = resource_filename('skillcorner_analysis_toolkit', f)
    fm.fontManager.addfont(filepath)
plt.rcParams["font.family"] = "Roboto"


def plot_bar_chart(df,
                   x_metric,
                   x_label=None,
                   x_unit=None,
                   primary_highlight_group=None,
                   secondary_highlight_group=None,
                   primary_highlight_color='#EE7A6F',
                   secondary_highlight_color='#F6C243',
                   data_point_id='player_name',
                   data_point_label='player_name',
                   plot_title=None,
                   base_color='#80CBA2',
                   figsize=(8, 4)):
    """
    Plot a bar chart using the given data.

    Parameters
    ----------
    df : DataFrame
        Metric DataFrame.
    x_metric : str
        The column in df we want to plot on the x-axis.
    x_label : str, optional
        The label for the x-axis. This should reflect what the x_value is.
    x_unit : str, optional
        If we want to add a unit to the axis values. For example % or km/h.
    primary_highlight_group : list, optional
        A group of players to label & highlight in SkillCorner red.
    secondary_highlight_group : list, optional
        A group of players to label & highlight in SkillCorner yellow.
    primary_highlight : str, optional
        The color for primary highlighted players (default: '#EE7A6F').
    secondary_highlight_color : str, optional
        The color for secondary highlighted players (default: '#F6C243').
    data_point_id : str, optional
        The identifier column for each data point (default: 'player_name').
    data_point_label : str, optional
        The label column for each data point (default: 'player_name').
    plot_title : str, optional
        The title of the plot.
    base_color : str, optional
        The base color for the bars (default: '#80CBA2').
    figsize : tuple, optional
        Tuple (x, y) that defines the dimensions of the figure (default: (8, 4)).

    Returns
    -------
    fig : matplotlib.figure.Figure
        The generated figure.
    ax : matplotlib.axes.Axes
        The generated axes.

    """

    if x_label is None:
        x_label = x_unit

    # Setting the font to our SkillCorner font.
    if primary_highlight_group is None:
        primary_highlight_group = []
    if secondary_highlight_group is None:
        secondary_highlight_group = []

    # Setting plot size & background.
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Sorting the dataframe based on the metric to plot.
    df = df.sort_values(by=x_metric)
    y_pos = range(0, len(df))

    # Plotting bars.
    bars = ax.barh(y_pos,
                   df[x_metric],
                   color=base_color,
                   edgecolor='#0C1B37',
                   lw=0.5,
                   zorder=3,
                   alpha=1)

    # Looping through data & bars to highlight specific players.
    for i, bar in zip(y_pos, bars):
        # If the player has been included in the comparison_players or target_players
        if df[data_point_id].iloc[i] in secondary_highlight_group or \
                df[data_point_id].iloc[i] in primary_highlight_group:
            ax.axhline(i,
                       color='white',
                       zorder=1,
                       linewidth=1)
            ax.axhline(i,
                       color='#0C1B37',
                       zorder=2,
                       linestyle='--',
                       linewidth=0.75)

            bar.set_color(secondary_highlight_color)

        # If the player has been included in the target_players
        if df[data_point_id].iloc[i] in primary_highlight_group:
            bar.set_color(primary_highlight_color)

        # Apply to all bars.
        bar.set_edgecolor('#0C1B37')
        bar.set_linewidth(0.5)

    # Setting x label.
    ax.set_xlabel(x_label,
                  fontweight='bold',
                  fontsize=7)

    # Hiding the top & right spines.
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    # Setting plot elements to #0C1B37.
    ax.spines['left'].set_color('#0C1B37')
    ax.spines['bottom'].set_color('#0C1B37')

    # Setting axis label style params.
    ax.tick_params(axis='x',
                   colors='#0C1B37',
                   labelsize=7)
    ax.tick_params(axis='y',
                   colors='#0C1B37',
                   labelsize=7)

    # Setting y ticks to player names.
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df[data_point_label])

    # Setting player names for those in comparison or target groups to bold.
    for i, tick_label in enumerate(ax.get_yticklabels()):
        if df[data_point_id].iloc[i] in secondary_highlight_group or \
                df[data_point_id].iloc[i] in primary_highlight_group:
            tick_label.set_fontproperties({'weight': 'bold', 'size': 7})
        else:
            tick_label.set_fontproperties({'size': 7})

    ax.yaxis.label.set_color('#0C1B37')
    ax.xaxis.label.set_color('#0C1B37')

    # If an x_unit has been specified, apply it to the x-axis.
    if x_unit is not None:
        formatter0 = EngFormatter(unit=x_unit)
        ax.xaxis.set_major_formatter(formatter0)

    # Add grid.
    ax.grid(color='#0C1B37',
            axis='both',
            linestyle='--',
            linewidth=0.5,
            alpha=0.25,
            zorder=1)

    if plot_title is not None:
        ax.set_title(plot_title, fontweight='semibold', color='#0C1B37')

    for k, spine in ax.spines.items():
        spine.set_zorder(10)

    plt.tight_layout()

    return fig, ax


def plot_scatter(df, x_metric, y_metric, z_metric=None, x_label=None, y_label=None, z_label=None,
                 x_annotation=None, y_annotation=None, x_unit=None, y_unit=None,
                 x_sd_highlight=None, y_sd_highlight=None,
                 primary_highlight_group=None, secondary_highlight_group=None,
                 primary_highlight_color='#EE7A6F', secondary_highlight_color='#F6C243',
                 data_point_id='player_name', data_point_label='player_name',
                 base_color='#80CBA2', avg_line=True, figsize=(8, 4)):
    """
    Plots a scatter plot based on the provided data and configuration.

    Parameters:
        df (DataFrame): The data to be plotted.
        x_metric (str): The column name of the x-axis values.
        y_metric (str): The column name of the y-axis values.
        z_metric (str, optional): The column name of the z-axis values. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
        z_label (str, optional): The label for the z-axis. Defaults to None.
        x_annotation (str, optional): The annotation for the x-axis corners. Defaults to None.
        y_annotation (str, optional): The annotation for the y-axis corners. Defaults to None.
        x_unit (str, optional): The unit of measurement for the x-axis. Defaults to None.
        y_unit (str, optional): The unit of measurement for the y-axis. Defaults to None.
        x_sd_highlight (float, optional): The standard deviation factor for x-axis filtering. Defaults to None.
        y_sd_highlight (float, optional): The standard deviation factor for y-axis filtering. Defaults to None.
        primary_highlight_group (list, optional): A list of player IDs to highlight as primary. Defaults to None.
        secondary_highlight_group (list, optional): A list of player IDs to highlight as secondary. Defaults to None.
        primary_highlight_color (str, optional): The color for primary highlighted players. Defaults to '#EE7A6F'.
        secondary_highlight_color (str, optional): The color for secondary highlighted players. Defaults to '#F6C243'.
        data_point_id (str, optional): The column name for identifying data points. Defaults to 'player_name'.
        data_point_label (str, optional): The column name for labeling data points. Defaults to 'player_name'.
        base_color (str, optional): The base color for the scatter plot. Defaults to '#80CBA2'.
        avg_line (bool, optional): Whether to display average lines. Defaults to True.
        figsize (tuple, optional): The figure size of the plot. Defaults to (8, 4).

    Returns:
        fig, ax: The Matplotlib figure and axis objects.
    """

    if x_label is None:
        x_label = x_metric

    if y_label is None:
        y_label = y_metric

    if secondary_highlight_group is None:
        secondary_highlight_group = []
    if primary_highlight_group is None:
        primary_highlight_group = []

    # Setting plot size & background.
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Calculating and setting size values based on z-axis values.
    if z_metric == 'sum_minutes_played':
        sum_minutes_played = (df['minutes_played_per_match'] * df['count_match']) / 10
        df = df.assign(sum_minutes_played=sum_minutes_played)
    if z_metric is not None:
        old_max = df[z_metric].max()
        old_min = df[z_metric].min()
        new_max = 300
        new_min = 50

        old_range = (old_max - old_min)
        new_range = (new_max - new_min)

        sizes = (((df[z_metric] - old_min) * new_range) / old_range) + new_min
        df = df.assign(size=sizes)
    else:
        df = df.assign(size=100)

    if z_metric is not None and z_label is None:
        z_label = z_metric

    # Filtering data points based on standard deviation factors.
    if x_sd_highlight is not None:
        label_group = df[(df[x_metric] > df[x_metric].mean() + (x_sd_highlight * df[x_metric].std())) |
                         (df[y_metric] > df[y_metric].mean() + (y_sd_highlight * df[y_metric].std())) |
                         (df[data_point_id].isin(secondary_highlight_group)) |
                         (df[data_point_id].isin(primary_highlight_group))]

    # If not, get any players specified in the comparison_players or target_players.
    else:
        label_group = df[(df[data_point_id].isin(secondary_highlight_group)) |
                         (df[data_point_id].isin(primary_highlight_group))]

    # Set style parameters for label_group.
    label_group = label_group.assign(colour=base_color)
    label_group.loc[label_group[data_point_id].isin(secondary_highlight_group), 'colour'] = secondary_highlight_color
    label_group.loc[label_group[data_point_id].isin(primary_highlight_group), 'colour'] = primary_highlight_color
    label_group = label_group.assign(fontweight='bold')
    label_group.loc[label_group[data_point_id].isin(secondary_highlight_group), 'fontweight'] = 'bold'
    label_group.loc[label_group[data_point_id].isin(primary_highlight_group), 'fontweight'] = 'bold'

    # Plotting scatters. Note the default size reflects the total minutes played.
    ax.scatter(df[x_metric],
               df[y_metric],
               c=base_color,
               edgecolor='#0C1B37',
               alpha=0.3,
               lw=0.5,
               s=df['size'],
               zorder=4)

    ax.scatter(label_group[x_metric],
               label_group[y_metric],
               c=label_group['colour'],
               edgecolor='#0C1B37',
               alpha=1,
               lw=0.5,
               s=label_group['size'],
               zorder=5)

    # Adding player_name texts for label group.
    if len(label_group) > 0:
        texts = [ax.text(label_group[x_metric].iloc[i],
                         label_group[y_metric].iloc[i],
                         str(label_group[data_point_label].iloc[i]),
                         color='#0C1B37',
                         fontsize=6,
                         fontweight=label_group['fontweight'].iloc[i],
                         zorder=6,
                         path_effects=[pe.withStroke(linewidth=1.5,
                                                     foreground='white',
                                                     alpha=1)]
                         ) for i in range(len(label_group))]

        # Plotting texts using adjust_text to manage spacing/overlaps.
        adjust_text(texts, ax=ax, expand_points=(1.5, 1.5),
                    force_text=.5,
                    force_points=.5,
                    ha='left',
                    arrowprops=dict(arrowstyle="-",
                                    color='#0C1B37',
                                    alpha=1,
                                    lw=0.5, zorder=6))

    # Add average lines.
    if avg_line == True:
        ax.axvline(df[x_metric].mean(),
                   color='#0C1B37', alpha=0.6, lw=1, linestyle='--', zorder=3, label='Average')
        ax.axhline(df[y_metric].mean(),
                   color='#0C1B37', alpha=0.6, lw=1, linestyle='--', zorder=3)

    # Setting x & y labels.
    ax.set_xlabel(x_label, fontweight='bold', fontsize=7, color='#0C1B37')
    ax.set_ylabel(y_label, fontweight='bold', fontsize=7, color='#0C1B37')

    # Hiding the top & right spines.
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('#0C1B37')

    # Setting plot elements to #0C1B37.
    ax.spines['left'].set_color('none')
    ax.tick_params(axis='x', colors='#0C1B37', labelsize=7)
    ax.tick_params(axis='y', colors='#0C1B37', labelsize=7, length=0)

    # Adding units if they have been specified.
    if x_unit != None:
        formatter0 = EngFormatter(unit=x_unit)
        ax.xaxis.set_major_formatter(formatter0)

    if y_unit != None:
        formatter1 = EngFormatter(unit=y_unit)
        ax.yaxis.set_major_formatter(formatter1)

    # Adding annotation to plot corners.
    # Extending the plot limits to avoid annotating over player scatters.
    if x_annotation != None and y_annotation != None:
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()

        ax.scatter([xmin, xmin, xmax, xmax],
                   [ymin, ymax, ymin, ymax],
                   color='white',
                   zorder=1)

        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()

        # Bottom left.
        ax.text(xmin, ymin,
                r" $\bf{Low}$ " + y_annotation + '\n' + r" $\bf{Low}$ " + x_annotation,
                ha='left',
                va='bottom',
                color='#0C1B37',
                fontsize=6,
                fontweight='regular',
                path_effects=[pe.withStroke(linewidth=1.5,
                                            foreground='white',
                                            alpha=1)])
        # Top left.
        ax.text(xmin, ymax,
                r" $\bf{High}$ " + y_annotation + '\n' + r" $\bf{Low}$ " + x_annotation,
                ha='left',
                va='top',
                color='#0C1B37',
                fontsize=6,
                fontweight='regular',
                path_effects=[pe.withStroke(linewidth=1.5,
                                            foreground='white',
                                            alpha=1)])
        # Bottom right.
        ax.text(xmax, ymin,
                r"$\bf{Low}$ " + y_annotation + '\n' + r"$\bf{High}$ " + x_annotation,
                ha='right',
                va='bottom',
                color='#0C1B37',
                fontsize=6,
                fontweight='regular',
                path_effects=[pe.withStroke(linewidth=1.5,
                                            foreground='white',
                                            alpha=1)])
        # Top right.
        ax.text(xmax, ymax,
                r"$\bf{High}$ " + y_annotation + '\n' + r"$\bf{High}$ " + x_annotation,
                ha='right',
                va='top',
                color='#0C1B37',
                fontsize=6,
                path_effects=[pe.withStroke(linewidth=1.5,
                                            foreground='white',
                                            alpha=1)])

    # Organising plot legend.
    # Adding empty legend handles & labels that reflect scatter size.
    if z_metric != None:
        ax.scatter([], [], c='white', s=5,
                   lw=0.5, edgecolor='white', zorder=3,
                   label=' ')
        ax.scatter([], [], c='white', s=5,
                   lw=0.5, edgecolor='white', zorder=3,
                   label=z_label + ':\n')
        ax.scatter([], [], c='white', s=df['size'].mean() + (1.5 * df['size'].std()),
                   lw=0.5, edgecolor='black', zorder=3,
                   label='High')
        ax.scatter([], [], c='white', s=df['size'].mean(),
                   lw=0.5, edgecolor='black', zorder=3,
                   label='Average')
        ax.scatter([], [], c='white', s=df['size'].mean() - (1.5 * df['size'].std()),
                   lw=0.5, edgecolor='black', zorder=3,
                   label='Low')

    # Adding legend.
    ax.legend(facecolor='white',
              edgecolor='white',
              framealpha=0.6,
              labelcolor='#0C1B37',
              fontsize=6,
              loc='center left',
              bbox_to_anchor=(1.01, 0.5))

    ax.grid(axis='both', color='#0C1B37', alpha=0.2, lw=.5, linestyle='--', )

    plt.tight_layout()

    return fig, ax


def plot_swarm_violin(df,
                      x_metric,
                      y_metric,
                      y_groups=None,
                      x_label=None,
                      y_group_labels=None,
                      x_unit=None,
                      primary_highlight_group=None,
                      secondary_highlight_group=None,
                      data_point_id='player_name',
                      data_point_label='player_name',
                      base_colour='#80CBA2',
                      primary_highlight_color='#EE7A6F',
                      secondary_highlight_color='#F6C243',
                      figsize=(8, 4)):
    """
    Plots a swarm/violin plot.

    Parameters:
    -----------
    df : DataFrame
        Metric DataFrame.
    x_metric : str
        The column in df we want to plot on the x-axis.
    y_metric : str
        The column in df we want to plot on the y-axis. This should be categorical.
    y_groups : list[str], optional
        The categorical values from the y_value column we want to include.
    x_label : str, optional
        The label for the x-axis. This should reflect what the x_value is.
    y_group_labels : list[str], optional
        The labels for the y-axis. This should reflect the data being split across the y-axis.
    x_unit : str, optional
        If we want to add a unit to the axis values. For example % or km/h.
    secondary_highlight_group : list, optional
        A group of players to label & highlight in SkillCorner yellow.
    primary_highlight_group : list, optional
        A group of players to label & highlight in SkillCorner red.
    data_point_id : str, optional
        The column in df that represents the unique identifier for each data point.
    data_point_label : str, optional
        The column in df that contains the labels to display for each data point.
    base_colour : str, optional
        The base color for the plot.
    primary_highlight_color : str, optional
        The highlight color for the primary highlight group.
    secondary_highlight_color : str, optional
        The highlight color for the secondary highlight group.
    figsize : tuple, optional
        The size of the figure (width, height).

    Returns:
    --------
    fig : Figure
        The generated figure.
    ax : Axes
        The axes of the generated plot.
    """

    if y_groups is None:
        y_groups = list(df[y_metric].unique())

    if x_label is None:
        x_label = x_metric

    if y_group_labels is None:
        y_group_labels = y_groups

    if primary_highlight_group is None:
        primary_highlight_group = []

    if secondary_highlight_group is None:
        secondary_highlight_group = []

    # Removing unseemly categories in the y_value column.
    plot_data = df[df[y_metric].isin(y_groups)]

    # Setting size & face colors.
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Plotting violins.
    violin_parts = sns.violinplot(data=plot_data,
                                  x=x_metric,
                                  y=y_metric,
                                  order=y_groups,
                                  inner=None,
                                  width=1,
                                  zorder=5)

    # Setting the style for each violin.
    for pc in violin_parts.collections:
        pc.set_facecolor('#0C1B37')
        pc.set_edgecolor('#0C1B37')
        pc.set_linewidth(0.5)
        pc.set_alpha(0.1)

    # Setting swarm groups: background_players, comparison_players, target_player.
    plot_data = plot_data.assign(swarm_group='background_group')
    plot_data = plot_data.assign(colour=base_colour)

    plot_data.loc[plot_data[data_point_id].isin(primary_highlight_group), 'swarm_group'] = 'primary_highlight_group'
    plot_data.loc[plot_data[data_point_id].isin(primary_highlight_group), 'colour'] = primary_highlight_color

    plot_data.loc[plot_data[data_point_id].isin(secondary_highlight_group), 'swarm_group'] = 'secondary_highlight_group'
    plot_data.loc[plot_data[data_point_id].isin(secondary_highlight_group), 'colour'] = secondary_highlight_color

    sns.set_palette([secondary_highlight_color, primary_highlight_color])
    hue_order = ['secondary_highlight_group', 'primary_highlight_group']

    plot_data = plot_data.sort_values(by=data_point_id)

    # Plotting swarm plot.
    sns.swarmplot(data=plot_data,
                  x=x_metric,
                  y=y_metric,
                  order=y_groups,
                  color=base_colour,
                  alpha=1,
                  size=6.5 - (len(y_groups)),
                  edgecolor='#0C1B37',
                  linewidth=0.1)

    # Plotting swarm plot for highlight data points (larger scatter size).
    if len(primary_highlight_group) > 0 or len(secondary_highlight_group) > 0:
        swarmplots = sns.swarmplot(data=plot_data[plot_data['swarm_group'] != 'background_group'],
                                   x=x_metric,
                                   y=y_metric,
                                   order=y_groups,
                                   hue_order=hue_order,
                                   hue='swarm_group',
                                   alpha=1,
                                   size=10 - (len(y_groups)),
                                   edgecolor='#0C1B37',
                                   linewidth=0.3,
                                   zorder=4)

        # Plotting player names for those specified in target or comparison players.
        # Get the positions of the swarm plot on the axis.
        artists = ax.get_children()
        swarmplot_positions = list(range(len(y_groups) * 2, len(y_groups) * 3))

        for i, group in zip(swarmplot_positions, y_groups):
            # Get the data for specific swarm plot.
            group_df = plot_data[plot_data[y_metric] == group].sort_values(by=x_metric, ascending=True).reset_index()
            label_df = group_df[group_df['swarm_group'] != 'background_group'].reset_index()

            # Match the data points to their jitter y position in the swarm plot.
            offsets = swarmplots.collections[i].get_offsets()

            if len(label_df) == len(offsets):
                label_df.loc[:, 'plotted_metric'] = [tup[0] for tup in offsets]
                label_df.loc[:, 'y'] = [tup[1] for tup in offsets]

                # Add texts for target & comparison players.
                texts = [ax.text(label_df[x_metric].iloc[i],
                                 label_df['y'].iloc[i],
                                 str(label_df[data_point_label].iloc[i]),
                                 color='#0C1B37',
                                 fontsize=5,
                                 fontweight='bold',
                                 zorder=6,
                                 path_effects=[pe.withStroke(linewidth=1,
                                                             foreground='white',
                                                             alpha=1)]
                                 ) for i in range(len(label_df))]

                # Plot texts using adjust_text - only adjust spacing in y-axis.
                adjust_text(texts,
                            ax=ax,
                            add_objects=[artists[i]],
                            expand_points=(1, 3),
                            expand_objects=(1, 3),
                            expand_text=(1, 3),
                            force_objects=.75,
                            force_points=.75,
                            force_text=.75,
                            only_move=dict(points='y', text='y', objects='y'),
                            autoalign='y',
                            arrowprops=dict(arrowstyle="-",
                                            color='#0C1B37',
                                            alpha=1,
                                            lw=.5, zorder=2))

    # Adding x-axis label.
    ax.set_xlabel(x_label,
                  fontweight='bold',
                  fontsize=7)

    # Removing y-axis labels
    ax.set_ylabel('')

    # Setting tick params.
    ax.tick_params(axis='x',
                   colors='#0C1B37',
                   labelsize=7)

    ax.tick_params(axis='y',
                   colors='#0C1B37',
                   labelsize=7)

    # Adding y_labels for each categorical group.
    ax.set_yticklabels(y_group_labels,
                       fontweight='bold')

    # Setting x-axis value unit if specified.
    if x_unit is not None:
        formatter0 = EngFormatter(unit=x_unit)
        ax.xaxis.set_major_formatter(formatter0)

    # Setting plot spines to #0C1B37 or none.
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('#0C1B37')
    ax.yaxis.set_ticks_position('none')
    ax.spines['left'].set_color('None')

    # Limiting x-axis if the value is a percentage.
    xmin, xmax = ax.get_xlim()
    if x_unit == '%' and xmax > 110:
        xmin, xmax = ax.get_xlim()
        ax.set_xlim([xmin, 110])

    # Add grid.
    ax.grid(color='#0C1B37',
            axis='both',
            linestyle='--',
            linewidth=0.5,
            alpha=0.25,
            zorder=1)

    # Remove legend.
    ax.legend().remove()

    plt.tight_layout()

    return fig, ax
